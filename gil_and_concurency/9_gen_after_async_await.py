import time

queue = []


def counter():
    count = 1
    while True:
        print(count)
        count += 1
        # time.sleep(0.5)
        yield

def third_time_counter():
    count = 0
    while True:
        if count % 3 == 0:
            print('Kuku!')
        count += 1
        yield




def main():
    while True:
        el = queue.pop(0)
        next(el)
        queue.append(el)
        time.sleep(0.1)

g1 = counter()
queue.append(g1)
g2 = third_time_counter()
queue.append(g2)
main()

# 1
# Kuku!
# 2
# 3
# 4
# Kuku!