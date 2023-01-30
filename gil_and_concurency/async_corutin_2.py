class MyException(Exception):
    pass


def corutine_init(func):
    def wrapper(*args, **kwargs):
        g = func(*args, **kwargs)
        g.send(None)
        return g

    return wrapper


# def subgen():
#     for i in 'Hello':
#         yield i
#
#
# def delegator(obj):
#     for i in obj:
#         yield i
#
#
# gen = subgen()
# deleg_gen = delegator(gen)
#
# print(next(deleg_gen))  # H
# print(next(deleg_gen))  # e
# # ...returned subgen values



# next out goal is push values in subgen from delegator function:

@corutine_init
def subgen():
    while True:
        try:
            message = yield
        except StopIteration:
            print('StopIteration raised, last value: ', message)
        else:
            print('current value: ', message)

@corutine_init
def delegator(obj):
    while True:
        try:
            data = yield
            obj.send(data)
        except StopIteration:
            print('StopItaration raised!')

gen = subgen()
deleg_gen = delegator(gen)

# >>> deleg_gen.send('Hello!')
# current value:  Hello!
# >>> deleg_gen.send('Hi')
# current value:  Hi
# >>>


# next step: exception handling


