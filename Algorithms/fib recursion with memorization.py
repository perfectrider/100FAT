
# Fibonacci sequence with recursion and caching?

cache = []

def fib_ind(index):

    if index <= 1:
        result = index
    else:
        result = fib_ind(index - 1) + fib_ind(index - 2)
        cache.append(result)
    return result

print(fib_ind(15))

# This func is more slowly than first var.