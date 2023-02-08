# 1. classmethod decorator

class User():
    age_validate = 18

    @classmethod
    def age_validator(cls, value):
        return value >= cls.age_validate

    def __init__(self, name, age, email):
        self.name = name
        if self.age_validator(age):
            self.age = age
        self.email = email

    def get_user_info(self):
        return self.name, self.age, self.email



# 2. class decorator:
class SquareRect:
    def __call__(self, a, b):
        return a * b


sq1 = SquareRect()
print(sq1(2, 6))



# 3. class decorator 2:

class MyDecorator:
    def __init__(self, func):
        print('init method')
        self.func = func

    def __call__(self, x, y):
        print('before wrapper')
        result = self.func(x, y)
        print('after wrapper')
        return result
@MyDecorator
def func(a, b):
    return 'Hello!', a, b

print(*func(3, 12))
# 12
# init method
# before wrapper
# after wrapper
# Hello! 3 12



# 3. class decorator 3 - with args:
class MyDecorator2:
    def __init__(self, name='Goodbye!'):
        print('init method:', name)
        self.name = name

    def __call__(self, func, *args, **kwargs):
        def wrapper(*args, **kwargs):
            print('before wrapper')
            func(*args, **kwargs)
            print('after wrapper')
        return wrapper

@MyDecorator2('Hi')
def func2(a, b):
    print('Function: ', a, b)

func2(10, 25)
# init method: Hi
# before wrapper
# 10 25
# after wrapper

@MyDecorator2() # Если аргумент по умолчанию, вызывать декоратор с ()!
def func3(a, b, c, d, str):
    print(a, b, c, d, str)

func3(5, 6, 7, 8, 'Hi')
