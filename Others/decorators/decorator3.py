def error_handler(func):
    def wrapper(*args):
        result = -1
        try:
            result = func(*args)
        except:
            print(f'error of {func.__name__} function!')
        return result

    return wrapper

@error_handler
def division(a, b):
    return a / b


print(division(6, 2))   # 3.0
print(division(6, 0))   # error of division function!
                        # -1
