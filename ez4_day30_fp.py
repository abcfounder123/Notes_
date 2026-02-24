
"""

1. Procedural Programming            10  and one bottle   (1 bit)
2. OOP                               10  and 10 bottle    (10 * 224 bits)
3. Functional Programming            data pipe line

#########################################

1. List Comprehension
   - Creating new list
   - Transforming data
   - Filtering data

#########################################

1. list to new list

l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
new2 = [n + 5 for n in l]
print(new2)

2. Transforming data (Kg to Lb)

kgs = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
lbs = [round(kg * 2.2, 2) for kg in kgs]
print(lbs)

3. Filtering data (even number)

l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers2 = [n for n in l if n % 2 == 0]

print(even_numbers2)

#########################################

1. list to new list

[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]     + 5
[6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
new = []
for n in l:
    new.append(n + 5)

l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
new2 = [n + 5 for n in l]
print(new2)

#########################################

2. Transforming data (Kg to Lb)

kgs = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
lbs = [kg * 2.2 for kg in kgs]
print(lbs)

kgs = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
lbs = [round(kg * 2.2, 2) for kg in kgs]
print(lbs)

#########################################

3. Filtering data (even number)

l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = []

for n in l:
    if n % 2 == 0:
        even_numbers.append(n)

print(even_numbers)


l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers2 = [n for n in l if n % 2 == 0]

print(even_numbers2)

##################################################################################

2. Decorator
   - new and old (different name)
   - old to new  (same name)(@decorator)

#########################################

1. new and old (different name)


def f2(x):
    def f3():
        print("-" * 41)
        x()
        print("-" * 41)
    return f3


def f1():
    print("Hello")


z = f2(f1)

f1()
f1()
f1()
f1()
f1()

z()

#########################################

2. old to new  (same name)

def f2(x):
    def f3():
        print("-" * 41)
        x()
        print("-" * 41)
    return f3


def f1():
    print("Hello")


f1 = f2(f1)

f1()
f1()
f1()
f1()
f1()

#########################################

def f2(x):
    def f3():
        print("-" * 41)
        x()
        print("-" * 41)
    return f3

@f2
def f1():
    print("Hello")


f1()
f1()
f1()
f1()
f1()

#########################################

f1 = f2(f1)

@f2
def f1():
    print("Hello")

#################################################################################

3. Generator
   - yield
   - eg.range, summation, A to Z


def generator():
    while True:
        yield 1

#########################################

1. range


def f(start, stop, step):
    ans = start
    while ans < stop:
        yield ans
        ans += step


number_sequence = f(2, 11, 2)
print(next(number_sequence))
print(next(number_sequence))
print(next(number_sequence))
print(next(number_sequence))
print(next(number_sequence))

#########################################

2. summation

summation of 1 = 1
summation of 2 = 1 + 2 = 3                2
summation of 3 = 1 + 2 + 3 = 6            3
summation of 4 = 1 + 2 + 3 + 4 = 10       4


def summation():
    ans = 1
    n = 2
    while True:
        yield ans
        ans += n
        n += 1


s = summation()
print(next(s))
print(next(s))
print(next(s))
print(next(s))

#########################################


def summation():
    ans = 1
    n = 2

    while True:
        yield ans
        ans += n
        n += 1


s = summation()

for i in range(1, 1001):
    print(f"summation of {i} = {next(s)}")

#########################################

n = 1
for s in summation():
    print(f"Summation of {n} = {s}")
    if n == 1000:
        break
    n += 1

#########################################

3. factorial


def factorial():
    ans = 1
    n = 2
    while True:
        yield ans
        ans *= n
        n += 1


n = 1
for s in factorial():
    print(f"Factorial of {n} = {s}")
    if n == 10:
        break
    n += 1
    
#########################################

4. even_number


def even_number():
    ans = 2
    while True:
        yield ans
        ans += 2


def even_number():
    ans = 0
    while True:
        ans += 2
        yield ans


e = even_number()

for _ in range(100):
    print(next(e))

#########################################

5. A to Z


def generator():
    n = 65
    while n < 91:
        yield chr(n)
        n += 1


for c in generator():
    print(c)

##################################################################################

4. Lambda

lambda x, y: x + y
lambda x, y: x - y
lambda x, y=0: x + y
lambda x, y, /: x + y
lambda : print("-" * 42)


def add(x, y):
    return x + y


def sub(x, y):
    return x - y


def add(x, y=0):
    return x + y


def add(x, y, /):
    return x + y


def line():
    print("-" * 42)


#########################################

For garbage collection

x = 1
y = 2
z = x + y
print(z)
>> int(1), int(2) ->  int(3)
>> 28 bytes 28 bytes 28 bytes -> 84 bytes, int 3

print(1 + 2)
>>28 bytes 28 bytes 28 bytes -> 0 bytes , int 0

#########################################

Test purpose

line = lambda :print("-" * 42)
line()


def line():
    print("-" * 42)


line()

##################################################################################

5. Higher-Order Functions

First-Order Functions -> f(x)

x = 3
y = 2x = 6


def f(x):
    y = 2 * x
    return y

#########################################

Second-Order Functions (produce First-Order Functions)


def s(a):

    def f(x):
        y = 2 * x
        return y

    return f


s(a) <- Second-Order Functions
f(x) <- First-Order Functions

#########################################

Third-Order Functions (produce Second-Order Functions)

def t():
    def s(a):
        def f(x):
            y = 2 * x
            return y

        return f

    return s

#########################################

fourth order function

def ff():
    def t():
        def s(a):
            def f(x):
                y = 2 * x
                return y

            return f
        return s
    return t

#########################################

first order function, normal function    -->  data

second order function                    -->  1st function
third order function                     -->  2nd function
fourth order function                    -->  3rd function

##################################################################################

6. Closure

- a process of closing somthing
- closing different data => s(2), s(3), s(7)

- data hiding (closing data)
- function factories
- decorators  (closing fun)


def s(a):

    def f(x):
        y = a * x
        return y

    return f


x = s(2)
print(x.__closure__)

#########################################

z = s(2) is same as z = f that closed a=2


def f(x):
    y = 2 * x
    return y


#########################################

z = s(3) is same as z = f that closed a=3


def f(x):
    y = 3 * x
    return y


#########################################


def s(a):

    def f(x):
        y = a * x
        return y

    return f


multiply_2 = s(2)  # a=2
print(multiply_2(1))      # 2 * x = 2
print(multiply_2(2))      # 2 * x = 4
print(multiply_2(3))      # 2 * x = 6

multiply_3 = s(3)  # a=3
print(multiply_3(1))      # 3 * x = 3
print(multiply_3(2))      # 3 * x = 6
print(multiply_3(3))      # 3 * x = 9

multiply_79 = s(79)

#########################################


def add_factory(n):
    def add(x):
        return x + n
    return add


add_1 = add_factory(1) # closed 1
print(add_1(2))

add_7 = add_factory(7) # closed 7
print(add_7(2))

#########################################

def alcohol_permit(age):
    return age >= age_by_country

def alcohol_permit(age):
    return age >= 19

def alcohol_permit(age):
    return age >= 21

def alcohol_permit(age):
    return age >= 15

def alcohol_permit(age):
    return age >= 16

#########################################


def factory(age_by_country):

    def alcohol_permit(age):
        return age >= age_by_country

    return alcohol_permit


age_by_country = 16 # 19, 16, 21, 18 by location of country
age = 18

alcohol_permit = factory(age_by_country)  # 19, 16, 21, 18

if alcohol_permit(age):
    print("You can buy.")

else:
    print("You can not buy.")

##################################################################################


def s(a, b, c):

    def f1(x):
        y = a + x
        return y

    def f2(x):
        y = a + b + x
        return y

    def f3(x):
        y = a + b + c + x
        return y

    return f1, f2, f3


x, y, z = s(1, 2, 3)

print(s.__closure__)     # None
print(x.__closure__)     # closed  1
print(y.__closure__)     # closed  1 and 2
print(z.__closure__)     # closed  1 and 2 and 3

##################################################################################

7. Map

- create a connection between fun and data, data pip line
- transform(kg to lb)

#########################################

>> transform(kg to lb)


def f1(kg):
    return round(kg * 2.2, 2)


kgs = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

#########################################

for kg in kgs:               # for loop
    lbs.append(f1(kg))


lbs = [f1(kg) for kg in kgs] # list comprehension

lbs = map(f1, kgs)           # map => a connection between f1 and kgs

#########################################

List comprehension example


def f1(kg):
    print("h")
    return round(kg * 2.2, 2)


kgs = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
l = [f1(kg) for kg in kgs] # 10 s

print(l)

#########################################

f1
f1
f1
f1
f1
f1
f1
f1
f1
f1
[2.2, 4.4, 6.6, 8.8, 11.0, 13.2, 15.4, 17.6, 19.8, 22.0]

#########################################

Map example


def f1(kg):
    print("h")
    return round(kg * 2.2, 2)


kgs = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
l = map(f1, kgs)

print(next(l))  # 1s

#########################################

f1
2.2

##################################################################################

Time consumption

all data => 1 hour

1 page  => 1 sec

##################################################################################

Memory consumption

lbs = [2.2, 4.4, 6.6, 8.8, 11.0, 13.2, 15.4, 17.6, 19.8, 22.0]
list = 50 bytes
float 10 = 300 bytes
total = 350 bytes

next(l)
float 1 = 30 bytes = 0 bytes

##################################################################################

kgs = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
lbs = [f1(kg) for kg in kgs]

list      => 50
int 10    => 280
lbs       => 50
float 10  => 300 bytes
total     => 680 bytes

########################################

kgs = range(1, 11)
l = map(f1, kgs)
print(next(l))  #  1 from range, f1(1) => 2.2

range(1, 11) => 30
map     => 30 byte
int 1   => 28 byte  => 0 bytes
float 1 => 30 bytes => 0 bytes

total   => 60 to 118

##################################################################################

Pip line

1000 GB  (1 page = 1MB )

database = 1 page (next value)
pip_line = map(negative_word, database)

total = 0  -> 10 -> 18 -> 100_000
total += next(pip_line)

##################################################################################

In List Comprehension or 'for loop',
if 1 error, None of result.


def f1(kg):
    print("f1")
    return round(kg * 2.2, 2)


kgs = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "abc"]   # 11 => 10 + 1(error)
lbs = [f1(kg) for kg in kgs]
print(lbs)

#########################################

Map can work well until error.


def f1(kg):
    print("f1")
    return round(kg * 2.2, 2)


kgs = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "abc"]   # 11 => 10 + 1(error)
lbs = map(f1, kgs)
print(next(lbs))
print(next(lbs))
print(next(lbs))
print(next(lbs))
print(next(lbs))
print(next(lbs))
print(next(lbs))
print(next(lbs))
print(next(lbs))
print(next(lbs))
# print(next(lbs))  # error

##################################################################################

8. Filter
- Filtering data

#########################################

Filtering data (even number)

1. for loop example

def is_even(n):
    return n % 2 == 0


l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = []

for n in l:
    if is_even(n):
        even_numbers.append(n)

print(even_numbers)

#########################################

2. LC example

l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
leven_numbers = [n for n in l if is_even(n)]   # [2, 4, 6, 8, 10]

print(leven_numbers)

#########################################

2. filter example

l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
f = filter(is_even, l)

print(next(f))
print(next(f))

#########################################


def is_even(n):
    print(f"is even({n})")
    return n % 2 == 0


l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
f = filter(is_even, l)

print(next(f))  #  1 from list , is_even(1) => 2 from list , is_even(2) => 2
print(next(f))  #  3 from list , is_even(3) => 4 from list , is_even(4) => 4

#########################################

Time and memory

After 10s,  [2, 4, 6, 8, 10]


2            after 2s
4            after 2s
6            after 2s
8            after 2s
10           after 2s

##################################################################################

9. Reduce

- reducing data
- all data to 1 data

#########################################

numbers to total
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10] to 55

#########################################

from functools import reduce


def add(a, b):
    return a + b


l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
r = reduce(add, l)  # add(1, 2) = 3 -> add(3, 3) = 6 -> add(6, 4) = 10 ... => 55

print(r)

##################################################################################

10. Data (Transform, filter, reduce)

1. map      =>   kg to lb                 =>   10 to 10

2. filter   =>   even numbers from list   =>   10 to 5

3. reduce   =>   all marks to otal marks  =>   6 to 1

##################################################################################



"""

