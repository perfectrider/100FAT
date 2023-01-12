
# Fibonacci sequence with recursion.

digs = [0, 1]

def fib_ind(index):

    digs.append(digs[-1] + digs[-2])
    if index >= 1 and index <= len(digs):
        return digs[index - 1]

    return fib_ind(index)

print(fib_ind(35))

# Possibility to implement recursion with a local variable?
