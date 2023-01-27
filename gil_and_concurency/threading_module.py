from threading import *
from time import sleep
from datetime import datetime

def testtime(func):
  def wrapper(*args):
    print(f'test time {func.__name__} start...')
    start_time = datetime.now()
    func(*args)
    print('function time start in: ', start_time)

  return wrapper

@testtime
def first_func(num):
    sleep(num)

@testtime
def second_func(num):
    sleep(num)

# test1_first = first_func(1.2)   # ...time start in:  2023-01-26 12:29:49.980439
# test1_second = second_func(1.4) # ...time start in:  2023-01-26 12:29:51.181915


# next step: create 2 threads for parallel perfomance:

th1 = Thread(target=first_func, args=(1.2,))
th2 = Thread(target=second_func,  args=(1.3,))

th1.start() # ...time start in:  2023-01-26 12:44:41.040990   - 1-й
th2.start() # ...time start in:  2023-01-26 12:44:41.046777   - 3-й

test3 = first_func(1.2) # ...time start in:  2023-01-26  12:44:41.046606  - 2-й
# for non-parallel perfomance of all code, use .join() method. It will allow to continue working only after th1 and th2
# threads complete the work

th1.join()
th2.join()
test4 = first_func(1.2) # ...time start in:  2023-01-26 12:44:42.348236   - 4-й

# several threads can work with one func in parallell!



