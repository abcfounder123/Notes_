
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

14. If mark is greater than 40 or mark is equal to 40, exam pass.                          or
15. If username is equal to "Mg Mg" and password is equal to "12345", login successful.    and
16. if full water, Motor Stop.
17. if not full water, Motor ON.                                                           not

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


                 90350 seconds                60         = 1 days 1 hours 5 minutes and 50 seconds
      
        1505 minutes   +   50 seconds         60

  25 hours + 5 minutes                        24

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
17. if not full water, Motor ON.                                                           not

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
"""
