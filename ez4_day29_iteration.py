
"""

Iteration (for)

x = ["apple", "banana", "orange"]

for i in x:
    print(i)

print(x)

#################################################

1. Iterable objects(str, list, ... )
   - iter
   
2. Iterator
   - next

#################################################

obj + obj      =>   __add__
for i in obj:  =>   __iter__
Access order   =>   __next__

#################################################

representation string     =>   __repr__       return str obj
Iterable objects          =>   __iter__       return iterator obj
Iterator                  =>   __next__       return as you like

#################################################

1. Iterable objects


class X:
    def __iter__(self):
        return iterator_obj
        

#################################################

2. Iterator


class X:
    def __next__(self):
        return "abc"


#################################################

x = ["apple", "banana", "orange"]

for i in x:
    print(i)

print(x)

#################################################

Iteration process

for
>> x.iter()      => new obj("apple", "banana", "orange")

in        
>> next(new obj) => "apple"    => new obj("banana", "orange")
>> next(new obj) => "banana"   => new obj("orange")
>> next(new obj) => "orange"   => new obj()
>> next(new obj) =>  Error     => stop iteration

#################################################

class     => X 
attribute => data, n = 0

#################################################

Iteration process

for
>> y.iter()      => new obj("apple", "banana", "orange")

in        
>> next(new obj) => 1         
>> next(new obj) => 2
>> next(new obj) => 3
>> next(new obj) => ....


class X:
    def __init__(self, *x):
        self.data = x
        self.n = 0

    def __next__(self):
        self.n += 1
        return self.n


class Y:
    def __iter__(self):
        return X()


y = Y()

for i in y:
    print(i)

#################################################

x.data = ["apple", "banana", "orange"]
x.data[0] => "apple"
x.data[1] => "banana"
x.data[2] => "orange"
x.data[3] => IndexError

#################################################

Iteration process

for
>> y.iter()      => X(["apple", "banana", "orange"]) => obj.data = ["apple", "banana", "orange"]

in        
>> next(new obj) => "apple"  
>> next(new obj) => "banana"   
>> next(new obj) => "orange"   
>> next(new obj) =>  IndexError  


class X:
    def __init__(self, x):
        self.data = x
        self.n = 0

    def __next__(self):
        ans = self.data[self.n]
        self.n += 1
        return ans


class Y:
    def __init__(self):
        self.d1 = ["apple", "banana", "orange"]
        self.d2 = [1, 2, 3, 4]

    def __iter__(self):
        return X(self.d1)


y = Y()

for i in y:
    print(i)

#################################################

>> next(new obj) =>   -1 "orange"
>> next(new obj) =>   -2 "banana"   
>> next(new obj) =>   -3 "apple"  
>> next(new obj) =>   -4 IndexError 


class X:
    def __init__(self, x):
        self.data = x
        self.n = -1

    def __next__(self):
        ans = self.data[self.n]
        self.n += -1
        return ans


class Y:
    def __init__(self):
        self.d1 = ["apple", "banana", "orange"]
        self.d2 = [1, 2, 3, 4]

    def __iter__(self):
        return X(self.d1)


y = Y()

for i in y:
    print(i)
    
#################################################
       
X() = Left to right iterator obj         next
Y() = Right to left iterator obj         next
Z() = Iterable objects                   iter    => return iterator obj
    
#################################################

class X:
    def __init__(self, x):
        self.data = x
        self.n = 0

    def __next__(self):
        ans = self.data[self.n]
        self.n += 1
        return ans


class Y:
    def __init__(self, x):
        self.data = x
        self.n = -1

    def __next__(self):
        ans = self.data[self.n]
        self.n += -1
        return ans


class Z:
    def __init__(self):
        self.d1 = ["apple", "banana", "orange"]
        self.d2 = [1, 2, 3, 4]

    def __iter__(self):
        return X(self.d1)


y = Y()

for i in y:
    print(i)
    
#################################################

How to stop Iteration?


class X:
    def __init__(self, x):
        self.data = x
        self.n = 0

    def __next__(self):
        try:
            ans = self.data[self.n]
            self.n += 1
            return ans
        except IndexError:
            raise StopIteration


class Y:
    def __init__(self, x):
        self.data = x
        self.n = -1

    def __next__(self):
        ans = self.data[self.n]
        self.n += -1
        return ans


class Z:
    def __init__(self):
        self.d1 = ["apple", "banana", "orange"]
        self.d2 = [1, 2, 3, 4]

    def __iter__(self):
        return X(self.d1)


y = Z()

for i in y:
    print(i)


#################################################

Changing iteration Style of list


                       list       iter       l to r
                       
                        |
                        
                     My_list      iter
                     
#################################################

  
class Y:
    def __init__(self, x):
        self.data = x
        self.n = -1

    def __next__(self):
        try:
            ans = self.data[self.n]
            self.n += -1
            return ans
        except IndexError:
            raise StopIteration


class My_list(list):
    def __iter__(self):
        return Y(self)


x = list(["apple", "banana", "orange"])

for i in x:
    print(i)

print("-" * 42)

x = My_list(["apple", "banana", "orange"])

for i in x:
    print(i)  
    
#################################################

Creating Iterable objects    
    

class Z:
    def __init__(self, x):
        self.data = x / 10
        self.n = 0

    def __next__(self):
        self.n += 1
        if self.n == 11:
            raise StopIteration
        return self.data


class Dollar:
    x = {}

    def __new__(cls, n):
        if n in Dollar.x.keys():
            return Dollar.x[n]                # 0x100d52120
        else:
            new = super().__new__(cls)        # 0x100d52120
            new.n = n                         # 0x100d52120 <- n=1
            Dollar.x[n] = new
            return new

    def __add__(self, other):
        if type(other) == Dollar:
            return Dollar(self.n + other.n)
        if type(other) == Kyat:
            return Dollar(self.n + other.n/5000)

    def __sub__(self, other):
        if type(other) == Dollar:
            return Dollar(self.n - other.n)
        if type(other) == Kyat:
            return Dollar(self.n - other.n/5000)

    def __eq__(self, other):
        if type(other) == Dollar:
            return self.n == other.n
        if type(other) == Kyat:
            return self.n == other.n/5000

    def __repr__(self):
        return f"{self.n} dollar"

    def __iter__(self):
        return Z(self.n)


x = Dollar(90)
for i in x:
    print(i)

##################################################################################################

"""

