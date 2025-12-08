
"""

1. CLI
2. character code
3. single line string, preformatted string, multiline string, documentation string
4. square root ( exponent 1/2 ), cube root ( exponent 1/3 ) 
5. unicode, uppercase to lowercase  ( A to a )
6. Algorithms, pseudo code
7. CLI 35

################################################

CLI ( Command Line Interface )

GUI

2000 * 1000 = 2_000_000

. . . . .
. . . . .
. . . . .
. . . . .
. . . . .


x
      .             .
        .         .
           .   .
             .
          .    .
        .        .
      .            .
                                     
                                                    
################################################

1. Basic input & output (str)
   - input -> prompt letter
   - print -> comma

################################################

x = int(input())

x           label
=           assignment operator 14
int()       integer
input()     receive input string

################################################

2. format(f)

f"Name = {name:fatr}."

################################################

3. character code (u0041, u000a, u0009)
   - 'select the new line' character = 10, u000a, n
   - select the tab = t  (4 space)   =  9, u0009, t
   
print("applebanana")
print("apple\u000abanana") 
print("apple\nbanana")   

y = "\nAge = 20\n\tName = Mg Mg\n\t\tMarks = 100\n\t\t\tRoll No = 1"
print(y)  

################################################

'''
Age = 20
    Name = Mg Mg
        Marks = 100
            Roll No = 1
'''

################################################

4. single line string 
   - single quotes, double quotes
   - 'appple', "apple"

################################################

5. preformatted string 
6. multiline string  
7. documentation string
   - triple quotes (can encode new lines & tabs)

################################################

8. square root ( exponent 1/2 )   

4 ** 2 
4 * 4 
16


16 ** (1/2)
4

square root of 16 = 4

################################################

9. cube root ( exponent 1/3 ) 

4 ** 3
4 * 4 * 4
64

64 ** (1/3)
4

cube root of 64 = 4

################################################

10. Sequence

Ohm’s Law (Voltage, Current, Resistance)( V = IR )

V = I * R
I = V / R
R = V / I

r = float(input("Resistance = "))
i = float(input("Current = "))
v = i * r

print(f"Voltage = {v}")

print(f"Voltage = {float(input("Current = ")) * float(input("Resistance = "))}")

################################################

1. input("Current = ")
2. float()
3. input("Resistance = ") 
4. float()
5. mul()
6. format() 
7. print() 

################################################

1. input
2. float
3. assign
4. input
5. float
6. assign
7. mul
8. assign
9. format
10. print

################################################

11. unicode

65       A
97       a
4096     က

################################################

12. character to unicode number (ord(က) -> 4096)
    - ordinal unicode number of a character (ord)

13. unicode number to character (chr(4096) -> က)
    - unicode character (chr) 

################################################

14. uppercase to lowercase  ( A to a )

- unicode of A          65
- unicode of A + 32     97
- unicode number of 'a' to character

"A"  ->  65  + 32  -> 97  ->  "a"

c = input("Upper case character = ")
l = chr(ord(c) + 32)
print(f"Lower case character = {l}")

################################################

15. Algorithms 

Algorithm for uppercase to lowercase 
- add 32

Algorithm for lowercase to uppercase
- minus 32

################################################

16. pseudo code

1. unicode of uppercase   
2. unicode of uppercase + 32    
3. unicode number of lowercase to character

################################################

uppercase = ord(input("uppercase = ")) # A   ->  65
lowercase = chr(uppercase + 32)        # 97  ->  a
print("lowercase =", lowercase)

################################################

Algorithm for lowercase to uppercase ( -32 )

- unicode of lowercase   
- unicode of lowercase - 32    
- unicode number of uppercase to character

lowercase = ord(input("lowercase = ")) # a   ->  97
uppercase = chr(lowercase - 32)        # 65  ->  A
print("uppercase =", uppercase)

################################################

Algorithm for A to  က ( + 4031 )

65 to 4096  

################################################################################################

CLI (35)

1. Water Intake Calculator

weight = float(input("Enter your weight in kg: "))
min = weight * 0.033
max = weight * 0.050
print(f"You should drink from {min:.2f} liters to {max:.2f} litres.")

1 kg = 2.2 lb       ( lb = kg * 2.2 )    ( kg = lb / 2.2 )
1 lb = 0.4535 kg    ( kg = lb x 0.4535 ) ( lb = kg / 0.4535 ) 

################################################

2. Area of the circle ( pi.r**2 )

r = float(input("Enter radius: "))
area = 3.14159 * r ** 2
print("Area of the circle:", area)               

################################################

3.Area of triangle ( 1/2.b.h) (05.b.h)

base = float(input("Enter base: "))
height = float(input("Enter height: "))
area = 0.5 * base * height
print("Area of triangle:", area)

################################################

4. Hypotenuse ( c**2 = a**2 + b**2 )  ( c**(2/1) = a**2 + b**2 ) ( c = (a**2 + b**2) ** (1/2) )


|\
| \ c
|b \
|...\
  a
  
c2 = 16
c = 16 ** (1/2) = 4
  
  
16 ** 1/2
16 / 2
8

16 ** (1/2)
16 ** 0.5
4.0

a = float(input("Enter first side: "))
b = float(input("Enter second side: "))
h = (a ** 2 + b ** 2) ** (1/2)
print("Hypotenuse:", h)

################################################

5. Ohm’s Law (Voltage, Current, Resistance)( V = IR ) ( I = V/R ) ( R = V/I )

voltage = float(input("Enter voltage (V): "))
resistance = float(input("Enter resistance (Ω): "))
current = voltage / resistance
print("Current:", current, "A")

################################################

6. Speed ( s = d / t )

3m + 3m + 3m + .. = 30m

speed = 3m/s
time = 10 seconds
distance = ? = 3m/s * 10s = 30m
d = s * t

10 sec, 30m, s=?
30 / 10, d/t 

distance = float(input("Enter distance (m): "))
time = float(input("Enter time (s): "))
speed = distance / time
print("Speed:", speed, "m/s")

################################################

7. Force (Newton's Second Law) ( F = ma )

mass = float(input("Enter mass (kg): "))
acceleration = float(input("Enter acceleration (m/s²): "))
f = mass * acceleration
print("Force:", f, "N")

################################################

initial_amount = 600 g
half_life = 1000 years

3000 years = ? 
1000 years     ->  300 g       / 2
1000 years     ->  150 g       / 2
1000 years     ->   75 g       / 2

n = ?  
>> total / half_life
>> 3000 / 1000 
>> 3

600 / 2 
>> 600 * 1/2
>> 600 * 0.5

>>   ((600 / 2) / 2 ) / 2 
>>   600 * 0.5 * 0.5 * 0.5 
>>   600 * 0.5 ** n 
>>   75 g

initial_amount = 600 g
half_life = 1000 years
total = 10000 years

>> initial_amount * 0.5 ** n 
>> 600 * 0.5 ** 10


8. Half-Life Calculator ( NO * 0.5 ** (time / half_life) )

initial_amount = float(input("Enter initial amount(g): "))
half_life = float(input("Enter half-life (years): "))  # 4.468e9 ( e9 = 1_000_000_000 )
time = float(input("Enter elapsed time (years): "))  # 4_000_000_000
ans = initial_amount * 0.5 ** (time / half_life)
print("Remaining amount:", ans)

################################################

9. Character to ASCII Code / unicode( က )

char = input("Enter a character: ")
print("ASCII Code:", ord(char))

################################################

10. ASCII Code to Character

ascii_code = int(input("Enter an ASCII code: "))
print("Character:", chr(ascii_code))

################################################

11. decimal to bin, oct, hex

decimal = int(input("Enter a decimal number: "))
print("Binary:", bin(decimal))
print("Octal:", oct(decimal))
print("Hexadecimal:", hex(decimal))

################################################

12. bin, oct, hex  to decimal ( without code No )  "0011"

int -> d = ?

d = 10 -> d = 10
b = 10 -> d =  2
o = 10 -> d =  8
x = 10 -> d = 16

d = int("10", base=10)
b = int("10", base=2)
o = int("10", base=8)
x = int("10", base=16)


binary = input("Enter a binary number: ")
print("Decimal:", int(binary, 2))

oct = input("Enter a octal number: ")
print("Decimal:", int(oct, 8))

hex = input("Enter a hexadecimal number: ")
print("Decimal:", int(hex, 16))

################################################

13. bin, oct, hex  to decimal ( with code No )  

"0b1010"  
-> 0b, 1010 
-> base = 2

binary = input("Enter a binary number: ")
print("Decimal:", int(binary, base=0))

oct = input("Enter a octal number: ")
print("Decimal:", int(oct, base=0))

hex = input("Enter a hexadecimal number: ")
print("Decimal:", int(hex, base=0))

################################################

14. Celsius to Fahrenheit

celsius = float(input("Enter temperature in Celsius: "))
fahrenheit = (celsius * 9/5) + 32
ans = f"{celsius} °C is equal to {fahrenheit} °F."
print(ans)

################################################

15. Fahrenheit to Celsius

fahrenheit = float(input("Enter temperature in Fahrenheit: "))
celsius = (fahrenheit - 32) * 5/9
print(f"{fahrenheit}°F is equal to {celsius}°C")

################################################

16. Temperature Converter (Celsius to Kelvin)

celsius = float(input("Enter temperature in Celsius: "))
kelvin = celsius + 273.15
print(f"{celsius}°C is equal to {kelvin:.2f}K")

################################################

1km = 0.621371 miles
- miles = km * 0.621371
- km = miles / 0.621371

1 miles = 1.609 km
- km = miles * 1.609
- miles = km / 1.609

17. Kilometers to Miles       ( 1km = 0.621371 miles )   

km = float(input("Enter distance in kilometers: "))
miles = km * 0.621371
print(f"{km} km is equal to {miles} miles")

################################################

18. Miles to Kilometers    

miles = float(input("Enter distance in miles: "))
km = miles / 0.621371
print(f"{miles} miles is equal to {km} km")

################################################

19. Kilograms to Pounds   ( 1 kg = 2.20462 lb ) ( 1 lb = 0.454 kg )

kg = float(input("Enter weight in kilograms: "))
pounds = kg * 2.20462
print(f"{kg} kg is equal to {pounds} pounds")

################################################

20. Pounds to Kilograms

pounds = float(input("Enter weight in pounds: "))
kg = pounds / 2.20462
print(f"{pounds} pounds is equal to {kg} kg")

################################################

21. Meters to Feet     ( 1m = 3.28084 ft ) ( 1 ft = 0.305 m )

meters = float(input("Enter length in meters: "))
feet = meters * 3.28084
print(f"{meters} meters is equal to {feet} feet")

################################################

22. Feet to Meters

feet = float(input("Enter length in feet: "))
meters = feet / 3.28084
print(f"{feet} feet is equal to {meters} meters")

################################################

23. Seconds to Minutes and Hours

seconds = int(input("Enter time in seconds: "))
minutes = seconds / 60
hours = seconds / 3600
print(f"{seconds} seconds is equal to {minutes:.2f} minutes or {hours:.2f} hours")

################################################

24. Seconds to Seconds, Minutes and Hours   ( 350, 3950)

seconds = int(input("Enter time in seconds: "))
h = seconds // 3600
m = (seconds % 3600) // 60
s = (seconds % 3600) % 60
print(f"{h}:{m}:{s}")

################################################

25. Seconds to Seconds, Minutes, Hours and days ( 90350 )
25  --> 1 + 1

seconds = int(input("Enter time in seconds: "))
h = seconds // 3600
m = (seconds % 3600) // 60
s = (seconds % 3600) % 60
d = h // 24
nh = h % 24
print(f"{d} days and {nh}:{m}:{s}")

################################################

Day. 11

# * rate

26. Currency Converter (USD to MMK)

usd = float(input("Enter amount in USD: "))
exchange_rate = 6000
mmk = usd * exchange_rate
print(f"{usd} USD is equal to {mmk} MMK")

dollar = float(input("Dollar : "))
kyats = dollar * 5000
print(f"{dollar} $ is equal to {kyats:.0f} kyats.")

################################################

27. Currency Converter (Custom Rate)

1 $        -> 5000 kyats
1 kyats    -> 0.0002 $

1 $ -> 40 B
1 B -> 0.025 $

amount = float(input("Enter amount: "))
rate = float(input("Enter exchange rate: "))
converted = amount * rate
print(f"Converted amount: {converted}")

Enter amount: 10000
Enter exchange rate: 0.0002
Converted amount: 2.0

Enter amount: 2
Enter exchange rate: 5000
Converted amount: 10000.0

################################################

28. Step-to-Calorie Converter

1 Step -> 0.04 kilo calorie
1 kcal -> 25 steps

steps = int(input("Enter number of steps taken: "))
calories_burned = steps * 0.04  # Approximation for an average person
print(f"Calories burned: {calories_burned:.0f} kcal")

calories_burned = int(input("Calories burned: "))
steps = calories_burned * 25
print(f"Number of steps : {steps:.0f} steps")

################################################

29. Storage Converter (GB to MB & KB)


b -> kb -> mb -> gb    (1000)(1024)
b -> gb
b
k = e3 = 1000
M = e6 = 1_000_000
G = e9 = 1_000_000_000


gb = float(input("Enter storage in GB: "))
mb = gb * 1000
kb = gb * 1_000_000
print(f"{gb} GB is equal to {mb} MB or {kb} KB")

gb = float(input("Enter storage in GB: "))
mb = gb * 1024  # 2 ** 10  Vs  10 ** 3
kb = mb * 1024
print(f"{gb} GB is equal to {mb} MB or {kb} KB")

################################################

30. Bytes to GB + MB + KB + B
  
                    34_567_891_234 bytes
                    
                  34 GB + 567 MB + 891 KB + 234 B
                                
                    
                    34_567_891_234 bytes

                 34_567_891 KB    +  234 bytes
                 
            34_567 MB + 891 KB 

       34 GB + 567 MB

################################################

31. 

bytes_size = int(input("Enter size in bytes: ")) # 34_567_891_234 bytes

e = 1000

kb = bytes_size // e # 34_567_891 KB
b = bytes_size % e # 234 B

mb = kb // e # 34_567 MB
kb2 = kb % e # 891 KB

gb = mb // e # 34 GB
mb2 = mb % e # 567 MB

print(f"{bytes_size} bytes = {gb} GB {mb2} MB {kb2} KB {b} B")


Enter size in bytes: 34_567_891_234
34567891234 bytes = 34 GB 567 MB 891 KB 234 B

################################################

bytes_size = int(input("Enter size in bytes: ")) # 34_567_891_234 bytes

e = 1024

kb = bytes_size // e 
b = bytes_size % e 

mb = kb // e 
kb2 = kb % e

gb = mb // e
mb2 = mb % e 

print(f"{bytes_size} bytes = {gb} GB {mb2} MB {kb2} KB {b} B")


Enter size in bytes: 34_567_891_234
34567891234 bytes = 32 GB 198 MB 522 KB 290 B

################################################

32.

         12_345_678_900       bytes
         
      12 GB     345_678_900 bytes
         
              345 MB      678_900   bytes
              
                      678 KB     900  bytes
         
 12 GB  345 MB  678 KB  900  bytes


bytes_size = int(input("Enter size in bytes: ")) # 12_345_678_900       bytes

gb = bytes_size // 1e9                       # 12 GB
mb = (bytes_size % 1e9) // 1e6               # 345 MB
kb = ((bytes_size % 1e9) % 1e6) // 1e3       # 678 KB
b = ((bytes_size % 1e9) % 1e6) % 1e3         # 900  bytes

print(f"{gb} GB {mb} MB {kb} KB and {b} bytes")

################################################

bytes_size = int(input("Enter size in bytes: ")) # 12_345_678_900       bytes

gb = bytes_size // (1024 ** 3)                               # 11 GB
mb = (bytes_size % (1024 ** 3)) // (1024 ** 2)               # 509 MB
kb = ((bytes_size % (1024 ** 3)) % (1024 ** 2)) // 1024       # 775 KB
b = ((bytes_size % (1024 ** 3)) % (1024 ** 2)) % 1024         # 52 bytes

print(f"{gb} GB {mb} MB {kb} KB and {b} bytes")

################################################################################################

1. Check Operating System

import platform
import sys
import psutil

print("Operating System:", platform.system()) # mac OS and IOS based on Darwin OS

################################################

2. Check OS Version

import platform
print("OS Version:", platform.version())

################################################

3. Check Machine Type (32-bit or 64-bit)

import platform
print("Machine Type:", platform.architecture()[0])

################################################

4. Check Python Version

import sys
print("Python Version:", sys.version)

################################################

5. Check Total RAM / Available RAM (Memory)

import psutil
ram = psutil.virtual_memory()
total = ram.total / ( 1024 ** 3 )
available = ram.available / ( 1024 ** 3 )
print(f"Total RAM:", total, "GB")
print(f"Available RAM:", available, "GB")

################################################

6. Check CPU Information

import psutil
print("CPU Cores:", psutil.cpu_count(logical=False))        
print("Logical CPUs:", psutil.cpu_count(logical=True))     

################################################

platform
1. system()
2. version()
3. architecture()[0] 

sys
1. version

psutil
1. virtual_memory() -> RAM 
   - total = 8GB
   - available = 3GB 
   
2. cpu_count(logical=False) # man = 2
   cpu_count(logical=True)  # work = 4

################################################

Computer

i5
i7

silicon chip
m1         i7 12 generation
m2
m3
m4
m5

i7    13 seconds      100 m     ( 1 km)
m1    13 seconds      100 m     (40 km)

Server

quantom  aeroplane

################################################

AI

AI    500 millions
D       5 millions

AI      5 millions to  500 millions, data 

quantom  5000 

New AI

################################################################################################   


"""


