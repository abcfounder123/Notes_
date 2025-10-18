"""
################################################

Procedural Programming
1. Sequences(top to buttom, left to right, parenthesis first)
2. Selection(if, else)
3. Iteration(for, while)
4. Functions

################################################

1.statements
  a.normal statements
  b.conditional statements

2.if, else
  >> can only interact with boolean data type
  a.if       --->   True
  b.else     --->   False
  
################################################

1.statements

a.normal statements

print("a")
print("b")

################################################

b.conditional statements

condition1 = True
condition2 = False

if condition1:print("a")
if condition2:print("b")

################################################
################################################

2.if, else
  >> can only interact with boolean data type
  a.if       --->   True
  b.else     --->   False 
  
################################################

a.if

if True:print("abc")

################################################

b.else

full = False

if full:
    print("Motor OFF")

else:
    print("Motor ON")

################################################################################################

Empty and Somthing

Exercise.1
  
if []: print("abcd")

# 1. list() -> empty list
# 2. bool(empty list) -> False
# 3. if

################################################

if ["apple", "banana"]: print("abcd")

# 1. str
# 2. str
# 3. list() -> list
# 4. bool(list) -> True
# 5. if
# 6. print()

################################################
 
fruits = []

if fruits:
    print("You can buy fruit.")

else:
    print("You can not buy.")


# logical not
if not fruits:
    print("You can not buy.")

else:
    print("You can buy fruit.")
    

1. str
2. str
3. list
4. assignment
5. bool(fruits) -> True
6. if
7. print("You can buy fruit.")

################################################

fruits = []
if fruits:print("You can buy fruit.")
else:print("You can not buy.")

1. list  -> empty list
2. assign
3. bool(empty list) -> False
4. if  close
5. else open
6. print("You can not buy.")

################################################

Exercise.2

# if water level is low, motor open.
# sensor value is somthing.

low_level = 1

if low_level:print("motor open")
else:print("water level is not low")

################################################

# if water level is full, motor off.
# sensor value is somthing.

# full = 1
# if full: print("Motor OFF") 

################################################

normally open ->  
normally close ->

"example of boolean operator"

if sensor value is empty, condition of full_water must be True.
if water is full, water motor must be off.

sensor_value = int(input("sensor value:"))
full = not sensor_value
if full: print("Motor OFF")

###############################################

if sensor value is somthing, condition of full_water must be True.
if water is full, water motor must be off.


sensor_value = int(input("sensor value:"))
full = bool(sensor_value)

if full: print("Motor OFF")

################################################################################################

Temperature Convertor

Equation

fahrenheit = (celsius * 9/5) + 32
celsius = (fahrenheit - 32) * 5 / 9

################################################

p = '''
Temperature Converter
1. Fahrenheit to Celsius 
2. Celsius to Fahrenheit 

>> '''

n = input(p)

if n == '1':
    print("Fahrenheit to Celsius")
    fahrenheit = float(input("Fahrenheit = "))
    celsius = (fahrenheit - 32) * 5 / 9
    print("Celsius =", celsius)

else:
    print("Celsius to Fahrenheit")
    celsius = float(input("Celsius = "))
    fahrenheit = (celsius * 9 / 5) + 32
    print("Fahrenheit =", fahrenheit)

################################################

p = '''
Temperature Converter
1. Fahrenheit to Celsius 
2. Celsius to Fahrenheit 
3. Celsius to Kelvin

>> '''

n = input(p)

if n == '1':
    print("1. Fahrenheit to Celsius")
    fahrenheit = float(input("Fahrenheit = "))
    celsius = (fahrenheit - 32) * 5 / 9
    print("Celsius =", celsius)

if n == '2':
    print("2. Celsius to Fahrenheit")
    celsius = float(input("Celsius = "))
    fahrenheit = (celsius * 9 / 5) + 32
    print("Fahrenheit =", fahrenheit)

if n == '3':
    print("3. Celsius to Kelvin")
    celsius = float(input("Celsius = "))
    kelvin = celsius + 273
    print("Kelvin =", kelvin)
    

################################################
    
p = '''
Temperature Converter

Enter temperature (eg. 100°C, 212°F, 273K) 
>> '''

n = input(p)
symbol = n[-1] # 'C'
t = float(n[:-2]) # '100' -> 100.0

if symbol == "C":
    fahrenheit = (t * 9 / 5) + 32
    print("Fahrenheit =", fahrenheit)

if symbol == "F":
    celsius = (t - 32) * 5 / 9
    print("Celsius =", celsius)

if symbol == "K":
    celsius = float(n[:-1]) - 273
    print("Celsius =", celsius)
    
################################################

input => Temperature is 100°C.I want to know Fahrenheit.
process => ?

################################################

looping, iteration

x = "Temperature 100°C."

for c in x: # c = 'T', c = 'e', c = 'm'
    print(c)
        
################################################

x = ["apple", "banana", 'orange']

for c in x: 
    print(c)
    
################################################
    
nested loop

x = ["apple", "banana", 'orange']

for c in x: # "apple"
    print(c)
    for i in c:
        print(i)

################################################

# for and range

x = [0, 1, 2, 3, 4, 5]

for i in x:
    print(i)

for i in range(0,11):
    print(i)

for i in range(11):
    print(i)
    
################################################

# for and indexing

x = "Temperature 100°C."
l = len(x) # 18 , valid range of index ---> -t to t-1 ---> -18 to 17
print(l)

for i in range(18): # 0, 1, 2, ... 17
    print(x[i])

################################################

# for and indexing by length

x = "Temperature 100°C."

for i in range(len(x)): # 0, 1, 2, ... 17
    print(x[i]) 
    
################################################

# for and break 

x = "Temperature 100°C."


for i in range(len(x)): # 0, 1, 2, ... 17
    print(x[i])
    if x[i] == "°" and x[i+1] == "C":
        print(i)
        break  
        
################################################

# checking digit by ordinal numbers
# isdigit()
# 0 -> 48, 9 -> 57
# print(ord("9"))

text = "The temperature today is 100°C."

for c in text:
    if 48 <= ord(c) and ord(c) <= 57: # 48, 49, 50, . . . 57
        print(f"{c} is a digit.")

################################################

# checking digit by selection          

text = "The temperature today is 100°C."
digits = "0123456789"

for c in text:
    if c in digits:
        print(f"{c} is a digit.")
        print(True)

################################################

# checking digit by function
  
x = '1'
print(x.isdigit())

################################################

# searching index of °C, °F, K


x = "Temperature is 100K and I want °C."
digits = "0123456789"

for i in range(len(x)): # 0, 1, 2, ... 17
    if x[i] == "°" and x[i+1] == "C":
        print("°C =", i)

    if x[i] == "°" and x[i+1] == "F":
        print("°F =", i)
   
    if x[i] == "K" and x[i-1] in digits and (x[i+1] == " " or x[i+1] == "."):
        print("K =", i)

################################################################################################

while loop

while condition:p1

if condition:p1

################################################

# assign value to i

x = "abcdefghijk"


for i in range(11): # 0 to 10
    print(x[i])


i = 0
while i < 11:
    print(x[i])
    i += 1

################################################

for i in range(20, 0, -1): # 20 to 1
    print(i)


i = 20
while i > 0:
    print(i)
    i += -1

################################################

for i in range(20, 1, -2): # 20, 18, 16 to 2
    print(i)


i = 20
while i > 1:
    print(i)
    i += -2
    
################################################
    
for i in range(-20, -1, 2): # -20, -18, -16 to -2
    print(i)


i = -20
while i < -1:
    print(i)
    i += 2
    
################################################   

for i in range(-1, -100, -2): # -1, -3, -5, to -99
    print(i)


i = -1
while i > -100:
    print(i)
    i += -2

################################################

x = "Temperature is 257K and I want °C."

if x[i-1] in digits, "7"
if x[i-2] in digits, "5"
if x[i-3] in digits, "2"
if x[i-4] in digits, break

"7" + "" = "7"
"5" + "7" = "57"
"2" + "5" + "7" = "257"

################################################

# collecting all digit of K

x = " 27383257K."  # K -> 9
digits = "0123456789"

i = 9
ans = ""

while x[i-1] in digits:
    ans = x[i-1] + ans
    i -= 1
    print(ans)
       
################################################
    
# collecting all digit of K (including floating-point number)

x = " 2738325.7K."  # K -> 9
digits = "0123456789"

i = 10
ans = ""

while x[i-1] in digits or x[i-1] == ".":
    ans = x[i-1] + ans
    i -= 1
    print(ans)

################################################

# collecting all from selection --->   "0123456789."

x = " 2738325.7K."  # K -> 9
selection = "0123456789."

i = 10
ans = ""

while x[i-1] in selection:
    ans = x[i-1] + ans
    i -= 1
    print(ans)
    
################################################
    
Temperature is 100.25°C. I want Fahrenheit.
Temperature is 200°C. I want Fahrenheit.
I want Fahrenheit. Temperature is 200°C.
Temperature is 200°C.Fahrenheit=?

################################################

# control flow (while, if, for) 

x = input("Temperature converter \n>> ")

selection = "0123456789."

for i in range(len(x)):  # 0, 1, 2, ... 17
    if x[i] == "°" and x[i + 1] == "C":
        t = ""
        while x[i - 1] in selection:
            t = x[i - 1] + t
            i -= 1
        # print(t)


t = float(t)

if "Fahrenheit" in x:
    fahrenheit = (t * 9 / 5) + 32
    print("Fahrenheit =", fahrenheit)

################################################################################################

# GUI

from tkinter import *

root = Tk()
degree = StringVar(root)
ans = StringVar(root)
selection = "0123456789."


def cal():
    x = degree.get()  # "Temperature is 200°C.Fahrenheit=?"
    for i in range(len(x)):  # 0, 1, 2, ... 17
        if x[i] == "°" and x[i + 1] == "C":
            t = ""
            while x[i - 1] in selection:
                t = x[i - 1] + t
                i -= 1

    t = float(t)
    if "Fahrenheit" in x:
        fahrenheit = (t * 9 / 5) + 32
        f = str(fahrenheit) + " °F"
        ans.set(f)

f = Frame(root, borderwidth=40)
f.pack()
Label(f, text="Enter temperature ( 100°C or 212°F )").pack(side=LEFT)
Entry(f, textvariable=degree).pack(side=LEFT)

Button(root, text="Calculate", command=cal).pack()

f2 = Frame(root, borderwidth=40)
Label(f2, text="Answer  =  ").pack(side=LEFT)
Entry(f2, textvariable=ans).pack(side=LEFT)
f2.pack()

root.mainloop()

################################################################################################

selection
1. if, 
2. else
3. elif  (one from many)

looping
4. while --> conditional loop
5. for   --> prefix loop

################################################################################################

  64K
  64864K
  368264864K 

for   --> prefix
  
x = "  368264864K"

k = x.find("K") # 10
print(x[k-1])
print(x[k-2])
print(x[k-3])
print(x[k-4])
print(x[k-5])
print(x[k-6])
print(x[k-7])
print(x[k-8])
print(x[k-9])

################################################

x = "  368264864K"

k = x.find("K") # 10

for i in range(1, 10): # 1 to 9
    print(x[k-i])  
    
x = "  356364K"

k = x.find("K") # 10

for i in range(1, 7): # 1 2 3 4 5 6, prefix = 6
    print(x[k-i])
    
################################################

4. while --> conditional loop

x = " 454573336343434387890664K"

k = x.find("K") # 7

i = 1
while x[k-i] in "0123456789":
    print(x[k-i])
    i += 1
       
################################################################################################

Exercises ( if, elif, else )

################################################

step.1 (condition -> output)(flow)
- 1101  acjm

################################################

step.2 (output -> condition)(control)
- acjn  1100
- behk
- beg   011
- ad    10
- behl  0100

################################################

step.3 (condition -> new code)
- 1100   - print("new")
- 1111   - if c4:print("new")
- 11111  - c5 = 1; if c5:print("new")
- 0001  
 
if c3:
    pass
else:
    if c4:
        print("new")
          
################################################
        
step.4 (idea -> code) 
- motor ON         

################################################

c1 = 0
c2 = 0
c3 = 0
c4 = 1
c5 = 1

if c1:
    print("a")
    if c2:
        print("c")
        if c3:
            print("i")
            if c4:
                if c5:
                    print("new")


        else:
            print("j")
            if c4:
                print("m")

            else:
                print("n")

    else:
        print("d")

else:
    print("b")
    if c2:
        print("e")
        if c3:
            print("g")

        else:
            print("h")
            if c4:
                print("k")

            else:
                print("l")

    else:
        print("f")
        if c3:
            pass
        else:
            if c4:
                print("new")
                
################################################

1. low   ->   print("water motor ON")
2. full  ->   print("water motor OFF")
                
                
if low_level:
    print("water motor ON")

if full:
    print("water motor OFF")
                
################################################
            
3. low + not short_circuit -> print("water motor ON")                

if low_level:
    if short_circuit:
        pass
    else:
        print("water motor ON")

################################################
                
4. low + electric + short_circuit   -> print("water motor ON")

if low_level:
    if electric:
        if short_circuit:
            pass
        else:
            print("water motor ON")                

################################################

5. low + not electric  -> print("Generator ON")

if low_level:
    if electric:
        if short_circuit:
            pass
        else:
            print("water motor ON")
    else:
        print("Generator ON")

################################################

6. low + not electric + not short_circuit   ->   Generator ON ->   print("water motor ON")

if low_level:
    if electric:
        pass
    else:
        print("Generator ON")
        if short_circuit:
            pass
        else:
            print("water motor.1 ON")

################################################

7. low + electric + short_circuit_1 +  not short_circuit_2     ->   print("water motor.2 ON")
     1      1            1                0

if low_level:
    if electric:
        if short_circuit_1:
            if short_circuit_2:
                pass
            else:
                print("water motor.2 ON")
        else:
            print("water motor.1 ON")
            
################################################

8. low + not electric + short_circuit_1 +  not short_circuit_2     ->   print("water motor.2 ON")

################################################

sensor(2)
- low level       (somthing) (True)
- full            (somthing) (True)
- short circuit   (somthing) (True)

Actuactors
- water motor ON
- water motor OFF

################################################

1. low                                      ->   print("water motor ON")
2. full                                     ->   print("water motor OFF")
3. low + not short_circuit                  ->   print("water motor ON")
4. low + electric + not short_circuit       ->   print("water motor ON")                           110      
5. low + not electric                       ->   print("Generator ON")
6. low + not electric + not short_circuit   ->   Generator ON -> print("water motor ON")           100       
7. low + electric + short_circuit_1 +  not short_circuit_2         ->   print("water motor.2 ON")  1110
8. low + not electric + short_circuit_1 +  not short_circuit_2     ->   print("water motor.2 ON")  1010
9. 1111     ->   print("call mechanic")
10. 1011    ->   print("call mechanic")  
11. 11110   ->   print("water motor.3 ON")
12. 10110   ->   print("water motor.3 ON") 
13. 11111        print("call mechanic")
14. 10111        print("call mechanic")
15. call mechanic for all short_circuit

16. 111110  ->   print("water motor.4 ON")
17. 101110  ->   print("water motor.4 ON")
18. 111111       print("call mechanic")
19. 101111       print("call mechanic")

"0"  is somthing value.

################################################

low_level = input("low_level = ")
electric = input("electric = ")
short_circuit_1 = input("short_circuit_1 = ")
short_circuit_2 = input("short_circuit_2 = ")
short_circuit_3 = input("short_circuit_3 = ")

print()

if low_level:
    if electric:
        if short_circuit_1:
            print("call mechanic")
            if short_circuit_2:
                print("call mechanic")
                if short_circuit_3:
                    print("call mechanic")
                else:
                    print("water motor.3 ON")
            else:
                print("water motor.2 ON")
        else:
            print("water motor.1 ON")
    else:
        print("Generator ON")
        if short_circuit_1:
            print("call mechanic")
            if short_circuit_2:
                print("call mechanic")
                if short_circuit_3:
                    print("call mechanic")
                else:
                    print("water motor.3 ON")
            else:
                print("water motor.2 ON")
        else:
            print("water motor.1 ON")

################################################################################################

one from many (elif -> else + if)

greater or equal 500, doctor
greater  or equal 400, engineer
greater  or equal 300, distance 

c1 = greater or equal 500
c2 = greater or equal 400
c3 = greater or equal 300

c1, doctor
not c1 and c2, engineer
not c1 and not c2 and c3, distance 
not c1 and not c2 and not c3, online shop

################################################

mark = int(input("Mark = "))

c1 = mark >= 500
c2 = mark >= 400
c3 = mark >= 300


if c1:print("doctor")
if not c1 and c2:print("engineer")
if not c1 and not c2 and c3:print("distance")
if not c1 and not c2 and not c3:print("online shop")

################################################

4      <--

1      <--
2
3      <--

################################################

mark = int(input("Mark = "))

c1 = mark >= 500
c2 = mark >= 400
c3 = mark >= 300


if c1:print("doctor")
elif c2:print("engineer")
elif c3:print("distance")
else:print("online shop")

################################################

mark >= 90    A+
mark >= 80    A
mark >= 70    B
mark >= 50    C
mark < 50     fail


c1 = mark >= 90    
c2 = mark >= 80    
c3 = mark >= 70   
c4 = mark >= 50    
c5 = mark < 50     

c1                              A+
not c1, c2                      A
not c1, notc2, c3               B
not c1, notc2, not c3, c4       C

mark < 50     fail

################################################

# Error sample

if c1:print("A+")       <---    c1                                       A+
elif c3:print("B")      <---    not c1 and c3                            B
elif c2:print("A")      <---    not c1 and not c3 and c2                 A
elif c4:print("D")      <---    not c1 and not c3 and not c2 and c4      C
    
mark = int(input("Mark = "))

c1 = mark >= 90
c2 = mark >= 80
c3 = mark >= 70
c4 = mark >= 50

if c1:print("A+")
elif c3:print("B")
elif c2:print("A")
elif c4:print("C")

#############

correct sample

c1                              A+
not c1, c2                      A
not c1, notc2, c3               B
not c1, notc2, not c3, c4       C
not c1, notc2, not c3, not c4   fail


mark = int(input("Mark = "))

c1 = mark >= 90
c2 = mark >= 80
c3 = mark >= 70
c4 = mark >= 50
c5 = mark < 50

if c1:print("A+")
elif c2:print("A")
elif c3:print("B")
elif c4:print("C")
else :print("fail")

# elif c5:print("fail")

################################################

"""
