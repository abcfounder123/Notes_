
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

"""

