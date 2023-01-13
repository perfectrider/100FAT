
find_index = 3
digs = [0, 1]

while find_index != len(digs):
    digs.append(digs[-1] + digs[-2])

print(digs[-1])

