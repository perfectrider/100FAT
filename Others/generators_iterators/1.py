# 1. Generations object and func.

a = (x for x in range(10))
print(a)    # <generator object <genexpr> at 0x7f0b4cff6880>

print(next(a))  # 0
print(next(a))  # 1


a = [1, 2, 3]
a = iter(a)
print(next(a))  # 1
print(next(a))  # 2
print(next(a))
# print(next(a))  # !StopIteration


# a = list(range(10000000000000000000000)) -> memoryError
a = (range(1000000000000000000000))
for i in a:
    if i > 89 and i <= 100:
        print(i)    # 90, 91 ... 100
        if i == 100:
            break


def func_iter():
    for x in range(10):
        yield x

n = func_iter()
print(next(n))
print(next(n))

text1 = 'There are a several items on the table'
def word_iter(text):
    start = -1
    while True:
        end = text.find(' ', start + 1)
        if end == -1:
            word = text[start + 1:]
        else:
            word = text[start + 1:end]
        start = end
        yield word

w1 = word_iter(text1)
print(next(w1))
print(next(w1))


# 2. Corutin

def greeting():
    to_greet = yield
    print(to_greet)

# hi1 = greeting()
# print(next(hi1))

hi1 = greeting()
# hi1.send(None)  # This step is defined by documentation! Or:
next(hi1)
# hi1.send('Hello!')
# print(next(hi1))    # Hello! -> Traceback StopIteration if send None-value to yield.

# 3. Multy yield func:

from time import time

def gen():
    yield 1
    yield 2
    yield 3

a = gen()
print(next(a))
print(next(a))
print(next(a))
# next() func run code just to current yield. Next iter will be run only second func call, and next yield or code
# after the first yield will run on the next iteration with next() func.


def gen_from():
    yield from 'Hello!'

g = gen_from()
print(next(g))  # H
print(next(g))  # e


