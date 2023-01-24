a = (x for x in range(10))
print(a)    # <generator object <genexpr> at 0x7f0b4cff6880>

print(next(a))  # 0
print(next(a))  # 1


a = [1, 2, 3]
a = iter(a)
print(next(a))  # 1
print(next(a))  # 2
print(next(a))
# print(next(a))  # !StopIteration


# a = list(range(10000000000000000000000)) -> memoryError
a = (range(1000000000000000000000))
for i in a:
    if i > 89 and i <= 100:
        print(i)    # 90, 91 ... 100
        if i == 100:
            break


def func_iter():
    for x in range(10):
        yield x

n = func_iter()
print(next(n))
print(next(n))

text1 = 'There are a several items on the table'
def word_iter(text):
    start = -1
    while True:
        end = text.find(' ', start + 1)
        if end == -1:
            word = text[start + 1:]
        else:
            word = text[start + 1:end]
        start = end
        yield word

w1 = word_iter(text1)
print(next(w1))
print(next(w1))






