import os

def get_some_info():
    return os.curdir, os.cpu_count()

if __name__ == "__main__":
    projName, cpuCnt = get_some_info()
    print(f'Welcome to dir: {projName:s}, I have {cpuCnt:d} cpus')
