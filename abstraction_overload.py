"""

4. Abstraction

Abstract classes are the classes which contains one or more abstract method;

and abstract methods are the methods which does not contain any implemetation,

but the child-class need to implement these methods otherwise error will
be reported.

In this way, we can force the child-class to implement certain methods in it.

#################################################

# abstraction example.1
from abc import ABCMeta, abstractmethod


class Car(metaclass=ABCMeta):
    def __init__(self, b="ABS system brake"):
        self.brake_system = b

    def brake(self):
        print(f"Brake with {self.brake_system}")

    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def stop(self):
        pass


class City_car(Car):
    def __init__(self):
        super().__init__()
        self.engine = "city engine"
        self.tire = "city tire"

    def start(self):
        print(f"{self.engine} start.")

    def stop(self):
        print(f"{self.engine} stop.")


x = City_car()
x.start()
x.stop()
x.brake()

#################################################

from abc import ABCMeta, abstractmethod


class Weight(metaclass=ABCMeta):
    @abstractmethod
    def __add__(self, other):
        pass

    @abstractmethod
    def __sub__(self, other):
        pass


class Kg(Weight):
    def __add__(self, other):
        pass

    def __sub__(self, other):
        pass


class Lb(Weight):
    def __add__(self, other):
        pass

    
x = Kg()

#################################################

# abstraction example.2
# crd freecodecamp

from abc import ABC, abstractmethod

class Book(ABC):
    def __init__(self, title, quantity, author, price):
        self.title = title
        self.quantity = quantity
        self.author = author
        self.__price = price
        self.__discount = None

    def set_discount(self, discount):
        self.__discount = discount

    def get_price(self):
        if self.__discount:
            return self.__price * (1 - self.__discount)
        return self.__price

    @abstractmethod
    def __repr__(self):
        return f"Book: {self.title}\nQuantity: {self.quantity}\nAuthor: {self.author}\nPrice: {self.get_price()}\n"


class Novel(Book):
    def __init__(self, title, quantity, author, price, pages):
        super().__init__(title, quantity, author, price)
        self.pages = pages

    def __repr__(self):
        return super().__repr__() + f"Pages: {self.pages}\n"


class Academic(Book):
    def __init__(self, title, quantity, author, price, branch):
        super().__init__(title, quantity, author, price)
        self.branch = branch

    def __repr__(self):
        return super().__repr__() + f"Branch: {self.branch}\n"


novel1 = Novel('Two States', 20, 'Chetan Bhagat', 300, 200)
novel1.set_discount(0.20)

academic1 = Academic('Python Foundations', 12, 'PSF', 300, 'IT')

print(novel1)
print(academic1)

# del @abstractmethod
#b = Book("book1", 10, "abc", 10)
#print(b)


#################################################

Method Overloading:

Two or more methods have the same name but different numbers of parameters or
different types of parameters, or both.

These methods are called overloaded methods and this is called method overloading.

Like other languages (for example, method overloading in C++) do,
python does not support method overloading by default.

But there are different ways to achieve method overloading in Python.

#################################################

# Python doesn't support Method Overloading by default.

class X:
    def __init__(self, value):
        self.value = value

    def add(self, other):
        print(self.value + other)

    def add(self, other1, other2):# li
        print(self.value + other1 + other2)


a = X(1)
a.add(1, 2) # lifo

#################################################

001 --> fun obj
add --> 001

002 --> fun obj
add --> 002

#################################################

from multipledispatch import dispatch

# different numbers of parameters
# method overloading
class X:
    def __init__(self, value):
        self.value = value

    @dispatch(int)
    def add(self, other):
        print(self.value + other)

    @dispatch(int, int)
    def add(self, other1, other2): # li
        print(self.value + other1 + other2)

a = X(1)
a.add(1, 2) # lifo

#################################################

# python style
class X:
    def __init__(self, value):
        self.value = value

    def add(self, other1, other2=None):
        if not other2:
            print(self.value + other1)
        else:
            print(self.value + other1 + other2)

a = X(1)
a.add(1) # lifo

#################################################

# python style
class X:
    def __init__(self, value):
        self.value = value

    def add(self, *other): # (1, 2, 3, 1, 1, 1, 1, 1, 1)
        t = self.value
        for n in other:
            t += n
        print(t)

a = X(1)
a.add(1, 2, 4, 5)

########################
"""

