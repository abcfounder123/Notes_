
"""
1. print()
2. comment => #
3. str, string
4. string concatenation => +
5. input() 
6. prompt => "Enter your age : "
7. TypeCasting   ( 26 => "26" )

##########################################

Arithmetic Operators
8. age = 2026 - Birth year , "You are 26 years old."
9. kyats to dollar, "10000 kyats is equal to 2 dollars."
10. 350 seconds => 5 minutes + 50 seconds
11. 90350 seconds => 1 days 1 hours 5 minutes and 50 seconds

##########################################

Comparison Operators
12. If mark is greater than or equal to 40, exam pass.
13. If mark is less than 40, exam fail.

##########################################

Logical Operators
1. not   =>  opposite
2. and   =>  all
3. or    =>  any

14. If mark is greater than 40 or mark is equal to 40, exam pass.
15. If username is equal to "Mg Mg" and password is equal to "12345", login successful.
16. if full water, Motor Stop.
17. if not full water, Motor ON.    

##########################################

birth_year = int(input("Enter birth year : "))
age = 2026 - birth_year
ans = "You are " + str(age) + " years old."
print(ans)

##########################################

kyat = int(input("Enter Kyats : "))
dollar = kyat / 5000
ans = str(kyat) + " kyats is equal to " + str(dollar) + " dollars."
print(ans)

##########################################

sec = int(input("Seconds : "))
m = sec // 60      # 5
s = sec % 60       # 50

ans = str(m) + " minutes and " + str(s) + " seconds"
print(ans)

##########################################

                  90350 seconds = 1 days 1 hours 5 minutes and 50 seconds
      
         1505 minutes     +     50 seconds        

     25 hours    +    5 minutes                  

1 day +  1 hours                             

##########################################

sec = int(input("Seconds : "))

m = sec // 60      # 1505 min
s = sec % 60       # 50   sec

h = m // 60        # 25  hour
min = m % 60       # 5   min

day = h // 24      # 1 day
hour = h % 24      # 1 hour

ans = str(day) + " days " + str(hour) + " hours " + str(min) + " minutes and " + str(s) + " seconds"
print(ans)

##########################################

sec = int(input("Seconds : "))

day = (sec // 3600) // 24

hour = (sec // 3600) % 24

min = (sec // 60) % 60

sec = sec % 60

ans = str(day) + " days " + str(hour) + " hours " + str(min) + " minutes and " + str(sec) + " seconds"
print(ans)

##########################################

Comparison Operators
12. If mark is greater than or equal to 40, exam pass.
13. If mark is less than 40, exam fail.


If mark is greater than or equal to 40, exam pass.
if mark >= 40: print("exam pass")

If mark is less than 40, exam fail.
if mark < 40: print("exam fail")

##########################################

Logical Operators

14. If mark is greater than 40 or mark is equal to 40, exam pass.
15. If username is equal to "Mg Mg" and password is equal to "12345", login successful.
16. if full water, Motor Stop.
17. if not full water, Motor ON. 

If mark is greater than 40 or mark is equal to 40, exam pass.
if mark > 40 or mark == 40: print("exam pass")

If username is equal to "Mg Mg" and password is equal to "12345", login successful.
if username == "Mg Mg" and password == "12345": print("login successful")

if full water, Motor Stop.
if full_water: print("Motor ON")

if not full water, Motor ON.
if not full_water: print("Motor ON")

##########################################

username = input("username : ")
password = input("password : ")

if username == "Mg Mg" and password == "12345": print("login successful")

##########################################

full_water = True

if full_water: print("Motor OFF")

if not full_water: print("Motor ON")

##########################################

Procedural programming
1. Sequence
2. Selection
3. Loop
4. Function

#################################################

1. Sequence
   - top
   - left
   - parenthesis first

#################################################

2. Selection (if, elif, else)

#####################################

1. if 

ချိတ်ဆက်ထားတဲ့ condition မှန်ရင် အလုပ်လုပ်သည်။

#####################################

mark = int(input("Marks = "))

if mark >= 40:
    print("Exam pass.")

#####################################


2. else

ချိတ်ဆက်ထားတဲ့ condition မှားရင် အလုပ်လုပ်သည်။

#####################################

mark = int(input("Marks = "))

if mark >= 40:
    print("Exam pass.")

else:
    print("Exam fail.")

#####################################

mark = int(input("Marks = "))

c1 = mark >= 40

if c1:
    print("Exam pass.")

else:
    print("Exam fail.")

#####################################

3. all from all

mark = 500

c1 = mark >= 500
c2 = mark >= 400
c3 = mark >= 300
c4 = mark >= 240

if c1: print("Doctor.")

if c2: print("Programmer.")

if c3: print("Engineer.")

if c4: print("Distance.")

#####################################

4. one from all

mark = 500

c1 = mark >= 500
c2 = mark >= 400
c3 = mark >= 300
c4 = mark >= 240

if c1: print("Doctor.")

if not c1 and c2: print("Programmer.")

if not c1 and not c2 and c3: print("Engineer.")

if not c1 and not c2 and not c3 and c4: print("Distance.")

#####################################

5. one from all by Python ( elif ) ( else + if )

mark = 500

c1 = mark >= 500
c2 = mark >= 400
c3 = mark >= 300
c4 = mark >= 240

if c1: print("Doctor.")

elif c2: print("Programmer.")

elif c3: print("Engineer.")

elif c4: print("Distance.")

#####################################

Programmer  =>  not c1 and c2
Engineer    =>  not c1 and not c2 and c3
Doctor      =>  c1
Distance    =>  not c1 and not c2 and not c3 and c4

Doctor      =>  c1
Programmer  =>  not c1 and c2
Engineer    =>  not c1 and not c2 and c3
Distance    =>  not c1 and not c2 and not c3 and c4

Grade 12    =>  not c1 and not c2 and not c3 and not c4

#####################################

6. if + elif + else

if not c1 and not c2 and not c3 and not c4: print("Grade 12.")

#####################################

mark = int(input("Marks = "))

c1 = mark >= 500
c2 = mark >= 400
c3 = mark >= 300
c4 = mark >= 240

if c1: print("Doctor.")

elif c2: print("Programmer.")

elif c3: print("Engineer.")

elif c4: print("Distance.")

else: print("Grade 12.")

#####################################

A+             90
A              80
B              70
C              50
F

A+  =>  c1
A   =>  not c1 and c2
B   =>  not c1 and c2 and c3
C   =>  not c1 and c2 and not c3 and c4
F   =>  not c1 and c2 and not c3 and not c4

c1 = mark >= 90
c2 = mark >= 80
c3 = mark >= 70
c4 = mark >= 50

#####################################

mark = 100

c1 = mark >= 90
c2 = mark >= 80
c3 = mark >= 70
c4 = mark >= 50


if c1:
    print("A+")

elif c2:
    print("A")

elif c3:
    print("B")

elif c4:
    print("C")

else:
    print("Fail")

#####################################

String formatting (fat)
- fill character (space)
- alignment (<, >, ^) (right)
- total character count
- f, :

"BMW-0001"
"BMW-0011"
"BMW-0100"

n = 1
s = f"BMW-{n:0>4}"
print(s)

##########################################################################

3. Loop
   1. Iteration - value
   2. Looping - 12 times
   3. nested loop
   4. definite loop (for)
   5. indefinite loop (while)
   6. break => to stop loop

##########################################

1. Iteration

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]     13

for number in numbers:
    print(f"2 x {number} = {2 * number}")

for r in range(1, 13, 1):
    print(f"2 x {r} = {2 * r}")

##########################################

2. Looping - 12 times   (definite loop)

for _ in range(12):
    print("apple")

##########################################

3. nested loop

print("2 x 1 = 1")

2 x 1 = 2
2 x 2 = 4
2 x 3 = 6
2 x 4 = 8
2 x 5 = 10
2 x 6 = 12
2 x 7 = 14
2 x 8 = 16
2 x 9 = 18
2 x 10 = 20
2 x 11 = 22
2 x 12 = 24


for r in range(1, 13):
    print("1 * " + str(r) + " = " + str(1 * r))

print("-" * 42)


for r in range(1, 13, 1):
    print(f"2 x {r} = {2 * r}")

print('-' * 42)

##########################################

for r in range(1, 13, 1):
    print(f"2 x {r} = {2 * r}")

print('-' * 42)

for r in range(1, 13, 1):
    print(f"3 x {r} = {3 * r}")

print('-' * 42)

for r in range(1, 13, 1):
    print(f"4 x {r} = {4 * r}")

print('-' * 42)

for r in range(1, 13, 1):
    print(f"5 x {r} = {5 * r}")

print('-' * 42)

for r in range(1, 13, 1):
    print(f"6 x {r} = {6 * r}")

print('-' * 42)

....

....

##########################################

for l in range(1, 17, 1):
    for r in range(1, 13, 1):
        print(f"{l} x {r} = {l * r}")
    print('-' * 42)

####################################################################################

3. Loop
   1. Iteration - value
   2. Looping - 12 times ( underscore )
   3. nested loop
   4. definite loop (for)
   5. indefinite loop (while)
   6. break => to stop loop
   7. exit  => to stop program
   8. else  => if, for, while

##########################################

5. Indefinite loop (while)

condition = True

while condition:

    user_name = input("user name = ")
    password = input("password = ")

    if user_name == "abc" and password == "12345":
        print("login successful.(opened abc' account.)")
        condition = False

    else:
        print("Wrong password. Try again.")

    print('-' * 42)


##########################################

6. break => to stop loop

while True:

    user_name = input("user name = ")
    password = input("password = ")

    if user_name == "abc" and password == "12345":
        print("login successful.(opened abc' account.)")
        break

    else:
        print("Wrong password. Try again.")

    print('-' * 42)

##########################################

"Indefinite loop with maximum count 3"

n = 0

while True:

    user_name = input("user name = ")
    password = input("password = ")

    if user_name == "abc" and password == "12345":
        print("login successful.(opened abc' account.)")
        break

    else:
        print("Wrong password. Try again.")
    
    print('-' * 42)
    
    n += 1
    if n == 3:
        print("Wait 24 hours.")
        break

    
##########################################

8. else  => if, for, while

parents = ["UBa@gmail.com", "UMya@gmail.com", "DawMya@gmail.com"]

for email in parents:
    print(f"Sent Congratulation letter to {email}")

else:
    print("Successfully sent all email.")

####################################################################################
####################################################################################

4. Function
   - code reuse
   - call, invoke   => ( )

##########################################

for r in range(1, 13, 1):
    print(f"2 x {r} = {2 * r}")

print('-' * 42)


for r in range(1, 13, 1):
    print(f"2 x {r} = {2 * r}")

print('-' * 42)


for r in range(1, 13, 1):
    print(f"2 x {r} = {2 * r}")

print('-' * 42)

##########################################

Step.1


def m2():
    for r in range(1, 13, 1):
        print(f"2 x {r} = {2 * r}")

    print('-' * 42)


def m3():
    for r in range(1, 13, 1):
        print(f"3 x {r} = {3 * r}")

    print('-' * 42)


def m4():
    for r in range(1, 13, 1):
        print(f"4 x {r} = {4 * r}")

    print('-' * 42)


m2()
m3()
m4()

##########################################

Step.2


def m(n):
    for r in range(1, 13, 1):
        print(f"{n} x {r} = {n * r}")

    print('-' * 42)


m(n=1)
m(n=2)
m(n=3)
m(n=4)
m(n=1028)

##########################################

Step.3


def m12(n):
    for r in range(1, 13, 1):
        print(f"{n} x {r} = {n * r}")

    print('-' * 42)


def m10(n):
    for r in range(1, 11, 1):
        print(f"{n} x {r} = {n * r}")

    print('-' * 42)


m12(n=2)
m10(n=2)

##########################################

Step.4

def m(n1, n2):
    for r in range(1, n2, 1):
        print(f"{n1} x {r} = {n1 * r}")

    print('-' * 42)


m(2, 11)
m(2, 13)

####################################################################################

Step.1  (multiple by 2)(1 to 12)


def m2():
    for r in range(1, 13, 1):
        print(f"2 x {r} = {2 * r}")

    print('-' * 42)


##########################################

Step.2   (multiple by n)(1 to 12)


def m(n):
    for r in range(1, 13, 1):
        print(f"{n} x {r} = {n * r}")

    print('-' * 42)

##########################################

Step.3  (multiple by n)(1 to n2 - 1)


def m(n1, n2):
    for r in range(1, n2, 1):
        print(f"{n1} x {r} = {n1 * r}")

    print('-' * 42)


##########################################

Step.4  (multiple by n)(1 to n2)

def m2(n, nn):
    for r in range(1, nn+1, 1):
        print(f"{n} x {r} = {n * r}")
    print('-' * 42)
    
####################################################################################

Parameters(6)

1. Normal Parameters, Standard Parameters        (x, y)
2. Default Parameters                            country="Myanmar"
3. Positional only Parameters                    /
4. Keyword only Parameters                       *
5. Variable length positional only Parameters    *name, *args
6. Variable length keyword only Parameters       **name, **kw, **kwargs

*  <---  all values
**  <---  all items

Standard Form(3)
1. Position                f(1, 2)
2. Keyword name            f(x=1, y=2)
3. 1 + 2                   f(1, y=2)

##########################################

1. Normal Parameters


def add(x, y):
    print(x + y)


add(1, 2)

##########################################

2. Default Parameters


def info(name, password, country="Myanmar"):
    print(name, password, country)


info("abc", "12345")

##########################################

3. Positional only Parameters

Simple is better than complex.

##########################################


def add(x, y, /):
    print(x + y)


add(1, 2)
add(2, 1)

##########################################

4. Keyword only Parameters

Complex is better than complicated.

##########################################


def info(*, name, age, ph_no, blood, height, weight, country):
    print(f"Name = {name}")
    print(f"age = {age}")
    print(f"ph_no = {ph_no}")
    print(f"blood = {blood}")
    print(f"height = {height}")
    print(f"weight = {weight}")
    print(f"country = {country}")


info(name="Mg Mg", age=10, weight=20, ph_no="09123456", height='''4' 2"''', country="Myanmar", blood="O")

##########################################

(x, y)
x <-- first parameter  (No.1)
y <-- second parameter (No.1)

(x, y, /)
x <-- first parameter  (No.3)
y <-- second parameter (No.3)

(*, x, y)
x <-- first parameter  (No.4)
y <-- second parameter (No.4)

####################################################################################

5. Variable length positional only Parameters

Fixed length = 2


def add(x, y):
    ans = x + y
    print(ans)


add(1, 2)

##########################################

variable length

add()
add(1)
add(1, 2)
add(1, 2, 3)
add(1, 2, 3, 4)

##########################################


def add(*numbers):
    ans = 0

    for number in numbers:
        ans += number

    print(ans)


add()
add(1)
add(1, 2)
add(1, 2, 3)
add(1, 2, 3, 4)

##########################################

6. Variable length keyword only Parameters

Fixed length = 7


def info(*, name, age, ph_no, blood, height, weight, country):
    print(f"Name = {name}")
    print(f"age = {age}")
    print(f"ph_no = {ph_no}")
    print(f"blood = {blood}")
    print(f"height = {height}")
    print(f"weight = {weight}")
    print(f"country = {country}")


info(name="Mg Mg", age=10, weight=20, ph_no="09123456", height='''4' 2"''', country="Myanmar", blood="O")

##########################################

Variable length


def info(**x):
    print(x)


info()
info(name="Mg Mg")
info(name="Mg Mg", age=10)
info(name="Mg Mg", age=10, ph_no="09123456")

####################################################################################

Combination of Parameters (12)


1. Simple is better than complex. (N0.3)


def add(n1, n2, /):
    print(n1 + n2)


add(1, 2)

##########################################

2. Complex is better than complicated. (No.4)


def info(*, name, age, grade, roll):
    print(name, age, grade, roll)


info(name="abc", age=10, grade="A", roll=1)

##########################################

3. No.1 + No.4

x, y        --->   F1, F2, F3
name, age   --->   F2


def f(x, y, *, name, age):
    print(x, y, name, age)


f(1, 2, name="Mg Mg", age=10)
f(x=1, y=2, name="Mg Mg", age=10)
f(1, y=2, name="Mg Mg", age=10)

##########################################

4. N0.3 + N0.1 + No.4

a, b, c     --->   F1
x, y        --->   F1, F2, F3
name, age   --->   F2


def f(a, b, c, /, x, y, *, name, age):
    print(a, b, c, x, y, name, age)


f(1, 2, 3, 4, 5, name="Mg Mg", age=10)
f(1, 2, 3, x=4, y=5, name="Mg Mg", age=10)
f(1, 2, 3, 4, y=5, name="Mg Mg", age=10)

##########################################

Understanding other functions

(a, b, c, /, x, y, *, name, age)

Step.1   ->  check parameter list (/, *)
Step.2   ->  divide

a, b, c      ->   F1
x, y         ->   F1, F2, F3
name, age    ->   F2

##########################################

5. No.3 + No.4 + No.2

a, b, c     --->   F1                    No.3
name, age   --->   F2                    No.4
country     --->   F2 ("Myanmar")        No.4 + No.2


def f(a, b, c, /, *, name, age, country="Myanmar"):
    print(a, b, c, name, age, country)


f(1, 2, 3, name="Mg Mg", age=10, country="England")
f(1, 2, 3, name="Mg Mg", age=10)

##########################################

6. No.5

variable length + simple data

m1   60 + 70 + 65
m2   60 + 70 + 65 + 70 + 68
m3   ...


def add(*x):
    ans = 0
    for number in x:
        ans += number
    print(ans)


add(60, 70, 65)
add(60, 70, 65, 70, 68)
add()


##########################################

7. No.6

variable length + complicated data


def info(**x):
    print(x)


info()
info(name="abc", age=10, weight = 20)

##########################################

8. No.3 + No.6

at least 3 values by pos
and more items


def f(a, b, c, /, **x):
    print(a, b, c, x)


f(1, 2, 3)
f(1, 2, 3, name="Mg Mg", age=10)

##########################################

9. No.3 + No.5

at least 3 values by pos
and more values


def f(a, b, c, /, *x):
    print(a, b, c)
    print(x)


f(1, 2, 3)
f(1, 2, 3, 4, 5, 6)

##########################################

10. No.4 + No.6


at least 2 values by name
and more items


def f(*, user_name, password, **x):
    print(user_name, password)
    print(x)


f(user_name="Mg Mg", password="12345")
f(user_name="Mg Mg", password="12345", gender="Male")

##########################################

11.

at least 3 values by pos
and more values

at least 2 values by name
and more items


def f(a, b, c, /, *t, user_name, password, **d):
    print(a, b, c)
    print(t)
    print(user_name, password)
    print(d)


f(1, 2, 3, 4, 5, 6, user_name="Mg Mg", password="12345", gender="Male", age=10)

##########################################

12. Unlimited function (No.5 + No.6)

all values, all items, all forms
variable length of values, variable length of items, (F1, F2, F3)


def f(*args, **kw):
    print(args)
    print(kw)
    print("-"* 42)


f()

f(1)
f(1, 2, 3)

f(age=10)
f(age=10, weight=20, name="Mg Mg")

f(1, 2, 3, age=10, weight=20, name="Mg Mg")

##########################################

13. No.5 + No.4

at least 2 values by name
and more values


def f(*args, name, password):
    print(args)
    print(name, password)


f(1, 2, 3, 4, "Mg Mg", 12345, name="abc", password=1234)

##########################################

*x   positional values, positional arguments    (args)
**y  keyword values, keyword arguments          (kw, kwargs)

####################################################################################

value passed by function        <--   argument
other value                     <--   value

##########################################

Arguments(7)

1. Positional arguments
2. Keyword arguments
3. Default arguments
4. Positional only arguments
5. Keyword only arguments
6. Arbitrary positional arguments
7. Arbitrary keyword arguments

##########################################

Positional arguments                  No.1
Positional only arguments             No.3
Arbitrary positional arguments        No.5

##########################################

Function (10)

1. Introduction
   - print(), input(), len(), int(input())
   - Function call =>  print, print()
   - Why?
     - Readability, reuse
     - Decomposition
   - Where?
     1. built-in module
     2. preinstalled module  tkinter.py, math.py
     3. external module      PyQt5, numpy

2. module, package, framwork
   - function (collection of program)         (one purpose - add(), sqrt() )
   - module   (file)   (collection of fun)    (one work - math.py, login.py)
   - package  (folder) (collection of module) (one group - frontend folder)
   - framework(folder) (collection of package)(one project - Django)

3. Function name
   - naming rules
   - same name (last one)
   - should not give the same name

4. Parameterized function
   - parameterized function   => def add(x, y):
   - parameter list           => (x, y), tuple
   - first parameter          => x

5. Arguments(7)
   - value passed by function
   - positional argument  =>  add(1, 2)
   - keyword argument     =>  add(x=1, y=2)
   - ...

6. Local, Global, Built-in
   Local          => local
   Global         => all (local file)
   Built-in       => all file

7. Standrd form(3)

8. Types of parameters(6)

9. Passing correct values to function

10. Checking Parameters


##########################################

Decomposition

     .    .
   X .    .
 ----------------
     . X  .
 ----------------
     .    .  X
     .    .


Board
draw X
draw O
check win
check tie
marks

##########################################

Passing correct values to function

a = 20
b = 10
c = 30
args = (1000, 700, 1100)
user_name = "Mg Mg"
password  = "12345"
kw        = {country: "Myanmar", "age": 10}


def f(a, b, c, /, *args, user_name, password, **kw):
    print(a, b, c)
    print(args)
    print(user_name, password)
    print(kw)


f(20, 10, 30, 1000, 700, 1100, user_name="Mg Mg", password="12345", country="Myanmar", age=10)

##########################################

Checking Parameters

No.5 + No.2
help(print)   =>   def print(*args, sep=' ', end='\n', file=None, flush=False):

No.2 + No.3
help(input)   =>   def input(prompt='', /):

No.3
help(len)     =>   def len(obj, /):

####################################################################################

Function
1. Function define      =>   def
2. Function name        =>   add
3. Parameter list       =>   ()
4. Parameters           =>   n1, n2
5. Code block           =>   :
6. Documentation string =>   triple quotes (help, doc)
7. Function body        =>   programs , ans = n1 + n2
8. return statement     =>   stop, return value

help()
1. Function name
2. Parameter list
3. documentation string  (__doc__)

9. Types of function
10. Pure function
11. Exercises

################################################


def add(n1, n2):
    '''documentation string'''
    ans = n1 + n2
    return ans


################################################

Types of function
1. effect only function    =>  difference_update()
2. result only function    =>  difference()
3. effect and result       =>  pop()

################################################

pop()
effect = Remove item at index
result = removed item

Remove and return item at index (default last).

------------------------------------------

difference()
effect = -
result = a new set

Return the difference of two or more sets as a new set.
(i.e. all elements that are in this set but not the others.)

------------------------------------------

difference_update()
effect = Remove all elements of another set from this set.
result = -

Remove all elements of another set from this set.

------------------------------------------

len()
effect =
result = the number of items in a container

Return the number of items in a container.

################################################

Pure function (result only function)

Three steps of function


def celsius_fahrenheit(celsius):
    fahrenheit = (celsius * 9 / 5) + 32
    print(fahrenheit)


def celsius_fahrenheit(celsius):
    fahrenheit = (celsius * 9 / 5) + 32
    return fahrenheit


def celsius_fahrenheit(celsius):
    return (celsius * 9 / 5) + 32

------------------------------------------

No         Date             Temperature(C)     Fahrenheit
1     1.1.2024(6:00)               27          80.6
2     1.1.2024(12:00)              30          86.0
3     1.1.2024(22:00)              29          84.2

------------------------------------------

import pandas


def celsius_fahrenheit(celsius):
    return (celsius * 9 / 5) + 32


t = pandas.read_excel("tt_2024.xlsx")
c = list(t["Temperature(C)"])         # [27, 30, 29]
f = []

for celsius in c:
    f.append(celsius_fahrenheit(celsius))

t["Fahrenheit"] = f
t.to_excel("group6_7.xlsx")

################################################################################################

Exercises

1. is_even (တန်ဖိုးတစ်ခုခုကို 2 နဲ့စားလို့ အကြွင်း 0 ရရင် စုံကိန်းဖြစ်ပါတယ်။)( n % 2 == 0)

------------------------------------------

2. is_odd (တန်ဖိုးတစ်ခုခုကို 2 နဲ့စားလို့ အကြွင်း 1 ရရင် မကိန်းဖြစ်ပါတယ်။) ( n % 2 == 1 )

------------------------------------------

3. is_number (0 1 2 3 4 5 6 7 8 9 စတာတွေဟာ နံပါတ်တွေဖြစ်ကြပါတယ်။) ( c in "0123456789" )

------------------------------------------

is_alphabet (a to z တွေနဲ့ ကကြီး ခကွေးလိုမျိုးတွေက အက္ခရာဖြစ်ပါတယ်။)

4. English alphabet

------------------------------------------

5. English alphabet + Myanmar alphabet by unicode

------------------------------------------

6. Myanmar alphabet

------------------------------------------

7. palindrome (နောက်ပြန်ဖတ်လျှင်လည်း ထပ်တူညီသော စကား) eg. madam ( str == str[::-1] )

------------------------------------------

8. greater number (ပိုကြီးတဲ့ နံပါတ်) ( n1 > n2 )

------------------------------------------

9. less number ( n1 < n2 )

------------------------------------------

################################################################################################


1. is_even (တန်ဖိုးတစ်ခုခုကို 2 နဲ့စားလို့ အကြွင်း 0 ရရင် စုံကိန်းဖြစ်ပါတယ်။)( n % 2 == 0)


def is_even(n):
    return n % 2 == 0


------------------------------------------

2. is_odd (တန်ဖိုးတစ်ခုခုကို 2 နဲ့စားလို့ အကြွင်း 1 ရရင် မကိန်းဖြစ်ပါတယ်။) ( n % 2 == 1 )


def is_odd(n):
    return n % 2 == 1


------------------------------------------

def is_even(n):
    return n % 2 == 0


numbers = [100, 105, 3, 9, 1000, 4, 8, 6]
even = []

for number in numbers:
    if is_even(number):
        even.append(number)

print(even)

------------------------------------------

3. is_number (0 1 2 3 4 5 6 7 8 9 စတာတွေဟာ နံပါတ်တွေဖြစ်ကြပါတယ်။) ( c in "0123456789" )

"a"
"6"


def is_number(c):
    return c in "0123456789"


------------------------------------------


def is_number(c):
    return c in "0123456789"


x = '''whgfjew dhu 38dhgjhwgd 383djcgw c8'''
n = 0

for c in x:
    if is_number(c):
        print(f"We found {c}")
        n += 1

print(n)

------------------------------------------

is_alphabet (a to z တွေနဲ့ ကကြီး ခကွေးလိုမျိုးတွေက အက္ခရာဖြစ်ပါတယ်။)

4. English alphabet, English alphabet by ordinal number


def is_alphabet(c):
    return c in "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"


def is_alphabet(c):
    return ord(c) in list(range(65, 91)) + list(range(97, 123))

------------------------------------------

[65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122]

------------------------------------------

5. English alphabet + Myanmar alphabet by ordinal number


def is_alphabet(c):
    return ord(c) in list(range(65, 91)) + list(range(97, 123)) + list(range(4096, 4130))


------------------------------------------

A = 65
Z = 90

a = 97
z = 122

က = 4096
အ = 4129

[65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 4096, 4097, 4098, 4099, 4100, 4101, 4102, 4103, 4104, 4105, 4106, 4107, 4108, 4109, 4110, 4111, 4112, 4113, 4114, 4115, 4116, 4117, 4118, 4119, 4120, 4121, 4122, 4123, 4124, 4125, 4126, 4127, 4128, 4129]

------------------------------------------

6. Myanmar alphabet


def is_alphabet(c):
    return ord(c) in list(range(4096, 4130))


------------------------------------------

7. palindrome (နောက်ပြန်ဖတ်လျှင်လည်း ထပ်တူညီသော စကား) eg. madam ( str == str[::-1] )


def palindrome(s):
    return s == s[::-1]


------------------------------------------

8. greater number (ပိုကြီးတဲ့ နံပါတ်) ( n1 > n2 )


def greater_number(n1, n2):
    if n1 > n2:
        return n1
    else:
        return n2


------------------------------------------

9. less number ( n1 < n2 )


def less_number(n1, n2):
    if n1 < n2:
        return n1
    else:
        return n2


------------------------------------------

"Three steps of greater number"

greater_number(2, 1)   =>  2      <-- n1           1sec    1    1
greater_number(1, 2)   =>  2      <-- n2           2       2    1
greater_number(2, 2)   =>  2      <-- n1 or n2     3       2    1


def greater_number(n1, n2):
    if n1 > n2:
        return n1
    elif n2 > n1:
        return n2
    elif n1 == n2:
        return n2


def greater_number(n1, n2):
    if n1 > n2:
        return n1
    elif n2 > n1:
        return n2
    else:
        return n2


def greater_number(n1, n2):
    if n1 > n2:
        return n1
    else:
        return n2

------------------------------------------

"""
