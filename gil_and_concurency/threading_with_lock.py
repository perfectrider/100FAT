import threading
from time import sleep


lock = threading.Lock()
count = 0

def first_func(num):
    global count
    lock.acquire()

    while count <= 5:
        print(f'first func value = {count}')
        count += 1
        sleep(num)
    lock.release()

def second_func(num):
    global count
    lock.acquire()

    while count <= 5:
        print(f'second func value = {count}')
        count += 1
        sleep(num)
    lock.release()



th1 = threading.Thread(target=first_func, args=(0.2,))
th2 = threading.Thread(target=second_func,  args=(0.2,))

th1.start()
th2.start()

th1.join()
th2.join()