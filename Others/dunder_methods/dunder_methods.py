# 1. Comparing methods

class Word(str):
    '''Class for сomparing strings by length'''

    def __new__(cls, word):
        # We must use __new__, because str-type is not mutable and we must initialize it early
        return str.__new__(cls, word)

    def __gt__(self, other):
        return len(self) > len(other)

    def __lt__(self, other):
        return len(self) < len(other)

    def __ge__(self, other):
        return len(self) >= len(other)

    def __le__(self, other):
        return len(self) <= len(other)


w1 = Word('Hi friend!')
w2 = Word('Hello!')
# w1.__new__('Hello friend')
# w2.__new__('Hi!')

print(w1 > w2, w2 < w1)


# 2. User list sequence.
class FunctionalList:
    '''tail, init, last, drop, take additionals for list type'''

    def __init__(self, values=None):
        if values is None:
            self.values = []
        else:
            self.values = values

    def __len__(self):
        return len(self.values)

    def __getitem__(self, key):
        # except will raise if type or value of key invalid
        return self.values[key]

    def __setitem__(self, key, value):
        self.values[key] = value

    def __delitem__(self, key):
        del self.values[key]

    def __iter__(self):
        return iter(self.values)

    def __reversed__(self):
        return FunctionalList(reversed(self.values))

    def append(self, value):
        self.values.append(value)

    def head(self):
        # get first element
        return self.values[0]

    def tail(self):
        # get all elements after first
        return self.values[1:]

    def init(self):
        # get all elements without last
        return self.values[:-1]

    def last(self):
        # get last element
        return self.values[-1]

    def drop(self, n):
        # all elements without first n
        return self.values[n:]

    def take(self, n):
        # first n elements
        return self.values[:n]

user_list = FunctionalList([1, 2, 3, 4, 5])

print(user_list.values) # [1, 2, 3, 4, 5]

u1 = user_list.__iter__()
print(next(u1)) # 1
print(next(u1)) # 2

print(user_list.drop(2))    # [3, 4, 5]
# ...etc


# 3. __call__ method.
class Point:
    '''Point coordinates'''
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __call__(self, x, y):
        self.x = x
        self.y = y

p1 = Point(12, 3)

p1(10, 5)
print(p1.__dict__)  # {'x': 10, 'y': 5}


# 4. Context manager methods
class Closer:
    '''Context manager for object close in auto mode'''

    def __init__(self, obj):
        self.obj = obj

    def __enter__(self):
        return self.obj # attaching to the active object of the with-block

    def __exit__(self, exception_type, exception_val, trace):
        try:
           self.obj.close()
        except AttributeError: # if object have not the close method
           print('Not closable.')
           return True # exception caught


# 5. Descriptor for conversion meter to centimeter
class Meter(object):
    '''Meter descriptor'''
    def __init__(self, value=0.0):
        self.value = float(value)

    def __get__(self, instance, owner):
        return self.value

    def __set__(self, instance, value):
        self.value = float(value)

class Centimeter(object):
    '''Centimeter descriptor'''
    def __get__(self, instance, owner):
        return instance.meter * 100

    def __set__(self, instance, value):
        instance.meter = float(value) / 100

class Measure(object):
    '''Measurement value for meter and centimeter'''
    meter = Meter()
    centimeter = Centimeter()
# ?
