import sys
import asyncio

def getInput():
    return input("Continue? : ")
    

def loop_one(times: int):
    iter=1
    while( times ):
        print("Doing %d" % iter)
        iter = iter + 1
        times = times - 1
        s = getInput()

        if( "Y" == s.upper() or "YES" == s.upper()):
            continue
        else:
            print("Done then")
            break;

async def loop_in_thread(loop):
    await loop.run_in_executor(None,loop_one(10))
    
async def f(name, delay, iter_count):
    try:
        i = iter_count
        while(i):
            print(f"calling {name}")
            i = i - 1
            await asyncio.sleep(delay)

    except StopIteration as e:
        print(f"stopping {name}")
    except asyncio.CancelledError as ee:
        print("Some other exception {1} " % type(ee))
    except BaseException as be:
        print("Some other exception {1} " % type(be))
    finally:
        print(f"Done {name}")


loop = asyncio.get_event_loop()

loop2 = asyncio.new_event_loop()

print( loop2 is loop )

tasks = [f("one", 1, 10),f("two", 2, 6),f("three", 3, 3)]
tasks2 = [f("one-1", 1, 10),f("two-2", 2, 6),f("three-3", 3, 3)]

for t in tasks:
    loop.create_task(t)

g = asyncio.Task.all_tasks(loop=loop)
print(g)
print(type(g))
fg = asyncio.gather(*g)
print(type(fg))

for t in tasks2:
    loop2.create_task(t)

loop.run_until_complete(fg)

loop2.run_until_complete(asyncio.gather(*asyncio.Task.all_tasks(loop=loop2)))

loop.stop()
loop2.stop()

loop.close()
loop2.close()
