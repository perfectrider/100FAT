def memorize(func):
    memory = {}

    def wrapper(*args):
        if args in memory:
            return f'from memory: {memory[args]}'
        else:
            result = func(*args)
            memory[args] = result
            return result

    return wrapper

@memorize
def multipli(a, b):
    return a * b

print(multipli(2, 5))   # 10
print(multipli(3, 5))   # 15
print(multipli(4, 5))   # 20
print(multipli(2, 5))   # from memory: 10

