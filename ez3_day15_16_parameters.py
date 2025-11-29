
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
5. Variable length Positional only parameter          (*name)
6. Variable length Keyword only parameter             (**name)

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


t = add(100, 20, 750, 40, 39)
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

################################################

# No.3 + No.1 + No.4
def f(a, b, c, /, d, e, f, *, g, h, i):
    pass


f(1, 2, 3, 4, 5, f=6, g=7, h=8, i=9)
f(1, 2, 3, 4, 5, 6, g=7, h=8, i=9)
f(1, 2, 3, 4, 5, 6, 7, h=8, i=9)

################################################


# No.5 + No.6
def f(*x, **y):
    print(x)
    print(y)


f()
f("apple")
f(name="Mg Mg")
f(1, 2, 3, 4, 5, "apple", 1.0, f=6, g=7, h=8, i=9, name="Mg Mg")

################################################################################################

"""


