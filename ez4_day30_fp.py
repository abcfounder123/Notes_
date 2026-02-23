
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



"""

