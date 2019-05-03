#!/opt/bb/bin/python3.7


import argparse
import functools
import inspect
import mypracticefuncs as mypf
import sys


def print_func_name(f):
    @functools.wraps(f)
    def runit(*args, **kwargs):
        print("Running %s" % f.__name__)
        f(*args, **kwargs)
    return runit


@print_func_name
def getprimelist():
    num = int(input("Enter a number: "))
    primes = mypf._generate_prime_list(num)
    print(f"Primes up to {num} are [{primes}]")


@print_func_name
def mergelists():
    d = ","
    a_str = input(f"Enter first list range <start>{d}<end>{d}[<step>]:")
    b_str = input(f"Enter second list range <start>{d}<end>{d}[<step>]:")

    a = mypf.str2rangeArgs(a_str, d)
    b = mypf.str2rangeArgs(b_str, d)

    res = [*set([*a, *b])]
    print(f"New list : {res}")


def randomguess():
    import random
    comp_range = [*range(1, 10)]
    while True:
        try:
            rn = random.randint(1, 9)
            un = int(input(f"Number in {comp_range} inclusive range : "))
            if un not in comp_range:
                raise ValueError(f"'{un}' out of range {comp_range}")
                diff = un - rn
                if 0 < diff:
                    print(f"Bad guess {un} < {rn}. Try again")
                    continue
                elif 0 > diff:
                    print(f"Bad guess {un} > {rn}. Try again")
                    continue
                else:
                    print(f"Good guess {un} == {rn}")
                    resp = input("Play more? (y/n)")
                    if "y" == resp.lower():
                        continue
                    else:
                        print("Good game!")
                        break
        except ValueError as ve:
            print(str(ve) + " Try again")
            continue
        else:
            raise Exception("Something else is wrong")


FUNCLIST = {"primelist": getprimelist,
            "mergelists": mergelists,
            "randomguess": randomguess}


def main_impl():
    _n_ = inspect.currentframe().f_code.co_name
    print(f"Starting: {_n_}")

    pp = argparse.ArgumentParser("Function to run choice")
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


if __name__ == "__main__":
    main_impl()
