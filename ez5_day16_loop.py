
"""

Looping

1. Iteration (meaningful name)
2. Looping ( underscore )
3. Nested loop for 2D data
4. for + range (to reduce memory consumption)
5. Checking iteration and loop 
6. for + indexing 
7. for + indexing by total length
8. Search all (for + if)
9. Search first element (for + if + break)
10. Search all °C, search all °F, search all Hg
11. Search °C    =>   x[i] == "°" and x[i+1] == "C"
12. Search by positive indexing (left to right and right to left) 
13. Search by negative indexing (left to right and right to left)         
14. Search and count ( for + if + count )
15. Search 3 values ( for + if + count + break )
16. Search by iteration Vs search by indexing
17. Definite Looping and Indefinite Looping
18. Controlling while loop by condition
19. while Vs if
20. login count 5  => wait 24 hours + stop
21. login count 5 and password wrong => wait 24 hours + stop
22. Search value of temperature by fixed position ( while + count )
23. Search value of temperature ( 10 + 22 ) (search all °C + Search value of temperature by fixed position)
23.1. Search all values of °C   ( for + if + while + count )
23.2. Search 3 values of °C   ( for + if + while + count + break )
24. Control flow (while, if, for)

################################################ 

1. Iteration (meaningful name)

x = "Temperature 100°C." # 18

for c in x:
    print(c)
    
    
fruits = ["apple", "banana", "orange"]

for fruit in fruits:
    print(fruit)


numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

for number in numbers:
    print(number)

################################################

2. Looping ( underscore )
       
for _ in range(10):
    print("ha ha")    

################################################ 

2. Nested loop


fruits = ["apple", "banana", "orange"]

for fruit in fruits: # "apple"
    print(fruit)
    for c in fruit:
        print(c)
        

yearly_marks = [[75, 78, 80], [76, 80, 85], [70, 73, 85]]

for monthly_marks in yearly_marks:
    print(monthly_marks)
    for mark in monthly_marks:
        print(mark)

################################################

2D data


yearly_marks.xlsh

myanmar   english    math

   75       78        80
   76       80        85
   70       73        85
   

myan of m1 = row, col = 0, 0  
eng of m2 = row, col = 1, 1  
eng of m3 = row, col = 2, 1   

yearly_marks = [
    [75, 78, 80], 
    [76, 80, 85], 
    [70, 73, 85]
]

################################################ 

3. Nested loop for 2D data

yearly_marks = [
    [75, 78, 80],
    [76, 80, 85],
    [70, 73, 85]
]

for monthly_marks in yearly_marks: # row1
    for mark in monthly_marks: # col1, col2, col3
        print(mark)
        
################################################ 

4. for + range (to reduce memory consumption)

numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for number in numbers:
    print(number)

for number in range(0, 11, 1):
    print(number)

for number in range(11):
    print(number)

################################################

memory consumption

numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

list ->  1             50 bytes
int  -> 11             330 bytes
330 + 50
if one million integer, 30 MB  + 50 bytes

range(11) -> 1         50 bytes
int       -> 1         30 bytes
if one million integer, 50 to 80 bytes

################################################

5. Checking iteration and loop 

for n in range(100):
    pass

for _ in range(100):
    pass
    
################################################

6. for + indexing

x = "Temperature 100°C."  # 18 => positive index => 0 to 17

for i in range(18):
    print(x[i])
    
################################################ 
    
7. for + indexing by total length

x = "Temperature 100°C."

for i in range(len(x)):
    print(x[i])
   
################################################ 

iteration

for c in x:
    print(c)
    
################################################ 
   
indexing

print(x[0])
print(x[1])
print(x[2])
print(x[3])
print(x[4])
print(x[5])

################################################ 

for + indexing

for i in range(18):
    print(x[i])
    
################################################ 
       
for + indexing by total length
    
for i in range(len(x)):
    print(x[i])

################################################ 

8. Search all (for + if)

x = "Te°mpera°ture 100°C.I want Fahrenheit."

for i in range(len(x)):
    if x[i] == "°":
        print(f"index of '°' = {i}")

################################################ 

index of '°' = 2
index of '°' = 8
index of '°' = 17

################################################ 

9. Search first element (for + if + break)
        
x = "Te°mpera°ture 100°C.I want Fahrenheit."

for i in range(len(x)):
    if x[i] == "°":
        print(f"index of '°' = {i}")
        break

################################################ 

index of '°' = 2

################################################ 

10. search all °C, search all °F, search all Hg

x = "TempeHgrature 100°C.I want Hg Fahrenheit.100°F 100°C Hg100°C 100°F"

for i in range(len(x)):
    if x[i] == "°" and x[i+1] == "C":
        print(f"index of '°C' = {i}")

################################################ 

11. search °C    =>   x[i] == "°" and x[i+1] == "C"

x = "Temperature 100°C.I want Fahrenheit."

for i in range(len(x)):
    if x[i] == "°" and x[i+1] == "C":
        print(f"index of '°C' = {i}")
        break
        
################################################ 

12. search by positive indexing (left to right and right to left) 
 
search left to right by indexing  => 0 to t-1           => range(t)

index of '°C' = 17
index of '°C' = 50
index of '°C' = 58


search right to left by indexing  => t-1 to 0           => range(t-1, -1, -1)

index of '°C' = 58
index of '°C' = 50
index of '°C' = 17

x = "TempeHgrature 100°C.I want Hg Fahrenheit.100°F 100°C Hg100°C 100°F"
t = len(x)

for i in range(t-1, -1, -1):
    if x[i] == "°" and x[i+1] == "C":
        print(f"index of '°C' = {i}")
        
        
################################################ 

13. search by negative indexing (left to right and right to left) 

Exercises

search left to right by negative indexing  => -t to -1           => range()

search right to left by negative indexing  => -1 to -t           => range()
        
################################################ 

14. search and count ( for + if + count )

n = 0
n += 1

################################################ 

x = "100°C 100°C Temperature 100°C.I want 100°C Fahrenheit.100°C 100°C"
n = 0

for i in range(len(x)):
    print(i, x[i])
    if x[i] == "°" and x[i+1] == "C":
        print("We found °C at", i)
        n += 1

print("total count =", n)

################################################ 

15. search 3 values ( for + if + count + break )

for + if   <= search

n = 0
n += 1     <= count

if n == 3:
    break

################################################ 

Stop after count

x = "100°C 100°C Temperature 100°C.I want 100°C Fahrenheit.100°C 100°C"
n = 0

for i in range(len(x)):
    print(i, x[i])

    if x[i] == "°" and x[i+1] == "C":
        print("We found °C at", i)
        n += 1
        if n == 3: 
            break     
        # ...
        # ...

print("total count =", n)

################################################

Stop later

x = "TempeHgrature 100°C.I want Hg Fahrenheit.100°F 100°C Hg100°C 100°F 100°C 100°C 100°C"
t = len(x)
n = 0

for i in range(t):
    if x[i] == "°" and x[i+1] == "C":
        print(f"index of '°C' = {i}")
        n += 1
        # ...
        # ...
    if n == 3:
        break
        
print("total count =", n)

################################################ 

16. search by iteration Vs search by indexing 

search by iteration

s = "I go to school by bycicle."
n = 0

for c in s:
    if c in "aeiouAEIOU":
        n += 1

print(n)

################################################ 

search by indexing

s = "I go to school by bycicle."
n = 0

for i in range(len(s)):
    if s[i] in "aeiouAEIOU":
        n += 1

print(n)

################################################ 

s = "I go to school by bycicle."
n = 0

for i in range(len(s)):
    if s[i] in "aeiouAEIOU":
        print(f"index of {s[i]} = {i} ")
        n += 1

print(n)

################################################ 

index of I = 0 
index of o = 3 
index of o = 6 
index of o = 11 
index of o = 12 
index of i = 21 
index of e = 24 
7

################################################

17. Definite Looping and Indefinite Looping

Looping
- for
  - Iteration
  - Definite Looping    ( interest of 5 years => 5 )
  
- while (True)
  - Indefinite Looping  ( login ) (1, 2, 5) 
  
################################################
  
18. Controlling while loop by condition

condition = True

while condition:

    user_name = input("User name = ")
    password = input("Password = ")

    if user_name == "Mg Mg" and password == "123456":
        print("Facebook account of Mg Mg is opened.")
        condition = False

################################################

19. while Vs if

if True: once and stop

while True: once + once + ....when false, stop

################################################

20. login count 5  => wait 24 hours + stop

Login count is indefinite looping.
Maximum chances is 5 times.

################################################

condition = True
n = 0

while condition:

    user_name = input("User name = ")
    password = input("Password = ")

    if user_name == "Mg Mg" and password == "123456":
        print("Facebook account of Mg Mg is opened.")
        condition = False

    n += 1
    if n == 5: #  if count 5 , wait 24 hours + stop 
        print("wait 24 hours.")
        break
        
################################################        

21. login count 5 and password wrong => wait 24 hours + stop

condition = True
n = 0

while condition:

    user_name = input("User name = ")
    password = input("Password = ")

    if user_name == "Mg Mg" and password == "123456":
        print("Facebook account of Mg Mg is opened.")
        condition = False

    n += 1
    if n == 5 and condition: #  if count 5 and wrong, wait 24 hours + stop 
        print("wait 24 hours.")
        break

################################################

22. Search value of temperature by fixed position ( while + count )

x = "Temperature 120°C."
fixed position = 15
14 = "0"
13 = "2"
12 = "1"
11 = " "
 
temperature = ""
"0" + temperature  => "0"
"2" + temperature  => "20"
"1" + temperature  => "120"

################################################

x = "Temperature 6.5°C."
p = 15
n = 1
temperature = ""

while x[p-n] in "0123456789.":  # x[14] => 0, x[13] => 2 , x[12] => 1, x[12] => " "
    temperature = x[p-n] + temperature    # "0" + "" => "0" , "2"  + "0"  => "20" , "1" + "20" =>  "120"
    n += 1

print(temperature)

################################################

23. Search value of temperature ( 10 + 22 ) (search all °C + Search value of temperature by fixed position)

23.1. Search all values of °C   ( for + if + while + count )

x = "Temperature 120°C.Temperature 36°C.Temperature 41.5°C.Temperature 120°C.Temperature 36°C.Temperature 41.5°C."

for i in range(len(x)):
    if x[i] == "°" and x[i+1] == "C":
        # print(i)
        p = i
        n = 1
        temperature = ""

        while x[p - n] in "0123456789.":
            temperature = x[p - n] + temperature
            n += 1

        print(temperature)


################################################

23.2. Search 3 values of °C   ( for + if + while + count + break )

x = "Temperature 120°C.Temperature 36°C.Temperature 41.5°C.Temperature 120°C.Temperature 36°C.Temperature 41.5°C."
count = 0

for i in range(len(x)):
    if x[i] == "°" and x[i+1] == "C":
        # print(i)
        p = i
        n = 1
        temperature = ""

        while x[p - n] in "0123456789.":
            temperature = x[p - n] + temperature
            n += 1

        print(temperature)
        count += 1
        # ...
        # ...

    if count == 3:
        break
        
################################################################################################

24. Control flow (while, if, for)

################################################################################################

"""
