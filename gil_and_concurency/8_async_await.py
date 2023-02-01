import asyncio
# Example with 2 funcs: One of them generates numbers with values from 1 to infinity, and second is return to print
# some message each several seconds.


# in 3.4 python version init-n of coroutine has possible with decorator of coroutine:
# @asyncio.coroutine  # isn't decorator with initialization. Only creation coroutine based on generators from func.
async def print_nums():
    num = 1
    while True:
        print(num)
        num += 1
#       yield from asyncio.sleep(1) - for python 3.4v
        await asyncio.sleep(0.1)

async def print_time():
    count = 0
    while True:
        if count % 2 == 0:
            print('{} seconds have passed'.format(count))
        count += 1
        await asyncio.sleep(1)

async def main():
    task1 = asyncio.create_task(print_nums())
    task2 = asyncio.create_task(print_time())

    await asyncio.gather(task1, task2)

if __name__ == '__main__':
    # loop = asyncio.get_event_loop()
    # loop.run_until_complete(main())
    # loop.close()
    # all of this code can replace to run method: (supported from 3.7 ver.)
    asyncio.run(main())

