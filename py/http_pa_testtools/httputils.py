#!/opt/bb/bin/python3.7

import argparse
import logging
import os
import uuid
import threading
import http.server
import concurrent.futures

_DEFAULT_PORT = 23456

class BCIHttpRequestHandler(http.server.BaseHTTPRequestHandler):

    def do_POST(self):
        logging.debug(f"Request Path {self.path}")
        logging.info(f"Request Headers {self.headers}")
        clen = int(self.headers["Content-Length"])
        reqId = self.headers["BCI-Request-Id"]
        payload = self.rfile.read(clen).decode("utf-8")
        logging.debug("BCIHttpRequestHandler received request {}".format(payload))

        '''Echo payload back in the response'''
        self.send_response(http.server.HTTPStatus.OK)
        self.send_header("Content-type", "application/json")
        self.send_header("Content-Length", str(len(payload)))
        self.send_header("BCI-Request-Id", reqId)
        self.end_headers()
        self.wfile.write(payload.encode("utf-8"))

    def do_GET(self):
        self.do_POST()

def send_http(url, resource, messages, match_key_field, method="POST"):

    responses = []
    def build_url(url, resource):
        if resource is not None:
            return url + resource
        return url

    def validate_response(req_hdrs:dict, resp_hdrs:dict, match_key_field):
        if None != match_key_field:
            assert req_hdrs[match_key_field] == resp_hdrs[match_key_field], \
                f"Response '{match_key_field}:{resp_hdrs[match_key_field]}' != Request '{match_key_field}:{req_hdrs[match_key_field]}'"

    import requests
    target = build_url(url, resource)
    action = getattr(requests, method.lower())

    for m in messages:
        logging.debug("Request msg : {} - {}".format(m, match_key_field))
        req_headers = {match_key_field:m[match_key_field]}
        logging.debug(f"URL target: {target}")
        resp = action(url=target, json=m, headers=req_headers)

        logging.debug(f"Response code {resp.status_code}")

        if requests.codes.ok == resp.status_code:
            logging.debug("Response headers: {}".format(resp.headers))
            resp_payload = resp.json()
            logging.debug("Response json: {}".format(resp_payload))
            validate_response(req_headers, resp.headers, match_key_field)
            responses.append(resp_payload)
    return responses

def run_http_server(stopflag: threading.Event,
                    port=_DEFAULT_PORT):

    handler = BCIHttpRequestHandler

    def watcher(stopflag: threading.Event, httpserv: http.server.HTTPServer):
        import time
        while not stopflag.is_set():
            time.sleep(1)
        httpserv.shutdown()

    import os

    with http.server.HTTPServer((os.uname().nodename, port), handler) as httpd:
        logging.info("Starting http server on port %d" % port)
        watch = threading.Thread(target=watcher, args=([stopflag, httpd]))
        watch.start()
        httpd.serve_forever()
        watch.join()

default_message_generator = "lambda count, key='BCI-Request-Id':([{'index': i, key: str(uuid.uuid4())} for i in range(count)], key)"

def run_http_client(message_generator=default_message_generator,
                    url ="http://" + os.uname().nodename,
                    port=_DEFAULT_PORT,
                    rest_resource=None,
                    http_method="POST",
                    messages_to_send=1):

    urlpath = url + ":" + str(port) + "/"
    resource = rest_resource
    method=http_method
    logging.info(f"Starting http client to URL: {urlpath}, METHOD: {method}, RESOURCE: {resource}")

    try:
        messages, match_key_field = eval(message_generator)(messages_to_send)
        responses = send_http(urlpath, resource, messages, match_key_field=match_key_field, method=method)
        assert messages == responses, "Requests list does not match Response list"
    finally:
        pass

class Params():
    def __init__(self):
        args = self._get_args()
        self.start_server=args.local_server
        self.debug_mode = args.debug
        self.url=args.url
        self.resource = args.resource
        self.port = args.port
        self.http_method = args.method
        self.msg_count = args.count
        self.max_workers = args.workers
        self.msg_generator = args.message_generator

    def _get_args(self):

        argparser = argparse.ArgumentParser()

        argparser.add_argument("--debug",
                               help="Enable DEBUG level of logging",
                               action="store_true")
        argparser.add_argument("-s", "--local_server",
                               help="Start local http server",
                               action="store_true")
        argparser.add_argument("--url", type=str,
                               help="URL for client connection (default:'http://" + os.uname().nodename + "')",
                               default="http://" + os.uname().nodename)
        argparser.add_argument("--resource", type=str,
                               help="URL resource",
                               default="")
        argparser.add_argument("--port", type=int,
                               help="Listen port (default:" + str(_DEFAULT_PORT) + ")",
                               default=_DEFAULT_PORT)
        argparser.add_argument("--method", type=str, choices=["POST", "GET"],
                               help="HTTP method to use (default:POST)",
                               default="POST")
        argparser.add_argument("--count", type=int,
                               help="Number of messages to send (per http client thread) (default:1)",
                               default=1)
        argparser.add_argument("--workers", type=int,
                               help="Number of http clients to spawn in parallel (default:1)",
                               default=1)
        argparser.add_argument("--message_generator",
                               help="Message generation lambda/function. This should be experession which will be executed with 'eval().'\
                               lambda takes 'params for number of messages ot generate and returns a list of messages \
                                and a string value to use as request/response match key. \
                                Example: \'lambda count, key='guid':([{'index': i, key: str(uuid.uuid4())} for i in range(count)], key)\'",
                                default=default_message_generator)

        return argparser.parse_args()

class LocalServer():
    def __init__(self, params:Params):
        self.stopflag = threading.Event()
        self.target = run_http_server
        self.start_server = params.start_server
        self.port = params.port

    def __enter__(self):
        self.serv = threading.Thread(target=self.target,
                                     args=([self.stopflag]),
                                     kwargs={"port": self.port})
        if self.start_server: self.serv.start()

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.stopflag.set()
        if self.start_server: self.serv.join()

class LocalClient():
    def __init__(self, params):
        self.url=params.url
        self.resource = params.resource
        self.port = params.port
        self.http_method = params.http_method
        self.msg_count = params.msg_count
        self.max_workers = params.max_workers
        self.msg_generator = params.msg_generator
        self.event = threading.Event()
        self.fut_list = []

    def __enter__(self):
        """Create parallel execution facility"""
        self.executor = concurrent.futures.ThreadPoolExecutor(max_workers=self.max_workers)
        self.params = {"message_generator": self.msg_generator,
                        "url": self.url,
                        "rest_resource":self.resource,
                        "port": self.port,
                        "http_method": self.http_method,
                        "messages_to_send": self.msg_count}
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        """Collect results ( if any )"""
        for f in concurrent.futures.as_completed(self.fut_list):
            d = f.result()

    def run(self):
        """Start http client(s) in a thread pool"""
        self.fut_list = [self.executor.submit(run_http_client, **self.params) for _ in range(self.max_workers)]
        self.event.set()

    def wait(self):
        self.event.wait()

if __name__== "__main__":

    params = Params()

    logging.basicConfig(level=logging.DEBUG if params.debug_mode == True else logging.INFO)

    with LocalServer(params=params):
        with LocalClient(params=params) as lc:
            lc.run()
            lc.wait()
