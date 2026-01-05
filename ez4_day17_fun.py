
"""
Day.17  

Function

1. function define    ->   def
2. function name      ->   add
3. parameter list     ->   ()    <--- tuple
4. code block         ->   :
5. doc                ->   ''' documentation string '''   <---   doc, help()
6. function body      ->   program
7. return             ->   stop, return result

################################################


def add(x, y):
    '''
    documentation string
    '''
    return x + y


def length(x):
    '''Return the number of items in a container.'''
    t = 0
    for _ in x:
        t += 1
    return t
    

################################################

Parameters
1. Normal parameter, Standard parameter
2. Default parameter
3. Positional only parameter
4. Keyword only parameter
5. Variable length positional only parameter
6. Variable length keyword only parameter

################################################

Standard form
1. positional only       add(1, 2)
2. keyword only          add(n1=1, n2=2)
3. pos + key             add(1, n2=2)

################################################

1. Normal parameter, Standard parameter


def add(n1, n2):
    return n1 + n2


add(1, 2)  # positional only
add(2, 1)

add(n1=1, n2=2)  # keyword only
add(n2=2, n1=1)

add(1, n2=2) # pos + key

################################################

2. Default parameter  ( default value )


def f(x, y, a=0):
    return x ** 2 + y ** 2 + a


ans = f(1, 2, 3)
print(ans)

ans = f(1, 2)
print(ans)

################################################

3. Positional only parameter  ( / )

Simple is better than complex.


def add(n1, n2, /):
    return n1 + n2


add(1, 2)  # positional only

################################################

4. Keyword only parameter ( * )

Complex is better than complicated.


def info(*, name, age, ph_no, roll, grade):
    pass


info(name="Mg Mg", age="09123456", ph_no=9, roll=1, grade=3)

################################################

1. a, b, c              ->   (a, b, c)                              F 1 2 3
2. name, age, country   ->   (name, age, country="Myanmar")         F 1 2 3
3. x, y, z              ->   (x, y, z, /)                           F 1 
4. name, age, country   ->   (*, name, age, country)                F 2
5. unlimited pos        ->   (*args)                                F 1
6. unlimited kw         ->   (**kw), (**kwargs)                     F 2

################################################

5. Variable length positional only parameter ( *args )

positional only arguments (args)


# fixed length = 2
def add(n1, n2, /):
    return n1 + n2


# fixed length = 3
def add2(n1, n2, n3, /):
    return n1 + n2 + n3


# variable length
def add(*args):
    t = 0

    for number in args:
        t += number

    return t

################################################

add()                           ->  0
add(1)                          ->  1
add(1, 2)                       ->  3
add2(1, 2, 3)                   ->  6
add2(1, 2, 3, 4)                ->  10

################################################

*    ->   all 

add()                           ->  n = ()
add(1)                          ->  n = (1,)
add(1, 2)                       ->  n = (1, 2)
add2(1, 2, 3)                   ->  n = (1, 2, 3)  
add2(1, 2, 3, 4)                ->  n = (1, 2, 3, 4) 

################################################

6. Variable length keyword only parameter

keyword only arguments (kw, kwargs)

name
name, password
name, password, age,
name, password, age, ph_no, roll, grade

################################################


def info(**kw):
    print(kw)


info(name="Mg Mg", age=9, roll=1, grade=3)

################################################


def f(*x, **y):
    print(x)
    print(y)


f(1, 2, 3, "apple", name="Mg Mg", age=9)

################################################################################################

Day.18

1. No.3   ( Simple is better than complex. )

def add(x, y, /):
    return x + y


add(1, 2)

################################################

2. No.4  ( Complex is better than complicated. )


def info(*, name, age, ph_no, roll, grade):
    pass


info(name="Mg Mg", age="09123456", ph_no=9, roll=1, grade=3)

################################################

3. No.1 + No.4

x, y        --->   1, 2, 3
name, age   --->   2


def f(x, y, *, name, age):
    print(x, y, name, age)


f(1, 2, name="Mg Mg", age=9)
f(x=1, y=2, name="Mg Mg", age=9)
f(1, y=2, name="Mg Mg", age=9)

################################################

4. No.3 + No.1 + No.4

(a, b, c, /, x, y, *, name, age)

step.1   ->   check parameter list (/, *)
step.2   ->   divide

- (a, b, c)    ->   1
- (x, y)       ->   1, 2, 3
- (name, age)  ->   2


def f(a, b, c, /, x, y, *, name, age):
    print(a, b, c, x, y, name, age)


f(1, 2, 3, 4, 5, name="Mg Mg", age=9)
f(1, 2, 3, x=4, y=5, name="Mg Mg", age=9)
f(1, 2, 3, 4, y=5, name="Mg Mg", age=9)
f(1, 2, 3, name="Mg Mg", y=5, age=9, x=4)

################################################

5. No.3 + No.4 + No.2

form.1  -> left
form.2  -> right
1, 2, 3 -> middle

- (a, b, c)    ->   1               No.3
- (name, age)  ->   2               No.4
- country      ->   2 ("Myanmar")   No.4 + No.2

(a, b, c, /, *, name, age, country="Myanmar")

- (x, y)       ->   1, 2, 3
(a, b, c, /, x, y, *, name, age, country="Myanmar")

(d, e, f)      ->   1
(a, b, c, d, e, f, /, x, y, *, name, age, country="Myanmar")

ph_no          ->   2
(a, b, c, d, e, f, /, x, y, *, name, age, ph_no, country="Myanmar")

city = "Yangon"
(a, b, c, d, e, f, /, x, y, *, name, age, ph_no, country="Myanmar", city = "Yangon")

z              ->  1, 2, 3
(a, b, c, d, e, f, /, x, y, z, *, name, age, ph_no, country="Myanmar", city = "Yangon")

################################################

6. No.5

# variable length  + simple
def add(*args):
    t = 0

    for number in args:
        t += number

    return t

################################################

m1    60 + 65 + 70                 195
m2    60 + 65 + 70 + 77 + 68       340
m3

################################################

7. No.6

# variable length  + complicated
def info(**kw):
    print(kw)


info(name="Mg Mg", age=9, ph_no="09123456")

################################################

8. No.3 + No.6

at least 3 value by pos and more items


def f(a, b, c, /, **kw):
    print(a, b, c)
    print(kw)


f(1, 2, 3, name="Mg Mg", age=9)

################################################

9. No.3 + No.5

at least 3 value by pos and more value


def f(a, b, c, /, *args):
    print(a, b, c)
    print(args)


f(1, 2, 3, 4, 5, 6, 7)

################################################

10. No.4 + No.6

at least 2 value by name and more items

user_name, password 
gender, age, country, ....  100


def f(*, user_name, password, **kw):
    print(user_name, password)
    print(kw)


f(user_name="Mg Mg", password=123456, age=20, gender="male")

################################################

11. No.5 + No.4


def f(*x, user_name, password):
    print(user_name, password)
    print(x)


f(1, 2, user_name="Mg Mg", password="123456")

################################################

11. No.3 + No.5 + No.4 + No.6

at least 3 value by pos and more value
a, b, c
*args

at least 2 value by name and more items
*, user_name, password
**kw


def f(a, b, c, /, *args, user_name, password, **kw):
    print(a, b, c)
    print(args)
    print(user_name, password)
    print(kw)


f(1, 2, 3, 4, 5, 6, user_name="Mg Mg", password="123456", age=20, gender="male")

################################################

12. No.5 + No.6  (all forms, variable length)

all values, all items
variable length of values and variable length of items


def f(*args, **kw):
    print(args)
    print(kw)


f()
f(1)
f(age=9)
f(1, 2, 3, name="Mg Mg", age=9)

################################################

Arguments
1. Positional arguments              No.1
2. Keyword arguments                 No.1
3. Default arguments                 No.2  (parameter list)
4. Positional only arguments         No.3
5. Keyword only arguments            No.4
6. Arbitrary positional arguments    No.5
7. Arbitrary keyword arguments       No.6


unlimited values    Arbitrary positional arguments    No.5
unlimited items     Arbitrary keyword arguments       No.6

################################################

Parameters
1. Normal parameter, Standard parameter
2. Default parameter
3. Positional only parameter
4. Keyword only parameter
5. Variable length positional only parameter
6. Variable length keyword only parameter

################################################

1. a, b, c              ->   (a, b, c)                              F 1 2 3
2. name, age, country   ->   (name, age, country="Myanmar")         F 1 2 3
3. x, y, z              ->   (x, y, z, /)                           F 1 
4. name, age, country   ->   (*, name, age, country)                F 2
5. unlimited pos        ->   (*args)                                F 1
6. unlimited kw         ->   (**kw), (**kwargs)                     F 2

################################################

1. Parameter(6)
2. Create
3. Use
4. Arguments(7)

################################################################################################

"""

