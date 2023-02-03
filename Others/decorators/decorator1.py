import time

def testtime(func):

    def wrapper(*args, **kwargs):
        print(f'test time {func.__name__} start...')
        start = time.time()
        func(*args, **kwargs)
        endtime = time.time() - start
        print('function time is: ', endtime.__round__(2))

    return wrapper

@testtime
def fib_fast_loop(index):
    a, b = 0, 1

    for i in range(index - 1):
        a, b = b, a + b

    return b

# fib_fast_loop(300000)   # function time is 1.53 sec.
# fib_fast_loop(400000)   # function time is 2.76 sec.