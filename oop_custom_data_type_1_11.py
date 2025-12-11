
"""

Built-in data types (15)

1 + 2.2     -> 3.2
1kg + 2.2lb -> 2kg

#################################################

Custom data types

class    -  Kg
data     -  n
methods  -  add()

#################################################

Step.1 (Draw Kg Type)

class Kg:
    def __init__(self, n):
        self.n = n
        
    def add(self, other):
        return self.n + other.n
        

x = Kg(1)
print(x)

#################################################

<__main__.Kg object at 0x104845340>

1 Kg

#################################################

Step.2 (repr) (1 Kg)

class Kg:
    def __init__(self, n):
        self.n = n

    def add(self, other):
        return self.n + other.n

    def __repr__(self):
        return f"{self.n} Kg"


x = Kg(1)
print(x)

#################################################

x = Kg(1)
y = Kg(2)
z = x + y

TypeError: unsupported operand type(s) for +: 'Kg' and 'Kg'

#################################################

Step.3 ( + ) (__add__) 

class Kg:
    def __init__(self, n):
        self.n = n

    def __add__(self, other):
        return self.n + other.n

    def __repr__(self):
        return f"{self.n} Kg"


x = Kg(1)
y = Kg(2)
z = x + y
print(z)

#################################################

3  
3 Kg

#################################################

Step.4 ( result of addition => 3 Kg ) 
- Kg(self.n + other.n)


class Kg:
    def __init__(self, n):
        self.n = n

    def __add__(self, other):
        return Kg(self.n + other.n)

    def __repr__(self):
        return f"{self.n} Kg"


x = Kg(1)
y = Kg(2)
z = x + y # Kg(3) 
print(z)

#################################################

Step.5 ( Lb )


class Kg:
    def __init__(self, n):
        self.n = n

    def __add__(self, other):
        return Kg(self.n + other.n)

    def __repr__(self):
        return f"{self.n} Kg"


class Lb:
    def __init__(self, n):
        self.n = n

    def __add__(self, other):
        return Lb(self.n + other.n)

    def __repr__(self):
        return f"{self.n} lb"


x = Kg(1)
y = Lb(2.2)
print(x + y)

#################################################

1 Kg + 2.2 lb => 3.2 Kg
1 Kg + 2.2 lb => 2 Kg

#################################################

Step.6 ( 2 Kg, 4.4 lb )

x + y => 1 Kg + 2.2 lb => 2 Kg

def __add__(self, other):
    if type(other) is Kg:
        return Kg(self.n + other.n)
    if type(other) is Lb:
        return Kg(self.n + other.n / 2.2)
        

y + x => 2.2 lb + 1 Kg = 4.4 lb

def __add__(self, other):
    if type(other) is Lb:
         return Lb(self.n + other.n)
    elif type(other) is Kg:
        return Lb(self.n + other.n * 2.2)

#################################################


class Kg:
    def __init__(self, n):
        self.n = n

    def __add__(self, other):
        if type(other) is Kg:
            return Kg(self.n + other.n)
        elif type(other) is Lb:
            return Kg(self.n + other.n / 2.2)

    def __repr__(self):
        return f"{self.n} Kg"


class Lb:
    def __init__(self, n):
        self.n = n

    def __add__(self, other):
        if type(other) is Lb:
            return Lb(self.n + other.n)
        elif type(other) is Kg:
            return Lb(self.n + other.n * 2.2)

    def __repr__(self):
        return f"{self.n} lb"


x = Kg(1)
y = Lb(2.2)
print(x + y)
print(y + x)

#################################################

Step.7 ( - ) ( __sub__ )

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

    def __repr__(self):
        return f"{self.n} Kg"


class Lb:
    def __init__(self, n):
        self.n = n

    def __add__(self, other):
        if type(other) is Lb:
            return Lb(self.n + other.n)
        elif type(other) is Kg:
            return Lb(self.n + other.n * 2.2)

    def __sub__(self, other):
        if type(other) is Lb:
            return Lb(self.n - other.n)
        elif type(other) is Kg:
            return Lb(self.n - other.n * 2.2)

    def __repr__(self):
        return f"{self.n} lb"


x = Kg(1)
y = Lb(2.2)

print(x - y)
print(y - x)

#################################################

Step.8 (literal)

print(1 .kg + 2.2 .lb) # 2.0 Kg
print(2.2 .lb + 1 .kg) # 4.4 lb

#################################################

from custom_literals import literal

@literal(int, float, name="kg")
def f1(n):
    return Kg(n)


@literal(int, float, name="lb")
def f2(n):
    return Lb(n)

#################################################

from custom_literals import literal


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

    def __repr__(self):
        return f"{self.n} Kg"


class Lb:
    def __init__(self, n):
        self.n = n

    def __add__(self, other):
        if type(other) is Lb:
            return Lb(self.n + other.n)
        elif type(other) is Kg:
            return Lb(self.n + other.n * 2.2)

    def __sub__(self, other):
        if type(other) is Lb:
            return Lb(self.n - other.n)
        elif type(other) is Kg:
            return Lb(self.n - other.n * 2.2)

    def __repr__(self):
        return f"{self.n} lb"


@literal(int, float, name="kg")
def f1(n):
    return Kg(n)


@literal(int, float, name="lb")
def f2(n):
    return Lb(n)


print(1 .kg + 2.2 .lb) # 2.0 Kg
print(2.2 .lb + 1 .kg) # 4.4 lb

#################################################

print(1 == 1) # True
print(1 .kg == 1 .kg) # False
print(1 .kg == 2.2 .lb) # False

#################################################

Step.9 (equality operator) (==) (__eq__) 

def __eq__(self, other):
    return self.n == other.n

#################################################

Kg and Kg, Lb and Lb

print(1 .kg == 1 .kg) # True
print(1 .kg == 2.2 .lb) # False     <-----  Kg and Lb

#################################################

Step.10 (Kg and Lb) (Lb and Kg)

Kg and Lb

def __eq__(self, other):
    if type(other) is Kg:
        return self.n == other.n
    elif type(other) is Lb:
        return self.n == other.n / 2.2

Lb and Kg

def __eq__(self, other):
    if type(other) is Lb:
        return self.n == other.n
    elif type(other) is Kg:
        return self.n == other.n * 2.2
        
        
#################################################

print(1 .kg == 2.2 .lb) # True 
print(2.2 .lb == 1 .kg) # True

#################################################

from custom_literals import literal


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


class Lb:
    def __init__(self, n):
        self.n = n

    def __add__(self, other):
        if type(other) is Lb:
            return Lb(self.n + other.n)
        elif type(other) is Kg:
            return Lb(self.n + other.n * 2.2)

    def __sub__(self, other):
        if type(other) is Lb:
            return Lb(self.n - other.n)
        elif type(other) is Kg:
            return Lb(self.n - other.n * 2.2)

    def __eq__(self, other):
        if type(other) is Lb:
            return self.n == other.n
        elif type(other) is Kg:
            return self.n == other.n * 2.2

    def __repr__(self):
        return f"{self.n} lb"


@literal(int, float, name="kg")
def f1(n):
    return Kg(n)


@literal(int, float, name="lb")
def f2(n):
    return Lb(n)


print(1 .kg == 2.2 .lb) # True 
print(2.2 .lb == 1 .kg) # True

#################################################

Note   --->   1 Kg = 2.20462 lb

#################################################

Step.11 ( is ) (hummar)

1000000 houses
1000000 obj
1 houses
1 obj

- same value, same memory address
- same value, same obj 
- if same value,
  - do not create new obj 
  - reuse the old one
  
- cache
  - dict = {} -> {1: 1kg, 100: 100kg}
  - if 1 in dict:
    - dict[1] # 1kg obj
  - if not in dict:
    - create new (super().__new__(cls))

#################################################

kilograms = {} 


def __new__(cls, n): 
    if n in Kg.kilograms:
        return Kg.kilograms[n]

    else:
        new = super().__new__(cls) 
        new.n = n                  
        Kg.kilograms[n] = new
        return new

#################################################


from custom_literals import literal


class Kg:

    kilograms = {} # {1: 1kg(001)}

    def __new__(cls, n): # 1 1
        if n in Kg.kilograms:
            return Kg.kilograms[n]

        else:
            new = super().__new__(cls)  # new kg obj from parent  (001)
            new.n = n                   # 1 kg
            Kg.kilograms[n] = new
            return new

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


@literal(int, float, name="Kg")
def f1(n):
    return Kg(n)


@literal(int, float, name="lb")
def f2(n):
    return Lb(n)
    

x = Kg(1)
y = Kg(1)

print(id(x))
print(id(y))
    
##################################################################################################

"""


