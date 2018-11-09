import asyncio
import threading
import time

def blocking(name, delay, times):
    while(times):
        tid = threading.current_thread().ident
        print(f"running blocking {name}. thread id {tid}")
        time.sleep(delay)
        times = times - 1

async def ablocking(name, delay, times):
    while(times):
        tid = threading.current_thread().ident
        print(f"running blocking {name}. thread id {tid}")
        await asyncio.sleep(delay)
        times = times - 1

loop = asyncio.get_event_loop()
loop.run_in_executor(None, blocking, "in-executor-3", 0.3, 10)
loop.run_in_executor(None, blocking, "in-executor-2", 0.2, 10)
loop.run_in_executor(None, blocking, "in-executor-1", 0.1, 10)

loop.create_task(ablocking("on-event-loop-1", 0.1, 5))
loop.create_task(ablocking("on-event-loop-2", 0.15, 5))
loop.create_task(ablocking("on-event-loop-3", 0.25, 5))

loop.run_until_complete(asyncio.gather(*asyncio.Task.all_tasks(loop=loop)))

        
if __name__=="__main__":
    t = threading.Thread(target=blocking, args=("in-thread", 1,10))
    t.start()
    blocking("in-main", 2, 5)
    t.join()
