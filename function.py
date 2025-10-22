"""
Function

1. collection of code

def c_f():
    celcius = int(input("Enter degree celcius : "))
    fahrenheit = (celcius * 9 / 5) + 32
    ans = f"{celcius} °C is equal to {fahrenheit} °F."
    print(ans)
    
################################################

2. parameterized function

def c_f(celcius):
    fahrenheit = (celcius * 9 / 5) + 32
    ans = f"{celcius} °C is equal to {fahrenheit} °F."
    print(ans)
    
################################################

3. pure function

def c_f(celcius):
    fahrenheit = (celcius * 9 / 5) + 32
    return fahrenheit

def c_f(celcius):
    return (celcius * 9 / 5) + 32

################################################    

# iteration
for n in range(1000): # 0 to 999 -> 1000
    print(n, "apple")


# repeatation purpose
for _ in range(1000): # 0 to 999 -> 1000
    print("apple")
    
################################################

def c_f(celcius):
    fahrenheit = (celcius * 9 / 5) + 32
    ans = f"{celcius} °C is equal to {fahrenheit} °F."
    print(ans)


celsius_list = [27, 30, 26, 28, 32, 29, 29, 30, 27, 27, 30, 26, 28, 32, 29, 29, 30, 27, 27, 30, 26, 28, 32, 29, 29, 30, 27, 27, 30, 26, 28, 32, 29, 29, 30, 27, 27, 30, 26, 28, 32, 29, 29, 30, 27, 27, 30, 26, 28, 32, 29, 29, 30, 27]

for i in celsius_list:
    c_f(i)
    
################################################    
    
function    ---> collection of code    
c_f         ---> function name    
()          ---> parameter list/tuple
celcius     ---> first parameter

################################################

def add(n1, n2):
    print(n1 + n2)

add         ---> function name    
()          ---> parameter list/tuple
n1          ---> first parameter
n2          ---> second parameter

################################################

Parameters

1. normal parameter                               (x, y)
2. default parameter                              (x, y, b=0)
3. positional only parameter                      (x, y, /)       2
4. keword only parameter                          (*, x, y)
5. variable-length positional parameter 
6. variable-length keyword parameter  

################################################

x ** 2 + y ** 2 + b
x ** 2 + y ** 2 + 0

def f(x, y, b=0):
    z = x ** 2 + y ** 2 + b
    print(z)
    
################################################

f           ---> function name    
()          ---> parameter list/tuple
x           ---> first parameter       normal parameter       x
y           ---> second parameter      normal parameter       y
b           ---> third parameter       default parameter      b=0
0           ---> default value

################################################

Standard form
1. assign value by position
2. assign value by keyword name
3. assign value by position and keyword name

################################################

2. default parameter

def add(n1, n2):
    print(n1 + n2)


add(3, 4) # assign value by position
add(n1=3, n2=4) # assign value by keyword name
add(3, n2=4) # assign value by position and keyword name

################################################

3. positional only parameter

def add(n1, n2, /):
    print(n1 + n2)

add          ---> function name    
()           ---> parameter list/tuple
n1           ---> first parameter       normal parameter       x
n2           ---> second parameter      normal parameter       y
/            ---> third parameter       positional only parameter  /

################################################

4. keword only parameter

def add(*, n1, n2): 
    print(n1 + n2)

add          ---> function name    
()           ---> parameter list/tuple
*            ---> first parameter        keword only parameter  *
n1           ---> second parameter       normal parameter       x
n2           ---> third parameter        normal parameter       y

################################################################################################

day.15

Creating parameters

1. x, y, a       -->  (x, y, a)
2. x, y, a=0     -->  (x, y, a=0)
3. x, y          -->  (x, y, /)
4. name, age, ph, grade, id, color, parent  --> (*, ... )
5. *args
6. **kwargs, **kw

################################################

3. /

def add(x, y, /):
    print(x + y)


add(1, 2)
add(x=1, y=2)
add(1, y=2)

################################################

4. *

def info(*, name, age, ph, grade, id, color, parent):
    print("Name =", name)
    print("Age =", age)
    print("Phone No =", ph)
    print("Grade =", grade)
    print("ID =", id)
    print("Color =", color)
    print("Parent =", parent)


print(" -" * 42)
info(name="Mg Mg", age="09000", ph=10, grade=5, id="9/wtn(N)0000", color="brown", parent="U Ba")
info(name="Mg Mg", age=10, ph="09000", grade=5, id="9/wtn(N)0000", color="brown", parent="U Ba")

################################################

No.1 + No.4

x, y --> 1, 2, 3 
a, b --> 2       

(x, y)
(*, a, b)
(x, y, *, a, b)


def f(x, y, *, a, b):
    print(x, y, a, b)


f(1, 2, a=3, b=4)
f(x=1, y=2, a=3, b=4)
f(1, y=2, a=3, b=4)
f(a=3, b=4, x=1, y=2)

################################################

No.3 + No.1 + No.4

a, b, c   ---> 1
x, y, z   ---> 1, 2, 3
i, j, k   ---> 2

(a, b, c, /)
(x, y, z)
(*, i, j, k)
(a, b, c, /, x, y, z, *, i, j, k)


a, b, c, /, x, y, z, *, i, j, k
group.1 --> a, b, c     1
group.2 --> x, y, z     1,2,3
group.3 --> i, j, k     2

def f(a, b, c, /, x, y, z, *, i, j, k):
    print(a, b, c, x, y, z, i, j, k)


f(1, 2, 3, 4, 5, 6, i=7, j=8, k=9)
f(1, 2, 3, x=4, y=5, z=6, i=7, j=8, k=9)
f(1, 2, 3, 4, y=5, z=6, i=7, j=8, k=9)

################################################

No.3 + No.4 + No.2

a, b, c    --> 1  (No.3)
name, age  --> 2  (No.4)
country    --> 2  (No.4)(No.2 -> "Myanmar")

(a, b, c, /, *, name, age, country="Myanmar")


def f(a, b, c, /, *, name, age, country="Myanmar"):
    print(a, b, c, name, age, country)


f(1, 2, 3, name="Mg Mg", age=10)
f(1, 2, 3, name="Mg Mg", age=10, country="Burma")

################################################

5. *x

* --> all


def f(*x):
    print(x)


f()
f(1)
f(1, 2)
f(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

################################################

()
(1,)
(1, 2)
(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

################################################

6. **x


def f(**x):
    print(x)


f()
f(x=1, y=2)
f(x=1, name="Mg Mg", age=20, y=2)

{}
{'x': 1, 'y': 2}
{'x': 1, 'name': 'Mg Mg', 'age': 20, 'y': 2}

################################################

Parameters
1. parameter 
2. default parameter
3. p only parameter
4. k only parameter
5. variable-length p only parameter      (*args)
6. variable-length k only parameter      (*kwargs), (*kw)

################################################

Arguments
1. default argument              y=3, No.2
2. positional argument           (1, 2)                  args
3. keyword argument              (x=1, y=2)              kwargs, kw
4. positional only argument      (1, 2), No.3
5. keyword only argument         (x=1, y=2), No.4

################################################

"Mg Mg" is "keyword only argument".

- info(name="Mg Mg") 
- def info(*, name):

"Mg Mg" is "p only argument".
- info("Mg Mg")
- def info(name, /):

################################################

def add(x, y, /):
    print(x + y)


add(1, 2)
x <-- position only parameter
1 <-- positional only argument

################################################

def f(*, x, y=3):
    print(x, y)


f(x=1, y=2)
x <-- keyword only parameter
1 <-- keyword only argument

################################################

as you like --> No.5 + No.6

# *args, **kwargs, **kw  
def f(*x, **y):
    print(x)
    print(y)
    print(" -" * 42)


f()
f(1, 2, 3)
f(x=1, y=2, name="X")
f(1, 2, 3, 4, 5 ,6, x=1, y=2, name="X")

################################################

No.3 + No.5

a, b, c, /  ->  3 
*x          ->  5

(a, b, c, /, *x):


def f(a, b, c, /, *x):
    print(a, b, c, x)


f(1, 2, 3, 4, 5 , 6)

################################################

help(print)

# print(*args, sep=' ', end='\n', file=None, flush=False)

################################################################################################

"""

