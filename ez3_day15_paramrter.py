
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
3. Positional only parameter                          (n1, n2, /) (form.1)
4. Keyword only parameter                             (*, n1, n2) (form.2)
5. Variable length Positional only parameter
6. Variable length Keyword only parameter

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

"""


