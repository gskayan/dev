import logging
import sys
import cmd
import argparse
import json
from collections import namedtuple
from simple_rest_client import api




class CmdHandler(cmd.Cmd):
    prompt="enter command >>"
    def __init__(self, log):
        super(CmdHandler, self).__init__()
        self.mylog = log
        self.mylog.info("Initialized command handler")

    def do_exit(self, none=None):
        return self

    def do_stuff(self, none=None):
        self.mylog.info("Stuff")

    def do_hello(self, none=None):
        ''' hello
        Being polite '''
        self.mylog.info("hello() called")

    def do_gettime(self, isUtc=True):
        ''' gettime
        Returns current timestamp in UTC. If argument is False, returns current local timestamp'''
        import datetime
        cur_time = datetime.datetime.now()
        if isUtc:
            cur_time = datetime.datetime.utcnow()
        self.mylog.info("Time now is : {time}".format(time=cur_time))

    def do_call_rest(self, none=None):
        caller = api.API(api_root_url="http://jsonplaceholder.typicode.com",
                         headers={},
                         params={},
                         timeout=5,
                         append_slash=False,
                         json_encode_body=True)

        caller.add_resource(resource_name="users")
        self.mylog.info("Resources: \n{}".format(caller.users.list(body=None, params={}, headers={})))
        obj = caller.users.list(body=None, params={"id":1}, headers={}).body[0]
        self.mylog.info("Resources: \n{}".format(obj["address"]))

logging.basicConfig(level=logging.INFO,
                    stream=sys.stdout,
                    format="%(asctime)s: %(filename)s:%(name)s - %(levelname)s: %(message)s")

log = logging.getLogger("http_pa_tools")

def run_commandHander():
    log.info("Interactive Command Hander")
    CmdHandler(log).cmdloop()


if __name__ == "__main__":

    pp = argparse.ArgumentParser()
    pp.add_argument("--file", help="Configurtation file to load", default="config.json")
    params = pp.parse_args()

    tests_to_run = []

    with open(params.file, "r") as f:
        cfg = json.load(f, object_hook=lambda l: namedtuple("cfgValue", l.keys())(*l.values()))
        log.info(f"Read : {cfg}")

        tests_to_run = [globals()[i.mode] for i in cfg.config if i.active == True]

        log.info(f"Will run these tests {tests_to_run}")

        for f in tests_to_run: f()




