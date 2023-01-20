
# While loop to find value of Fibonacci sequence.

find_index = 15
digs = [0, 1]

while find_index != len(digs) - 1:
    digs.append(digs[-1] + digs[-2])

print(digs[-1]) # 610