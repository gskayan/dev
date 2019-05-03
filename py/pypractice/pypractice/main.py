#!/opt/bb/bin/python3.7


import argparse
import inspect
import sys
import functools


def print_func_name(f):
    @functools.wraps(f)
    def runit(*args, **kwargs):
        print("Running %s" % f.__name__)
        f(*args, **kwargs)
    return runit


def _generate_prime_list(num: int):
    primes = []
    for i in range(1, num+1):
        r = [d for d in range(1, num+1) if i % d == 0]
        if 2 == len(r) and 1 == r[0] and i == r[1]:
            primes.append(i)
    return primes

@print_func_name
def getprimelist():
    num = int(input("Enter a number: "))
    primes = _generate_prime_list(num)
    print(f"Primes up to {num} are [{primes}]")


@print_func_name
def mergelists():
    d = ","
    a_str = input(f"Enter first list range <start>{d}<end>{d}[<step>]:")
    b_str = input(f"Enter second list range <start>{d}<end>{d}[<step>]:")

    def str2rangeArgs(s: str, delim: str):
        params = s
        try:
            intlist = [int(i) for i in s.split(delim) if len(i.strip()) > 0]
        except ValueError as ve:
            raise ValueError(f"Input format invalid: '{params}'")

        if len(intlist) < 2:
            raise Exception(f"Insufficient params for range: '{params}'")
        if 2 == len(intlist):
            return [*range(intlist[0], intlist[1])]
        elif 3 >= len(intlist):
            return [*range(intlist[0], intlist[1], intlist[2])]
        else:
            raise Exception(f"Range generation failed: '{params}'")

    a = str2rangeArgs(a_str, d)
    b = str2rangeArgs(b_str, d)

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

    print(FUNCLIST)

    if funcname is not None:
        FUNCLIST[funcname]()
    else:
        print("Running all functions")
        for f in FUNCLIST.values():
            f()

    print(f"Stopping: {_n_}")


if __name__ == "__main__":
    main_impl()
