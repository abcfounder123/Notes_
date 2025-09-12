"""

Major OOP Concepts

1. polymorphism  ( many forms ) 

2. inheritance ( code reuse ) 
   - parent class ?  
   - common data ?
   
- parent class ?

Car, Motor Car, Electric Car
    
                    Car
                  /     \
            Motor Car   Electric Car
            
    
Adding new feature -> Vehicle 
    
                   Vehicle
                     |
                    Car
                  /     \
            Motor Car   Electric Car
                   
                   
     
3. encapsulation ( data hiding )

4. abstraction

#################################################

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

# y = Car()

################################################

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

################################################

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
a.add(1) # lifo

###########

001 --> fun obj
add --> 001

002 --> fun obj
add --> 002

###########

from multipledispatch import dispatch

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
a.add(1) # lifo

###########

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
a.add(1, 3) # lifo

###########

# python style
class X:
    def __init__(self, value):
        self.value = value

    def add(self, *other):
        t = self.value
        for n in other:
            t += n
        print(t)

a = X(1)
a.add(1, 2, 3, 1, 1, 1, 1, 1, 1)

#################################################

# Method Overloading by using dispatch decorator
# dispatch = ‌သီးသန့်‌ေနရာ
from multipledispatch import dispatch

@dispatch(int, int)
def product(first, second):
    result = first * second
    print(result, "   <--- int 2")

@dispatch(int, int, int)
def product(first, second, third):
    result = first * second * third
    print(result, "   <---  int 3 ")

@dispatch(float, float, float)
def product(first, second, third):
    result = first * second * third
    print(round(result), "   <---  float 3")

def product(*x):
    t = 0
    for i in x:
        t += i
    print(t)

product(1, 2)
product(1, 2, 3)
product(1.1, 2.1, 3.0)
#product(1, 2, 3, 4, 5, 0.1)

#################################################

2. Method overriding ( LIFO ) ( FIFO )

override လွှမ်းမိုး

---> sub class method "overrides" the method provided in the base class.

         A   i = 1
         |
         X   i = 2
         |
         Y   i = 3
         
        obj  i = 4
        
MRO obj.i -> obj, Y, X, A       4
MRO Y.i   -> Y, X, A            3
MRO X.i   -> X, A               2
MRO A.i   -> A                  1

class B:
    def f(self):
        print("b")

class S(B):
    def f(self):
        print("s")

s = S()
s.f()

################################################

Design Patterns & Python

What is a Design Pattern?
Design Patterns are concrete solutions for reoccurring problems.
They satisfy the design principles and can be used to understand and illustrate them.
They provide a NAME to communicate effectively with other programmers.

#################################################

1. Iterator Pattern
The essence of the Iterator Factory method Pattern is to
"Provide a way to access the elements of an aggregate object sequentially
without exposing its underlying representation."

sequentially access

aggregate ( စုပေါင်း )
exposing ( မြင်သာအောင်ပြ )
representation ( ကိုယ်စားပြု )

#################################################

2. Decorator Pattern
( မူလအရာကို မထိခိုက်ဘဲ  မွမ်းမံနိုင်စွမ်း )
The decorator pattern is a design pattern that
allows behavior to be added to an existing object dynamically.
behaviour ( အပြုအမူ လုပ်ဆောင်ချက် )

#################################################

5000 ( gps, radar, ir  )
300  ( radar )
30   ( ir )

3. Strategy Pattern
The strategy pattern (also known as the policy pattern) is
a particular software design pattern,
whereby algorithms behavior can be selected at runtime.

#################################################

4. Adapter Pattern
The adapter pattern is a design pattern that
translates one interface for a class into a compatible interface

#################################################

# Iterator
class My_list:
    def __init__(self, *x):
        self.p = 0
        self.x = x    # ("apple", "banana", "orange")

    def __repr__(self):
        s = "["
        for i in self.x:
            s += i
            s += ", "        # "[apple, banana, ...         
        s += "]"
        return s

    def __iter__(self):
        return self

    def __next__(self):
        try:
            v = self.x[self.p]
        except IndexError:
            raise StopIteration()
        self.p += 1
        return v


l = My_list("apple", "banana", "orange", "mangoes")

for i in l:
    print(i)
    
##################################################################################################     


 

"""


