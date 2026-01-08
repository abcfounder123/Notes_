
"""

Iteration  (for)
1. iterable object (iter method)
2. iterator        ( next )

for ->  iter()  ->  iterator -> i = next value of iterator

TypeError: 'X' object is not iterable
TypeError: iter() returned non-iterator of type 'str'

#################################################

Iterable object

class X:

    def __iter__(self):
        return iterator

#################################################

Iterator (next)

class X:

    def __next__(self):
        return "abc"

    def __iter__(self):
        return self
        

#################################################

data = (1, 2, "apple")
range -> -3, -2, -1, 0, 1, 2

data[3]
IndexError: tuple index out of range

StopIteration()

#################################################


class X:
    def __init__(self, *d):
        self.data = d  # (1, 2, "apple")
        self.n = 0

    def __next__(self):
        try:
            value = self.data[self.n]  # data[2] -> apple
            self.n += 1  # n = 3
            return value
        except IndexError:
            raise StopIteration()

    def __iter__(self):
        return self


x = X(1, 2, "apple")


for i in x:
    print(i)
        
##################################################################################################


class X:
    def __init__(self, d):
        self.data = d  # "10 Kg"
        self.n = 0

    def __next__(self):
        try:
            value = self.data[self.n]
            self.n += 1
            return value
        except IndexError:
            raise StopIteration()

    def __iter__(self):
        return self


class R:
    def __init__(self, d):
        self.data = d
        self.n = -1

    def __next__(self):
        try:
            value = self.data[self.n]
            self.n -= 1
            return value
        except IndexError:
            raise StopIteration()

    def __iter__(self):
        return self


class L:
    def __init__(self, *d):
        self.data1 = d
        self.data2 = [1, 2, 3, 4]

    def __iter__(self):
        return X(self.data1)


class Kg:
    def __init__(self, n):
        self.n = n

    def __add__(self, other):
        if type(other) is Kg:
            return Kg(self.n + other.n)
        elif type(other) is Lb:
            return Kg(self.n + other.n / 2.2)

    def __sub__(self, other):
        if type(other) is Kg:
            return Kg(self.n - other.n)
        elif type(other) is Lb:
            return Kg(self.n - other.n / 2.2)

    def __eq__(self, other):
        if type(other) is Kg:
            return self.n == other.n
        elif type(other) is Lb:
            return self.n == other.n / 2.2

    def __repr__(self):
        return f"{self.n} Kg"

    def __iter__(self):
        return X(repr(self))


x = L("apple", "banana", "orange")

for i in x:
    print(i)

w = Kg(10)

for i in w: # X("10 Kg")  , x obj , i = next(x)
    print(i)

##################################################################################################

"""
