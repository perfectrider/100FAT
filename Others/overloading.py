
class Smt:

    def __init__(self, a, b):
        self.a = a
        self.b = b


    # def sum(self, a=None, b=None, c=None):
    #     if a != None and b != None and c != None:
    #         sum = a + b + c
    #     elif a != None and b != None:
    #         sum = a + b
    #     else:
    #         sum = a
    #     return sum

    def sum(self, *args):
        return sum(args)


h1 = Smt(3, 12)
print(h1.sum(1))        # 1
print(h1.sum(1, 3))     # 4
print(h1.sum(1, 3, 4))  # 8

# https://docs.python.org/3/library/functools.html#functools.singledispatch
