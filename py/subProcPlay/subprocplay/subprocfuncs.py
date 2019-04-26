import os
import time

def subproc_func(repeatCount:int):
    i = repeatCount
    while 0 < repeatCount:
        print("Testing subproc_func: procid = {0}".format(os.getpid()))
        repeatCount = repeatCount - 1
        time.sleep(1)

def run_subproc(cmdstr:str, cmdargs:str, runincwd:str):
    import subprocess as sp
    print("My cwd is : %s" % os.getcwd())
    mysp = sp.run(cmdstr + " " + cmdargs, cwd=runincwd, shell=True)

    print(f"Sub process completed with return code {0}".format(mysp.returncode))
