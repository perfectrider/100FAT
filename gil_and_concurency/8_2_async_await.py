import requests
from Others.decorators.decorator1 import testtime

# Example with testing downloading the image from my site in sequency and asynchronous modes.


def get_file(url):
    r = requests.get(url)
    return r

def write_file(response):
    filename = response.url.split('/')[-1]
    with open(filename, 'wb') as file:  # write in binary
        file.write(response.content)    # .content method => open in binary

@testtime
def main():
    url = 'https://perfectride.ru/fitnessblog/media/images/python-logo.jpg'
    for i in range(10):
        write_file(get_file(url))

    return

if __name__ =='__main__':
    main()