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



# 2. next out goal is push values in subgen from delegator function:

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



# 3. next step: exception handling:
@corutine_init
def subgen2():
    while True:
        try:
            message = yield
        except MyException:
            print('MyException raised, last value: ', message)
        else:
            print('current value: ', message)

@corutine_init
def delegator2(obj):
    while True:
        try:
            data = yield
            obj.send(data)
        except MyException as MyE:
            obj.throw(MyE)

gen2 = subgen2()
deleg_gen2 = delegator2(gen2)

# >>> deleg_gen2.send('Wtf Johnny?')
# current value:  Wtf Johnny?
# >>> deleg_gen2.throw(MyException)
# MyException raised, last value:  Wtf Johnny?



# 4. Too much strings of code and without handler, and withot return operator which need handler too. Solution for
# this porblem in use yield from construction for delegator.
def subgen3():
    while True:
        try:
            message = yield
        except MyException:
            print('MyException raised, last value: ', message)
        else:
            print('current value: ', message)

@corutine_init

def delegator3(obj):
    # while True:
    #     try:
    #         data = yield
    #         obj.send(data)
    #     except MyException as MyE:
    #         obj.throw(MyE)
    yield from obj  # PEP380 Spec. tells us, that "yield from" included initialization for generator, and we mustn't
    # need to use manual init with our decorator in subgen (corutine_init).

gen3 = subgen3()
deleg_gen3 = delegator3(gen3)

# >>> deleg_gen3.send('Aaaarghhghg!!!')
# current value:  Aaaarghhghg!!!
# >>> deleg_gen3.throw(MyException)
# MyException raised, last value:  Aaaarghhghg!!!
# >>>
