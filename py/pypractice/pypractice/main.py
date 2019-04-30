import inspect
import sys
import argparse


def getprimelist():
        print("Enter a number: ")
        num = int(input())
        primes = []
        for i in range(1,num+1):
                r = [d for d in range(1,num+1) if i%d == 0]
                if 2 == len(r) and 1 == r[0] and i == r[1]:
                        primes.append(i)
        print(f"Primes up to {num} are [{primes}]")

def mergelists():
        a = range(0, 10, 3)
        b = range(0, 20, 5)

        def doit( x:list, y:list):
                return [*set([*x, *y])]
        print(doit(a,b))


FUNCLIST={"primelist":getprimelist, 
          "mergelists":mergelists
}

def main_impl():
        _n_ = inspect.currentframe().f_code.co_name
        print(f"Starting: {_n_}")
        
        pp = argparse.ArgumentParser("Parameter determining which test function to run")
        pp.add_argument("--run", 
                        choices=[*FUNCLIST],
                        help="Run funciton from the list")        
        params = pp.parse_args()
        
        funcname = params.run

        print(f" funcname = {funcname}")
        if funcname:
                FUNCLIST[funcname]()
        else:
                print("Running all functions")
                for f in FUNCLIST.values():
                        f()

        print(f"Stopping: {_n_}")

if __name__ =="__main__":
        main_impl()

