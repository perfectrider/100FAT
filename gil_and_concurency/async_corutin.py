# 1. Corutins, asynch(), await()
from inspect import getgeneratorstate


# def subgen():
#     message = yield
#     print('Subgen received: ', message)
#
# a = subgen()
# print(getgeneratorstate(a)) # GEN_CREATED
# a.send(None)
# print(getgeneratorstate(a)) # GEN_SUSPENDED (Приостановлен)
# a.send('Hello-1')   # Subgen received:  Hello-1, -> StopIteration


def subgen():
    x = 'Ready to accept message'
    message = yield x
    print('Subgen received: ', message)

a = subgen()
a.send(None)  # if print - "Ready to accept message"
# a.send('Hello-2')   # Subgen received:  Hello-2, -> StopIteration


# 2.

class MyException(Exception):
    pass

def corutine_init(func):
    def wrapper(*args, **kwargs):
        g = func(*args, **kwargs)
        g.send(None)
        return g
    return wrapper

@corutine_init
def average():
    count = 0
    sum = 0
    average = None

    while True:
        try:
            x = yield average
        except StopIteration:
            print('Done')
        except MyException:
            print('MyException raised!')
        else:
            count += 1
            sum += x
            average = round(sum / count, 2)

# obj.send(3)
# 3.0
# obj.send(5)
# 4.0
#...
# obj.throw(StopIteration)
# 'Done'
# 4.0
