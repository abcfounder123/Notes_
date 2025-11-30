
"""

Day.15 (function)

Procedural programming
1. sequence  (top, left, p)
2. selection (if, elif, else)
3. looping   (for, while)
4. function (Procedure)

################################################

Parameters
1. Normal parameter, standard parameter               (x, y, a)
2. Default parameter                                  (x, y, a=0)
3. Positional only parameter(/)                       (x, y, /) (form.1)
4. Keyword only parameter(*)                          (*, x, y) (form.2)
5. Variable length Positional only parameter          (*name)  (all values)
6. Variable length Keyword only parameter             (**name) (all items)

################################################

1. function define  ->  def
2. function name    ->  add
3. parameter list   ->  ()     <-- tuple
4. code block       ->  :      <-- colon
5. doc              ->  '''Doc string '''     <---   help(), doc
6. function body    ->  program
7. return           ->  stop, return result   <---   None

help()
- function name 
- parameter list
- doc string

doc
- doc string

################################################

function

def fahrenheit(celsius):
    fahrenheit = (celsius * 9 / 5) + 32
    print(fahrenheit)


def fahrenheit(celsius):
    fahrenheit = (celsius * 9 / 5) + 32
    return fahrenheit


def fahrenheit(celsius):
    return (celsius * 9 / 5) + 32

################################################


import pandas


def fahrenheit(celsius):
    return (celsius * 9 / 5) + 32


t = pandas.read_excel("test_2024.xlsx")

c = list(t["Temperature(C)"])  # [27, 30, 29]
f = []

for celsius in c:
    f.append(fahrenheit(celsius))

t["Temperature(F)"] = f  # [80.6, 86.0, 84.2]

print(f)
print(t)

################################################

1. Normal parameter  (x, y, a)


def formula(x, y, a):
    return x**2 + y**2 + a


ans = formula(1, 2, 3)
print(ans)

################################################

def add(n1, n2):
    return n1 + n2


add(1, 2) # position only
add(2, 1) # position

add(n1=1, n2=2) # keyword only
add(n2=2, n1=1) # keyword name

add(1, n2=2) # pos + key

################################################

Standard form
1. position only
2. keyword only
3. pos + key

################################################

2. Default parameter (x, y, a=0)


def formula(x, y, a=0):
    return x**2 + y**2 + a


ans = formula(1, 2, 3)
print(ans)

ans = formula(1, 2)
print(ans)

################################################

3. Positional only parameter ( / ) 


def add(n1, n2, /):
    return n1 + n2


add(1, 2) # position only

################################################

4. Keyword only parameter ( * )


def info(*, name, age, ph_no, roll, grade):
    print("Name =", name)
    print("Age =", age)
    print("phone number =", ph_no)
    print("Roll number =", roll)
    print("Grade =", grade)


info(name="Mg Mg", age=10, ph_no="090000", roll=1, grade=5)

################################################################################################

Day.16

PEP.8
other   ->  lower snake case    ->   i_go_to_school
class   ->  upper cameal case   ->   IGoToSchool

################################################

1. def              ->  function define  
2. summation        ->  function name 
3. ()               ->  parameter list
4. n                ->  parameter (No.1)
5. colon (:)        ->  code block
6. '''...'''        ->  Doc string, doc
7. program          ->  function body
8. return           ->  stop and return result 

################################################


def summation(n):
    '''...'''
    ans = 0
    for i in range(1, n+1): # (start=1, stop=6, step=1) -> 1, 2, 3, 4, 5,
        ans += i
    return ans


x = summation(5)
print(x)

################################################

def factorial(n, /):
    '''
    It is a factorial function.
    eg.
    5! = 1 * 2 * 3 * 4 * 5 = 120
    6! = 1 * 2 * 3 * 4 * 5 * 6 = 720

    '''
    ans = 1
    for i in range(1, n+1): # (1, 5) -> 1 2 3 4 5
        ans *= i
    return ans


x = factorial(5)
print(x)

################################################

5. Variable length Positional only parameter (*name)


# Fixed length = 2 
def add(x, y, /):
    return x + y


x = add(1, 2)
print(x)


# Fixed length = 3
def add(x, y, z, /):
    return x + y + z


x = add(1, 2, 3)
print(x)

################################################

add()               ->   0     
add(1)              ->   1
add(1, 2)           ->   3
add(1, 2, 3)        ->   6
add(1, 2, 3, 4)     ->   10

################################################

* = all
add()                ->   n = ()
add(1)               ->   n = (1,)
add(1, 2)            ->   n = (1, 2)
add(1, 2, 3)         ->   n = (1, 2, 3)
add(1, 2, 3, 4)      ->   n = (1, 2, 3, 4)
add(1, 2, 3, 4, 5)   ->   n = (1, 2, 3, 4, 5)


# Variable length
def add(*n):
    ans = 0
    for i in n:
        ans += i
    return ans


a = add() # 0
b = add(1) # 1
c = add(1, 2) # 3
d = add(1, 2, 3) # 6
e = add(1, 2, 3, 4) # 10
print(a, b, c, d, e)

################################################


# Variable length
def sum(*n):
    ans = 0
    for i in n:
        ans += i
    return ans


t = sum(100, 20, 750, 40, 39)
print(t)

################################################

6. Variable length Keyword only parameter  


# Fixed length = 2 
def info(*, name, age):
    print(name, age)


info(name="Mg Mg", age=20)

################################################

# Variable length
def info(**i):
    print(i)


info()                                        ->   i = {}
info(name="Mg Mg")                            ->   i = {'name': 'Mg Mg'}
info(name="Mg Mg", age=20)                    ->   i = {'name': 'Mg Mg', 'age': 20}
info(name="Mg Mg", age=20, ph_no="0911111")   ->   i = {'name': 'Mg Mg', 'age': 20, 'ph_no': '0911111'}

################################################################################################

Day.17

1. No.3 (Simple is better than complex.)


def add(x, y, /):
    return x + y


add(1, 2)
add(x=1, y=2)
add(1, y=2)

################################################

2. No.4 (Complex is better complicated.)


def info(*, name, age, ph_no, roll, grade, id, color):
    print("Name =", name)
    print("Age =", age)
    print("phone number =", ph_no)
    print("Roll number =", roll)
    print("Grade =", grade)
    print("ID =", id)
    print("Skin color =", color)
    print("- " * 39)


info("Mg Mg", 10, "090000", 5, 1, "123456", "brown")
info(name="Mg Mg", age=10, ph_no="090000", roll=1, grade=5, id="123456", color="brown")

################################################

3. No.1 + No.4 

x, y   --->  1, 2, 3
a, b   --->  2



def f(x, y, *, a, b):
    print(x, y, a, b)


f(1, 2, a=3, b=4)
f(x=1, y=2, a=3, b=4)
f(1, y=2, a=3, b=4)
f(a=3, b=4, x=1, y=2)

################################################

4. No.3 + No.1 + No.4

parameter list

(a, b, c, /, d, e, f, *, g, h, i)

step.1 ->  check parameter list (/, *)
step.2 ->  divide

(form.1, all, form.2)
- (a, b, c)   -  1
- (d, e, f)   -  1, 2, 3
- (g, h, i)   -  2


def f(a, b, c, /, d, e, f, *, g, h, i):
    pass


f(1, 2, 3, 4, 5, 6, g=7, h=8, i=9)
f(1, 2, 3, d=4, e=5, f=6, g=7, h=8, i=9)
f(1, 2, 3, 4, 5, f=6, f=7, h=8, i=9)

################################################

5. No.3 + No.4 + No.2

- (name, age)   -  2
- (a, b, c)     -  1
- (country)     -  2   (No.2 -> "Myanmar")

- (a, b, c)     -  1   (No.3)
- (name, age)   -  2   (No.4)
- (country)     -  2   (No.4) (No.2 -> "Myanmar")


def f(a, b, c, /, *, name, age, country="Myanmar"):
    print(a, b, c, name, age, country)


f(1, 2, 3, name="Mg Mg", age=10)
f(1, 2, 3, name="Mg Mg", age=10, country="Burma")

################################################

6. No.5


# Variable length
def sum(*n):
    ans = 0
    for i in n:
        ans += i
    return ans


t = sum(100, 20, 750, 40, 39)
print(t)

################################################

7. No.6


def info(**i):
    print(i)


info(name="Mg Mg", age=10, ph_no="090000", roll=1, grade=5, id="123456", color="brown")
info(name="Mg Mg", age=10, ph_no="090000", roll=1, grade=5, id="123456", color="brown", first_term=[70, 74, 85])

################################################

8. No.3 + No.6

form.1, all, form.2,
a, b, c  ->  form.1 (No.3) (Simple is better than complex.)
info     ->  form.2 (No.6) (Complex is better complicated.)


def f(a, b, c, **info):
    print(a, b, c)
    print(info)


f(1, 2, 3, name="Mg Mg", roll=1, age=10)

################################################

9. No.3 + No.5

a, b, c  ->  form.1 (No.3) (Simple is better than complex.) 
x        ->         (No.5) (Simple is better than complex.) 

f(1, 2, 3)
f(1, 2, 3, 4, 5, 6)


def f(a, b, c, /, *x):
    print(a, b, c)
    print(x)
    print("- " * 39)


f(1, 2, 3)
f(1, 2, 3, 4, 5, 6)

################################################

10. No.4 + No.6


user_name, password   ->  form.2 (No.4) (*, user_name, password)
info                  ->         (No.6) (**info)

def f(*, user_name, password, **info):
    print(user_name, password)
    print(info)
    print("- " * 39)


f(user_name="Mg Mg", password="123456")
f(user_name="Mg Mg", age=10, ph_no="090000", roll=1, grade=5, id="123456", color="brown", password="123456")

################################################

11. No.5 + No.6 (all form, variable length)(all values, all items)

f()
f(1, 2, 3, 4 , 5, "apple", 1.2)
f(name="Mg Mg", age=20, roll=1)
f(1, 2, 3, 4 , 5, "apple", 1.2, name="Mg Mg", age=20, roll=1)


def f(*x, **y):
    print(x)
    print(y)
    print("- " * 39)


f()
f(1, 2, 3, 4 , 5, "apple", 1.2)
f(name="Mg Mg", age=20, roll=1)
f(1, 2, 3, 4 , 5, "apple", 1.2, name="Mg Mg", age=20, roll=1)

################################################

What is argument?

MTZ, MTZ
MTZ, Thadaw MTZ

Value, Value
Value, Argument

################################################

Where is argument?

100, 50

payment = 20

80, 50, 20

################################################

payment style

payment form kpay
payment form wave

positional argument
keyword argument

################################################

payment from kpay only
payment from wave only

positional only argument
keyword only argument

################################################

0, 10, 20, 100   arbitrary payment (arbitrary argument) 

arbitrary payment from kpay
arbitrary argument from position
arbitrary positional argument

arbitrary payment from wave
arbitrary keyword argument

################################################


def add(n1, n2=0):
    a = 1
    return n1 + n2

1
add(1, 2) # positional argument
add(n1=1, n2=2) # keyword argument

################################################

Arguments
1. Positional argument               No.1
2. Keyword argument                  No.1
3. Default argument                  parameter list
4. Positional only argument          No.3
5. Keyword only argument             No.4
6. Arbitrary positional argument     No.5
7. Arbitrary keyword argument        No.6

args         ->   Arbitrary positional arguments  ->  tuple
kw, kwargs   ->   Arbitrary keyword arguments     ->  dict

################################################

def add(n1, n2, /):
    return n1 + n2


add(1, 2) # (pos only)

################################################

def add(*, n1, n2):
    return n1 + n2


add(n1=1, n2=2) # (keyword only)

################################################

def f(*x):
    pass


f()             # Arbitrary argument -> ()
f(1)            # Arbitrary argument -> (1,)
f(1, 2)         # Arbitrary argument -> (1, 2)
f(1, 2, 3, 4)   # Arbitrary argument -> (1, 2, 3, 4)

################################################

def f(**x):
    pass


f()                                        # Arbitrary argument -> {}
f(name="Mg Mg")                            # Arbitrary argument -> {'name': "Mg Mg"}
f(name="Mg Mg", password=123456)           # Arbitrary argument -> {'name': "Mg Mg", 'password': 123456}
f(name="Mg Mg", password=123456, age=20)   # Arbitrary argument -> {'name': "Mg Mg", 'password': 123456, 'age'=20}

################################################

def f(*args):
    pass


f()             # Arbitrary argument -> ()
f(1)            # Arbitrary argument -> (1,)
f(1, 2)         # Arbitrary argument -> (1, 2)
f(1, 2, 3, 4)   # Arbitrary argument -> (1, 2, 3, 4)

################################################

def f(**kwargs):
    pass


f()                                        # Arbitrary argument -> {}
f(name="Mg Mg")                            # Arbitrary argument -> {'name': "Mg Mg"}
f(name="Mg Mg", password=123456)           # Arbitrary argument -> {'name': "Mg Mg", 'password': 123456}
f(name="Mg Mg", password=123456, age=20)   # Arbitrary argument -> {'name': "Mg Mg", 'password': 123456, 'age'=20}

################################################

No.5 + N0.2

print(*args, sep=' ', end='\n', file=None, flush=False)

################################################

No.3

sqrt(x, /)

################################################

import math


def sqrt(x, /):
    '''Return the square root of x.'''
    return x ** (1 / 2)


help(math.sqrt)
help(sqrt)

################################################################################################

Summary

1. def              ->  function define  
2. summation        ->  function name 
3. ()               ->  parameter list
4. n                ->  parameter (No.1)
5. colon (:)        ->  code block
6. '''...'''        ->  Doc string, doc
7. program          ->  function body
8. return           ->  stop and return result 

################################################

Standard form
1. assign value by position
2. assign value by keyword name
3. assign value by position and keyword name

################################################

Using unknown function

step.1 ->  check parameter list (/, *)
step.2 ->  divide

parameter list
(a, b, c, /, d, e, f, *, g, h, i)

(form.1, all, form.2)
- (a, b, c)   -  1
- (d, e, f)   -  1, 2, 3
- (g, h, i)   -  2

################################################

Parameters
1. Normal parameter, standard parameter               (x, y, a)
2. Default parameter                                  (x, y, a=0)
3. Positional only parameter(/)                       (x, y, /) (form.1)
4. Keyword only parameter(*)                          (*, x, y) (form.2)
5. Variable length Positional only parameter          (*name)  (all values)
6. Variable length Keyword only parameter             (**name) (all items)

################################################

Arguments
1. Positional argument               No.1
2. Keyword argument                  No.1
3. Default argument                  parameter list
4. Positional only argument          No.3
5. Keyword only argument             No.4
6. Arbitrary positional argument     No.5
7. Arbitrary keyword argument        No.6

args         ->   Arbitrary positional arguments  ->  tuple
kw, kwargs   ->   Arbitrary keyword arguments     ->  dict

################################################################################################

"""

