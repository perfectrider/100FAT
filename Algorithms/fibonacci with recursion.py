
# Fibonacci sequence with recursion.

def fib_ind(index):

    if index < 2:
        return index
    else:
        return fib_ind(index - 1) + fib_ind(index - 2)

print(fib_ind(15))

# Possibility to implement recursion with a local variable?
