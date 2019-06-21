import time
import threading

from simple_rest_client.api import API


keep_running = threading.Event()
mut = threading.Lock()

def foo():
    while True:
        #mut.acquire()
        print("Keep running thread {}".format(threading.currentThread().getName()))
        if keep_running.is_set():
            print("Stopping thread {}".format(threading.currentThread().ident))
            #mut.release()
            break
        time.sleep(1)
        #mut.release()


def main_impl_2():
    app = API (api_root_url="https://jsonplaceholder.typicode.com",
               params={},
               headers={},
               timeout=2,
               append_slash=False,
               json_encode_body=True)
    app.add_resource(resource_name="comments")
    print(app.comments.actions)

    resp = app.comments.list(body=None, params={}, headers={})
    print("{}\n{}\n{}\n{}\n".format(resp.url, resp.method, resp.headers, resp.body))

    body=resp.body
    for i,r in enumerate(body):
        print(body[i]["name"])



def main_impl_1():

    print("Starting Thread")

    tlist = []

    for tn in range(20):
        tlist.append(threading.Thread(target=foo, name="{} Thread".format(tn)))

    for t in tlist:
        t.start()

    time.sleep(10)

    keep_running.set()

    for t in tlist:
        t.join()

if __name__ == '__main__':
    main_impl_2()
