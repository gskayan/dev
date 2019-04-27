import inspect
import os
import subprocfuncs as spf
import timeit

def main_impl():
        _n_ = inspect.currentframe().f_code.co_name
        pid = os.getpid()
        print(f"Starting: {_n_} : pid: {pid}")

        import argparse
        pp = argparse.ArgumentParser()
        pp.add_argument("--command", metavar="cmdstr", type=str, help="Program to run")
        pp.add_argument("--args", metavar="cmdargs", type=str, help="Program args")
        pp.add_argument("--runincwd", metavar="run_in_cwd", type=str, help="Run from cwd")
        params = pp.parse_args()

        spf.run_subproc(params.command, params.args, params.runincwd)
        print(f"Stopping: {_n_}")

if __name__ =="__main__":
        main_impl()
