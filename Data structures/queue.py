
#    1. Queue

class FIFO:
    '''First-In-First_out'''

    def __init__(self):
        self.queue = []

    def push_front(self, value):
        self.queue.append(value)

    def get(self):
        return self.queue.pop(0)

fifo = FIFO()
fifo.push_front(1)
fifo.push_front(2)
print(fifo.get())   # 1
print(fifo.get())   # 2

# Чтобы преобразовать обычную очередь в стек, необходимо геттером выводить не первый элемент, а последний:
class LIFO:
    '''Last-In-First-Out'''

    def __init__(self):
        self.queue = []

    def push_front(self, value):
        self.queue.append(value)

    def get(self):
        return self.queue.pop(-1)

lifo = LIFO()
lifo.push_front(1)
lifo.push_front(2)
print(lifo.get())   # 2
print(lifo.get())   # 1