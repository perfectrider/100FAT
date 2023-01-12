
# Fibonacci sequence with recursion.

digs2 = [0, 1]

def fib_ind(index):

    digs2.append(digs2[-1] + digs2[-2])
    length = len(digs2)
    if index >= 1 and index <= length:

        return digs2[index - 1]

    return fib_ind(index)

print(fib_ind(1))

# Possibility to implement recursion with a local variable?
