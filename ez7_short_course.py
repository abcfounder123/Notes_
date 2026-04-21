
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
5. Variable length positional only Parameters    *name
6. Variable length keyword only Parameters       **name

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

##########################################

"""
