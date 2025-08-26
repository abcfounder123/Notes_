
"""

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
 
fruits = ["apple", "banana"]
if fruits:print("You can buy fruit.")
else:print("You can not buy.")

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

"example of boolean operator"

if sensor value is empty, condition of full_water must be True.
if water is full, water motor must be off.

sensor_value = int(input("sensor value:"))
full = not sensor_value
if full: print("Motor OFF")

################################################

if sensor value is somthing, condition of full_water must be True.
if water is full, water motor must be off.


sensor_value = int(input("sensor value:"))
full = bool(sensor_value)

if full: print("Motor OFF")

################################################################################################

Temperature Convertor

Equation

fahrenheit = (celsius * 9/5) + 32

(fahrenheit - 32) = celsius * 9/5 
(fahrenheit - 32) * 5 = celsius * 9
(fahrenheit - 32) * 5 / 9 = celsius

celsius = (fahrenheit - 32) * 5 / 9

################################################

if value of n is equal to 1, Celsius to Fahrenheit.
if n == 1, Celsius to Fahrenheit 


if value of n is not equal to 1, Fahrenheit to Celsius.
if n != 1, Celsius to Fahrenheit 

################################################

program quality

if c1:Celsius to Fahrenheit

else: Celsius to Fahrenheit 

################################################

User Interface, User Experiance

"100°C" to F
"212°F" to C

     "100°C"
     
      /   |
    100   °C
    
    
     "100°F"
     
      /   |
    100   °F
    
    
     "373K"
     
      /   |
    373   K
    
    
value = t[:-2] # °C
sign = t[-2:]  # 100

################################################

Celsius to Fahrenheit

celsius = float(input("Enter temperature in Celsius: "))
fahrenheit = (celsius * 9/5) + 32
ans = f"{celsius} °C is equal to {fahrenheit} °F."
print(ans)

################################################

Fahrenheit to Celsius

fahrenheit = float(input("Enter temperature in Fahrenheit: "))
celsius = (fahrenheit - 32) * 5/9
print(f"{fahrenheit}°F is equal to {celsius}°C")

################################################

prompt = '''

              Temperature Convertor Application


Enter your temperature ( 100°C or 212°F ) : '''


t = input(prompt) # "100°C"  "100K"  --> "0K", "10"

sign = t[-2:]  # -2, -1 -> "°C"
value = float(t[:-2]) # '100' -> 100.0


print("-" * 42)

if sign == "°C":
    fahrenheit = (value * 9 / 5) + 32
    ans = f"{value} °C is equal to {fahrenheit} °F."
    print(ans)

elif sign == "°F":
    celsius = (value - 32) * 5 / 9
    print(f"{value}°F is equal to {celsius}°C")

else:
    value = float(t[:-1])
    celsius = value - 273
    print(f"{value} Kelvin  is equal to {celsius}°C")
    
################################################################################################

Step.1 ---> Select

p = '''
            Temperature Convertor
A. Celsius to Fahrenheit 
B. Fahrenheit to Celsius
Please choose A or B: '''

q = input(p)

if q == "A":
    celsius = float(input("Enter temperature in Celsius: "))
    fahrenheit = (celsius * 9 / 5) + 32
    ans = f"{celsius} °C is equal to {fahrenheit} °F."
    print(ans)

else:
    fahrenheit = float(input("Enter temperature in Fahrenheit: "))
    celsius = (fahrenheit - 32) * 5 / 9
    ans = f"{fahrenheit}°F is equal to {celsius}°C"
    print(ans)

################################################

            Temperature Convertor
A. Celsius to Fahrenheit 
B. Fahrenheit to Celsius
Enter your temperature ( 100°C or 212°F ) :  100°C
100.0 °C is equal to 212.0 °F.

            Temperature Convertor
A. Celsius to Fahrenheit 
B. Fahrenheit to Celsius
Enter your temperature ( 100°C or 212°F ) :  212°F
212.0°F is equal to 100.0°C

################################################

Step.2 ---> User Interface, User Experiance

p = '''
            Temperature Convertor

Enter your temperature ( 100°C or 212°F ) :  '''

q = input(p)  # "100°C"

s = q[-1]  # "C"
n = float(q[:-2]) # float("100") -> 100.0

if s == "C":
    fahrenheit = (n * 9 / 5) + 32
    ans = f"{n} °C is equal to {fahrenheit} °F."
    print(ans)

else:
    celsius = (n - 32) * 5 / 9
    ans = f"{n}°F is equal to {celsius}°C"
    print(ans)

################################################

Step.3 --->  adding new feature "K"

from tkinter import *

root = Tk()
degree = StringVar(root)
ans = StringVar(root)


def cal():
    q = degree.get()  # "100°C"
    s = q[-1]
    n = float(q[:-2])  # 100.0
    if s == "C":
        f = str((n * 9 / 5) + 32) + "°F"
        ans.set(f)

    if s == "F":
        c = str((n - 32) * 5 / 9) + "°C"
        ans.set(c)

    if s == "K":
        value = float(q[:-1]) # 373K  --> "100.0" + "C"
        celsius = str(value - 273) + "°C"
        ans.set(celsius)


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


"""
