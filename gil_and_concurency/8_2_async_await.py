import requests
from Others.decorators.decorator1 import testtime

# Example with testing downloading the image from my site in non-asynch and asynchronous modes.



# 1. Non-asynch realization:
# def get_file(url):
#     r = requests.get(url)
#     return r
#
# def write_file(response):
#     filename = response.url.split('/')[-1]
#     with open(filename, 'wb') as file:  # write in binary
#         file.write(response.content)    # .content method => open in binary
#
# @testtime
# def main():
#     url = 'https://perfectride.ru/fitnessblog/media/images/python-logo.jpg'
#     for i in range(10):
#         write_file(get_file(url))
#
#     return
#
# if __name__ =='__main__':
#     main()



# 2. Asynch realization:
import asyncio
import aiohttp
from time import time

def write_file(data):
    filename = 'file-{}.jpeg'.format(int(time() * 1000))
    with open(filename, 'wb') as file:
        file.write(data)

async def get_file(url, session):
    async with session.get(url, allow_redirects=True) as response:
        data = await response.read()    # return binary data
        write_file(data)

# @testtime
async def main():
    url = 'https://loremflickr.com/320/240'
    tasks = []

    async with aiohttp.ClientSession() as session:
        for i in range(10):
            task = asyncio.create_task(get_file(url, session))
            tasks.append(task)

        await asyncio.gather(*tasks)

start_time = time()
asyncio.run(main())
print((time() - start_time))
