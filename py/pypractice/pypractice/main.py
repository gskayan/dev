import inspect
import sys


def getprimelist( num : int ):
        for i in range(1,num+1):
                r = [d for d in range(1,num+1) if i%d == 0]
                if 2 == len(r) and 1 == r[0] and i == r[1]:
                        print(i)

def overlap_lists(x:list, y:list):
        return [*set([*x, *y])]

def main_impl():
        _n_ = inspect.currentframe().f_code.co_name
        print(f"Starting: {_n_}")
        getprimelist(int(sys.argv[1]))

        a = range(0, 10, 3)
        b = range(0, 20, 5)
        
        print(overlap_lists(a,b))
        print(f"Stopping: {_n_}")

if __name__ =="__main__":
        main_impl()

