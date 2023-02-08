from Others.decorators.decorator1 import testtime
import time

def time_for_class_methods(cls):
    class Class:
        def __init__(self, *args, **kwargs):
            self._obj = cls(*args, **kwargs)

        def __getattribute__(self, s):
            # Is here attribute "s"?

            try:
                x = super().__getattribute__(s)
            except AttributeError:
                pass
            else:
                return x

            mthd = self._obj.__getattribute__(s)

            if isinstance(mthd, type(self.__init__)):

                #
                return testtime(mthd)
            else:
                return mthd

    return Class


@time_for_class_methods
class Stopper:

    def one_sec(self):
        time.sleep(1)
        return

    def two_sec(self):
        time.sleep(2)
        return

first = Stopper()

first.one_sec()
first.two_sec()

# test time one_sec start...
# function time is:  1.0
# test time two_sec start...
# function time is:  2.0

#