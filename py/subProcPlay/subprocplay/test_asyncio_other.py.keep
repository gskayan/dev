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

tasks = [f("one", 1, 100),f("two", 2, 6),f("three", 3, 3)]

number=10
for t in range(number):
    loop.create_task(f(f"task-{t}", float(t/number), 10))

g = asyncio.Task.all_tasks(loop=loop)
fg = asyncio.gather(*g)

loop.run_until_complete(fg)

#loop.stop()

#loop.close()
