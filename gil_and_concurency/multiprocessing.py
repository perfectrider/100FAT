import multiprocessing
from Others.decorators.decorator1 import testtime


# 1. CPU Bound.
@testtime
def f(value):
    result = 0
    for x in range(value):
        result = result + x * x
    return result


test_value_1 = 10000000
# f(test_value_1) # function time is:  1.6


# 2. 2-nd step: separate process

if __name__ == '__main__':
    test_value_1 = 10000000
    p = multiprocessing.Process(target)


