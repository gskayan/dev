import time
import threading


keep_running = threading.Event()
mut = threading.Lock()

def foo():
    while True:
        mut.acquire()
        print("Keep running thread {}".format(threading.currentThread().getName()))
        if keep_running.is_set():
            print("Stopping")
            mut.release()
            break
        time.sleep(1)
        mut.release()



if __name__ == '__main__':
    print("Starting Thread")

    t = threading.Thread(target=foo, name="First Thread")

    t1 = threading.Thread(group=None, target=foo, name="Second Thread")

    t1.start()

    t.start()

    time.sleep(10)

    keep_running.set()

    t.join()