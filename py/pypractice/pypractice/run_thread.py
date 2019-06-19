import time
import threading


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



if __name__ == '__main__':
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