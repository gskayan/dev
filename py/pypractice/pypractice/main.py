import inspect
import sys
import argparse


def getprimelist():
        num = int(input("Enter a number: "))
        primes = []
        for i in range(1,num+1):
                r = [d for d in range(1,num+1) if i%d == 0]
                if 2 == len(r) and 1 == r[0] and i == r[1]:
                        primes.append(i)
        print(f"Primes up to {num} are [{primes}]")

def mergelists():
        delim=","
        a_str = input(f"Enter first list range <start>{delim}<end>{delim}[<step>] : ")
        b_str = input(f"Enter second list range <start>{delim}<end>{delim}[<step>] : ")

        def str2rangeArgs( s:str, delim:str ):
                try:
                        intlist = [int(i) for i in s.split(delim)]
                except ValueError as ve:
                        raise ValueError(f"Can not process input string : '{s}'. Please follow format")
                if 2 == len(intlist):
                        return [*range(intlist[0], intlist[1])]
                elif 3 >= len(intlist):
                        return [*range(intlist[0], intlist[1], intlist[2])]                        
                else:
                        raise Exception(f"Can not generate range arguments from string : '{s}'")

        a = str2rangeArgs(a_str, delim)
        b = str2rangeArgs(b_str, delim)
        
        res= [*set([*a, *b])]
        print(f"New list : {res}")


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

        if funcname is not None:
                FUNCLIST[funcname]()
        else:
                print("Running all functions")
                for f in FUNCLIST.values():
                        f()

        print(f"Stopping: {_n_}")

if __name__ =="__main__":
        main_impl()

