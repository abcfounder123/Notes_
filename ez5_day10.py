
"""

Day.10

1. Three parts of programmimg 
2. Basic input/output
3. program flow   
4. control flow

################################################

1. Three parts of programmimg
   - input     (mic)(30 35 60 70 90 120) 
   - processing   ( 60 70 )
   - output    (speaker)                 

################################################

2. Basic input/output (str)
   - input(prompt letter)
   - print(,)

################################################

3. program flow 

1. input()       '90350'
2. int()          90350
3. asssign()

4. floor div()
5. asssign()
6. mod()
7. asssign()

8. floor div()
9. asssign()
10. mod()
11. asssign()

12. floor div()
13. asssign()
14. mod()
16. asssign()

17. format()
18. print()

Day
Hour
Min
Sec

################################################

4. control flow 
Sec
Min

################################################

Associativity
- left-sided bind
- right-sided bind (1, 2, 10, 14, 15)(e, u, assignment)

left
2 ** 2 ** 3
4 ** 3
64

right
2 ** 2 ** 3
2 ** 8
256

left
2 / 2 * 3
1.0 * 3
3

right
2 / 2 * 3
2 / 6
3.333

################################################

e, u, assignment

Exponent      -  1
+, -, ~, not  -  4
13 + 1        - 14

                19

################################################

1 ** 2 + 3 * 4 / 5 - 6 ** 1 

1. r **, l **

>> 1 ** 2 + 3 * 4 / 5 - 6
>> 1 + 3 * 4 / 5 - 6

2. l*, r/

>> 1 + 12 / 5 - 6
>> 1 + 2.4 - 6

3. l+, r-

>> 3.4 - 6
>> - 2.6

################################################

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


800 * 600 = 480_000

2000 * 1000 = 2_000_000

500 50
. . . . .       X
. . . . .
. . . . .
. . . . .
. . . . .  5, 5

Y

500

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

x           identifier, label
=           assignment operator 14
int()       integer
input()     receive input string


x = 5

5  -> int house -> (n=5,str='5' + 74) => Mandalay, 4333981320

x  -> house address 

print(x)


################################################

2. format(f)

f"Name = {name:fatr}."

################################################

3. character code (u0041, u000a, u0009)
   - 'select the new line' character = 10, u000a, n
   - select the tab = t  (4 space)   =  9, u0009, t
   
65 66 -> AB
0x41 0x42 -> AB

\u0041\u000a\u0009\u0042\u000a\u0009\u0009\u0043
A\u000a\u0009B\u000a\u0009\u0009C
A\u000a\u0009B\u000a\u0009\u0009C
A\n\tB\n\t\tC
41 a 9 42 a 9 9 43

A
	B
		C

print("A\u000a\u0009B\u000a\u0009\u0009C")
print("A\n\tB\n\t\tC")

################################################################################################

Day.11

encode(A => \u0041) 
decode(\u0041 => A)

################################################

4. single line string 
   - single quotes, double quotes
   - 'appple', "apple"
   - can not encode "new line chr"      --->   'A\u000aB'
   
   - single quotes can not encode '     --->   'I\u0027m abc.'    --->   'I\'m abc.'   --->  "I'm abc."
   - doublele quotes can not encode "   --->   "\u0022My Family\u0022"    --->   "\"My Family\""  --->  '"My Family"'
 
39   0x27  single quote
34   0x22  double quote
                     
'A
B'

unterminated str  
                  
################################################

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

Triple quotes can encode new lines.

5. multiline string
6. preformatted string   
7. documentation string
   
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

################################################

print(f"Voltage = {v}")

print(f"Voltage = {i * r}")

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

"A"  ->  65  + 32  ->  97  ->  "a"

u = input("Uppercase Character = ")
l = chr(ord(u) + 32)
print(f"Lowercase Character = {l}")

l = input("Lowercase Character = ")
u = chr(ord(l) - 32)
print(f"Uppercase Character = {u}")

################################################

15. Algorithms 

Algorithm for uppercase to lowercase 
- add 32

Algorithm for lowercase to uppercase
- substract 32

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

1$ = 5000 kyats

* 5000
10$ = 50000 kyats 

/ 5000
50000 kyats = 10$


1 kyats = 0.0002$

* 0.0002
50000 kyats = 10$

/ 0.0002
10$ = 50000 kyats

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


|\\
| \\ c
|b \\
|...\\
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

10 sec, 30m, 
s = ?
1 sec   ?
30 / 10, d/t 

distance = float(input("Enter distance (m): "))
time = float(input("Enter time (s): "))
speed = distance / time
print("Speed:", speed, "m/s")

################################################

Day.11

7. Force (Newton's Second Law) ( F = ma )

mass = float(input("Enter mass (kg): "))
acceleration = float(input("Enter acceleration (m/s²): "))
f = mass * acceleration
print("Force:", f, "N")

################################################

initial_amount = 600 g
half_life = 1000 years

3000 ? 
1000 ->  600 / 2  = 300 g
2000 ->  300 / 2  = 150 g
3000 ->  150 / 2  = 75  g  

600 * 0.5 * 0.5 * 0.5   = 75
600 * (0.5) ** 3        = 75
initial_amount * 0.5 ** n

total = 3000 years
half_life = 1000 years
n = total / half_life = 3

8. Half-Life Calculator ( NO * 0.5 ** (time / half_life) )

initial_amount = float(input("Enter initial amount(g): "))
half_life = float(input("Enter half-life (years): "))  # 4.468e9 ( e9 = 1_000_000_000 )
time = float(input("Enter elapsed time (years): "))  # 4_000_000_000

n = time / half_life
ans = initial_amount * 0.5 ** n

print("Remaining amount:", ans)

################################################

9. Character to unicode( က )

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
print("Octal:", oct(decimal))  # "0o12"
print("Hexadecimal:", hex(decimal))

################################################

12. bin, oct, hex  to decimal ( without code No )  "0011"

int -> decimal = ?

d = 10 -> d = 10
b = 10 -> d =  2
o = 10 -> d =  8
x = 10 -> d = 16

d = int("10", base=10)
b = int("10", base=2)
o = int("10", base=8)
x = int("10", base=16)

"10"
"0b10"    2
"0o10"    8
"0x10"    16

int("0b10", base=0)
int("0o10", base=0)
int("0x10", base=0)

binary = input("Enter a binary number: ")
print("Decimal:", int(binary, 2))

oct = input("Enter a octal number: ")
print("Decimal:", int(oct, 8))

hex = input("Enter a hexadecimal number: ")
print("Decimal:", int(hex, 16))

################################################

13. bin, oct, hex  to decimal ( with code No )  

"10"
"0b10"    0b = 2
"0o10"    0o = 8
"0x10"    0x = 16

int("0b10", base=0)
int("0o10", base=0)
int("0x10", base=0)

code = input("Enter a code: ")
print("Decimal:", int(code, base=0))

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

16. Temperature Converter (Celsius to Kelvin) (F -> C -> K)

celsius = float(input("Enter temperature in Celsius: "))
kelvin = celsius + 273.15
print(f"{celsius}°C is equal to {kelvin:.2f}K")

fahrenheit = float(input("Enter temperature in Fahrenheit: "))
celsius = (fahrenheit - 32) * 5/9
k = celsius + 273.15
print(k)

################################################

1km = 0.621371 miles
- miles = km * 0.621371
- km = miles / 0.621371

1 miles = 1.609 km
- km = miles * 1.609
- miles = km / 1.609

17. Kilometers to Miles       ( 1km = 0.621371 miles )   

km = float(input("Enter distance in kilometers: "))
miles = km * 0.621371  # 1km = 0.621371 miles
print(f"{km} km is equal to {miles} miles")

################################################

18. Miles to Kilometers    

miles = float(input("Enter distance in miles: "))
km = miles * 1.609  # 1miles = 1.609 km
print(f"{miles} miles is equal to {km} km")

################################################

19. Kilograms to Pounds   ( 1 kg = 2.20462 lb ) ( 1 lb = 0.454 kg )

kg = float(input("Enter weight in kilograms: "))
pounds = kg * 2.20462  # 1 kg = 2.20462 lb
print(f"{kg} kg is equal to {pounds} pounds")

################################################

20. Pounds to Kilograms

pounds = float(input("Enter weight in pounds: "))
kg = pounds * 0.454  # 1 lb = 0.454 kg
print(f"{pounds} pounds is equal to {kg} kg")

################################################

21. Meters to Feet     ( 1m = 3.28084 ft ) ( 1 ft = 0.305 m )

meters = float(input("Enter length in meters: "))
feet = meters * 3.28084
print(f"{meters} meters is equal to {feet} feet")

################################################

22. Feet to Meters

feet = float(input("Enter length in feet: "))
meters = feet * 0.305
print(f"{feet} feet is equal to {meters} meters")

################################################################################################

Day.12

                90350 sec
                  
            1505 min           50 sec
            
        25 h        5min
     
    1 day   1 h   
    

23. Seconds to Minutes and Hours

seconds = int(input("Enter time in seconds: "))
minutes = seconds / 60
hours = seconds / 3600
print(f"{seconds} seconds is equal to {minutes:.2f} minutes or {hours:.2f} hours")

################################################

24. Seconds to Seconds, Minutes and Hours   ( 350, 3950)

            3950 sec
            
            
       1 hour        350 sec
       
                  5 min    50 sec

seconds = int(input("Enter time in seconds: "))
h = seconds // 3600               # 1 hour
m = (seconds % 3600) // 60        # 350 sec // 60 => 5 min
s = (seconds % 3600) % 60         # 50 sec
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

################################################################################################

# * rate

1$ = 5000 Kysts
10$ = ?
Kysts =  10 / 1  * 5000  = 50000

2$ = 10000 Kysts
10$ = ?
Kysts =  10 / 2  * 10000  = 50000

* rate

26. Currency Converter (USD to MMK)

usd = float(input("Enter amount in USD: "))     3
exchange_rate = 5000                            1
mmk = usd * exchange_rate                       2
print(f"{usd} USD is equal to {mmk} MMK")       2     8

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

10    = 10 ** 1
100   = 10 ** 2
1000  = 10 ** 3

2 ** 1  = 2
2 ** 2  = 4
2 ** 3  = 8
2 ** 4  = 16
2 ** 5  = 32
2 ** 6  = 64
2 ** 7  = 128
2 ** 8  = 256
2 ** 9  = 512
2 ** 10 = 1024
2 ** 11 = 2048

1 * 24 * 60 * 60
1 * 1000 * 1000 * 1000

1 hour 
min = h * 60
sec = h * 60 * 60

b -> kb -> mb -> gb    (1000)(1024)
b -> gb
b
k = e3 = 1000
M = e6 = 1_000_000
G = e9 = 1_000_000_000

gb = float(input("Enter storage in GB: "))
mb = gb * 1000
kb = gb * 1000 * 1000
print(f"{gb} GB is equal to {mb} MB or {kb} KB")

gb = float(input("Enter storage in GB: "))
mb = gb * 1024  # 2 ** 10  Vs  10 ** 3
kb = gb * 1024 * 1024
print(f"{gb} GB is equal to {mb} MB or {kb} KB")

################################################

30. Bytes to GB + MB + KB + B
    
                    
                    34_567_891_234 bytes

                 34_567_891 KB    +  234 bytes
                 
            34_567 MB + 891 KB 

       34 GB + 567 MB

################################################

31. 

bytes = int(input("Enter size in bytes: ")) # 34_567_891_234 bytes
e = 1000

kb = bytes // e # 34_567_891 KB
b = bytes % e   # 234 B

mb = kb // e # 34_567 MB
kb2 = kb % e # 891 KB

gb = mb // e # 34 GB
mb2 = mb % e # 567 MB

print(f"{bytes} bytes = {gb} GB {mb2} MB {kb2} KB {b} B")


34567891234 bytes = 34 GB 567 MB 891 KB 234 B
34567891234 bytes = 32 GB 198 MB 522 KB 290 B

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

################################################

                  90350 sec
                  
            1505 min           50 sec        60
            
        25 h        5min                     60
     
     1 day 1 h                               24
         
################################################
    
                            90350 sec

    86400              1 day         3950 sec
    
    3600                           1 h       350 sec
    
    60                                     5 min  50 sec

n = 60 * 60 * 24 = 86400

sec = int(input("Seconds = "))
d = sec // 86400
h = (sec % 86400) // 3600
m = ((sec % 86400) % 3600) // 60
s = ((sec % 86400) % 3600) % 60
print(f"{d} day {h} : {m} : {s}")
        
################################################################################################

platform
1. system()
2. version()
3. architecture()[0] 

sys
1. version

psutil (process and system utilities )
1. virtual_memory() -> RAM 
   - total = 8GB
   - available = 3GB 
   
2. cpu_count(logical=False) # man = 2
   cpu_count(logical=True)  # work = 4
   
3. disk_usage('/')
   - total = 256GB
   - free = 156GB 
   
4. cpu_percent(interval=1)

5. sensors_battery()
   - power_plugged
   - percent

################################################

1. Check Operating System

import platform

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

Day.12

7. Check Disk Usage (Total and Free Space)

import psutil
disk = psutil.disk_usage('/')
t = disk.total / ( 1024 ** 3 )
f = disk.free / ( 1024 ** 3 )
print(f"Total Disk Space: {t:.0f} GB")
print(f"Free Disk Space: {f:.0f} GB")

################################################

8. Check CPU Usage

import psutil
cpu = psutil.cpu_percent(interval=1)
print(f"CPU Usage:", cpu, "%")

################################################

9. Check Battery Status

import psutil

battery = psutil.sensors_battery()
charging = battery.power_plugged
percent = battery.percent

print(f"Battery Status: {percent}%")
print("Charging:", charging)

################################################

import psutil
disk = psutil.disk_usage('/')

gb = disk.free // ( 1024 ** 3 )
mb = (disk.free % ( 1024 ** 3 )) // ( 1024 ** 2 )
kb = ((disk.free % ( 1024 ** 3 )) % ( 1024 ** 2 )) // 1024
b =  ((disk.free % ( 1024 ** 3 )) % ( 1024 ** 2 )) % 1024
print(f"Free Disk Space: {gb} GB {mb} MB {kb} KB and {b} bytes")

print(dir(psutil)) 

################################################################################################

        bytes
              
         GB        B             ( 1024 ** 3 )
         
              MB     B           ( 1024 ** 2 )
              
                 KB    B         ( 1024 )
                 
                                
               136_023_508_001 bytes       (1000) (1024)
             
        136_023_508 kb       1 b
        
   136_023 mb   508 kb
    
136 gb  23 mb     


import psutil
disk = psutil.disk_usage('/')

gb = disk.free // ( 1024 ** 3 )
mb = (disk.free % ( 1024 ** 3 )) // ( 1024 ** 2 )
kb = ((disk.free % ( 1024 ** 3 )) % ( 1024 ** 2 )) // 1024
b =  ((disk.free % ( 1024 ** 3 )) % ( 1024 ** 2 )) % 1024
print(f"Free Disk Space: {gb} GB {mb} MB {kb} KB and {b} bytes")

b = disk.free % 1024
kb = (disk.free // 1024) % 1024
mb = ((disk.free // 1024) // 1024) % 1024
gb = ((disk.free // 1024) // 1024) // 1024
print(f"Free Disk Space: {gb} GB {mb} MB {kb} KB and {b} bytes")

################################################

Day.13

10. BMI (Body Mass Index) Calculator  (kg per m**2)

weight = float(input("Enter weight in kg: "))
height = float(input("Enter height in meters: "))
bmi = weight / (height ** 2)
print(f"Your BMI is: {bmi}")


weight = float(input("Enter weight in lb: ")) * 0.454
height = float(input("Enter height in ft: ")) * 0.3048
bmi = weight / (height ** 2)
print(f"Your BMI is: {bmi}")


# 1lb = 0.454 kg  ( lb * 0.454 )
# 1kg = 2.2lb     ( lb / 2.2 )

# 1ft = 0.3048m   ( ft * 0.3048 )
# 1m = 3.28 ft    ( ft / 3.28 )

weight2 = float(input("Enter weight in lb: ")) * 0.454
height_f = float(input("Enter height in ft: ")) * 0.3048
height_i = float(input("Enter height in inches: ")) * 0.0254
height2 = height_f + height_i

bmi2 = weight2 / (height2 ** 2)
print(f"Your BMI is: {bmi2}")

################################################

11. Heart Rate Zones Calculator

32

188 bpm                 

< 94         ( sit )

> 94         ( walk )

> 131 bpm    ( run )


64

156  bpm

< 78         ( sit )

> 78         ( walk )

> 109 bpm    ( run )

100  --> 50
1    --> ? 1 / 100  * 50  = 0.5


100 % = 100 / 100 = 1
95%  = 95 / 100 = 0.95
85 % = 85 / 100 = 0.85
75 % = 75 / 100 = 0.75
50 % = 50 / 100 = 0.5
5 %  = 5 / 100  = 0.05 
105% = 105 / 100 = 1.05 

100  -> 50
1    -> 0.5      (rate)
188  -> ?  188 * 0.5 = 94


age = int(input("Enter your age: "))
max_heart_rate = 220 - age

print(f"Maximum Heart Rate: {max_heart_rate} bpm")
print(f"Fat Burn Zone (50-70%): {max_heart_rate * 0.5} - {max_heart_rate * 0.7} bpm")
print(f"Cardio Zone (70-85%): {max_heart_rate * 0.7} - {max_heart_rate * 0.85} bpm")
print(f"Peak Zone (85-100%): {max_heart_rate * 0.85} - {max_heart_rate} bpm")

################################################

12. Moles to Mass Converter

molar_mass = float(input("Enter molar mass (g/mol): "))
moles = float(input("Enter number of moles: "))
print("Mass:", molar_mass * moles, "g")

################################################

13. Mass to Moles Converter

mass = float(input("Enter mass (g): "))
molar_mass = float(input("Enter molar mass (g/mol): "))
print("Moles:", mass / molar_mass)

################################################

14. Concentration (Molarity) Calculator

moles = float(input("Enter moles of solute: "))
volume = float(input("Enter volume of solution (L): "))
print("Molarity:", moles / volume, "M")

################################################

15. Dilution Calculator (M1V1 = M2V2)

M1V1 = M2V2
M2V2 = M1V1
M2 = M1V1/V2

M1 = float(input("Enter initial molarity (M): "))
V1 = float(input("Enter initial volume (L): "))
M2 = float(input("Enter final molarity (M): "))
print("Final volume:", (M1 * V1) / M2, "L")

################################################

16. Work Done

force = float(input("Enter force (N): "))
distance = float(input("Enter distance (m): "))
print("Work Done:", force * distance, "J")

################################################

17. Gravitational Force

G = 6.674 * (10**-11)
m1 = float(input("Enter mass of first object (kg): "))
m2 = float(input("Enter mass of second object (kg): "))
r = float(input("Enter distance between objects (m): "))
print("Gravitational Force:", G * m1 * m2 / (r ** 2), "N")

################################################

18. Kinetic Energy ( 1/2.m.v**2 )  ( 0.5 * m * v ** 2 )

mass = float(input("Enter mass (kg): "))
velocity = float(input("Enter velocity (m/s): "))
print("Kinetic Energy:", 0.5 * mass * velocity ** 2, "J")

################################################

19. Potential Energy (mgh) ( m * g * h )

mass = float(input("Enter mass (kg): "))
height = float(input("Enter height (m): "))
g = 9.81
ans = mass * g * height
print("Potential Energy:", ans, "J")

################################################

20. Power Calculation (Electrical Power) ( P = VI ) ( V * I )

voltage = float(input("Enter voltage (V): "))
current = float(input("Enter current (A): "))

print("Power:", voltage * current, "W")

################################################

21. Frequency and Wavelength (Wave Equation) (Frequency = speed / wavelength)


Frequency = speed / wavelength

wavelength = 3m

speed = 12 m sec

Frequency = 12 / 3 = 4

speed = float(input("Enter wave speed (m/s): "))
wavelength = float(input("Enter wavelength (m): "))
print("Frequency:", speed / wavelength, "Hz")

################################################

22. Momentum

mass = float(input("Enter mass (kg): "))
velocity = float(input("Enter velocity (m/s): "))
print("Momentum:", mass * velocity, "kg·m/s")

################################################

23. Ideal Gas Law Calculator (PV = nRT) (P = nRT/V) (P = n * R * T / V)

V = float(input("Enter volume (L): "))
n = float(input("Enter number of moles: "))
R = 0.0821  # Gas constant (L·atm/mol·K)
T = float(input("Enter temperature (K): "))
print("Pressure:", n * R * T / V, "atm")

################################################

24. Percentage Composition

p = 200       100%
s = 210       ? 105%

210 / 200  *  100  = 21000 / 200 = 210 / 2 = 105 %

x = (s / p) * 100  # 105 % -> + 5%
print(x)

element_mass = float(input("Enter mass of the element (g): "))
compound_mass = float(input("Enter total mass of the compound (g): "))
print("Percentage composition:", (compound_mass / element_mass) * 100, "%")


################################################

25. Heat Energy Calculation (q = mcΔT) (mass * specific_heat * temp_change)

mass = float(input("Enter mass (g): "))
specific_heat = float(input("Enter specific heat capacity (J/g·°C): "))
temp_change = float(input("Enter temperature change (°C): "))
print("Heat energy:", mass * specific_heat * temp_change, "J")

################################################

26. Avogadro’s Law Calculator (V1/n1 = V2/n2) (v2 = (V1/n1) * n2 )

V1 = float(input("Enter initial volume (L): "))
n1 = float(input("Enter initial moles: "))
n2 = float(input("Enter final moles: "))
print("Final volume:", (V1/n1) * n2, "L")

################################################

27. Running Pace Calculator

distance = float(input("Enter distance in kilometers: "))
time_minutes = float(input("Enter time taken in minutes: "))

pace = time_minutes / distance
print(f"Your running pace is {pace:.2f} minutes per km.")

################################################

28. Fuel Efficiency Converter (L/100km to MPG) (miles per gallon)

mpg = 235.215 / liters_per_100km
mpg * liters_per_100km = 235.215  
liters_per_100km = 235.215 / mpg  


x = y / z
y = x * z
z = y / x
liters_per_100km = 235.215 / mpg

liters_per_100km = float(input("Enter fuel efficiency in L/100km: "))
mpg = 235.215 / liters_per_100km
print(mpg, "MPG")

mpg = float(input("Enter fuel efficiency in mpg: "))
liters_per_100km = 235.215 / mpg
print(liters_per_100km, "l per 100km.")

################################################

29. Square Root Calculator

number = float(input("Enter a number: "))
sqrt = number ** (1/2)
print(f"The square root of {number} is {sqrt}")

# Cube Root Calculator
number = float(input("Enter a number: "))
print(f"The cube root of {number} is {number ** (1/3):.0f}")

################################################

30. Simple Interest  (p * r * t)

100_000
1 year = 100_000 + 10_000 = 110_000

10 %  
100      ->  10

rate
1        ->  1/100 * 10 = 10/100  = 0.1                 <- rate for 1 item

100000   ->  100000 / 1 * 0.1 = 100000 * 0.1 = 10000    <- Interest for 1 year

1 year   ->  10000
5 years  ->  5/1 * 10000 =  5 * 10000 = 50000           <- Interest for 5 years

50000
10000 * 5
100000 * 0.1 * 5
p * rate * year

p = float(input("Enter principal amount: "))
r = float(input("Enter interest rate (%): ")) / 100  # 0.1
t = float(input("Enter time (years): "))
print("Simple Interest:", p * r * t)

################################################

31. Compound Interest

100_000
1 year => 100_000 + 10_000 =>  110_000 
2 year => 110_000 + 11_000 =>  121_000
3 year => 121_000 + 12_100 =>  133_100

################################################

p = 100_000
r = 0.1

i = p * r # 10_000
p = p + i # 110_000
print(p)

################################################

p = 100_000
r = 0.1

i = p * r # 10_000
p = p + i # 110_000
print(f"1 year = {p}")

i = p * r # 11_000
p = p + i # 121_000
print(f"2 year = {p}")

i = p * r # 12_100
p = p + i # 133_100
print(f"3 year = {p}")

i = p * r
p = p + i
print(f"4 year = {p}")

i = p * r
p = p + i 
print(f"5 year = {p}")

################################################

p = 100_000
r = 0.1

for n in range(1, 6): 
    i = p * r
    p = p + i
    print(f"{n} year = {p}")

################################################################################################

p = 100_000
r = 0.1

i = p * r # 10_000
p = p + i # 110_000

i = p * r # 11_000
p = p + i # 121_000

i = p * r # 12_100
p = p + i # 133_100

i = p * r
p = p + i

i = p * r
p = p + i

print(f"5 year = {p}")

################################################

p = 100_000
r = 0.1

for _ in range(5):
    i = p * r
    p = p + i

print(f"5 year = {p}")

################################################################################################

for
1. iteration       for n in range(1, 6)
2. looping (_)     for _ in range(5)

################################################

p = float(input("Enter principal amount: "))
r = float(input("Enter interest rate (%): ")) / 100  # 0.1
t = int(input("Enter time (years): ")) # 5

# print(f"{t} year = {(p * r * t) + p}")

for _ in range(t):
    i = p * r
    p = p + i

print(f"{t} year = {p}")

################################################

p = float(input("Enter principal amount: "))
r = float(input("Enter interest rate (%): ")) / 100  # 0.1
t = int(input("Enter time (years): ")) # 5

for n in range(1, t+1):
    i = p * r
    p = p + i
    print(f"{n} year = {p}")
    
################################################################################################

32. nested loop

2 * 1 = 2
2 * 2 = 4
2 * 3 = 6
2 * 4 = 8
2 * 5 = 10
2 * 6 = 12
2 * 7 = 14
2 * 8 = 16
2 * 9 = 18
2 * 10 = 20
2 * 11 = 22
2 * 12 = 24


print(f"2 * 1 = ?")
print(f"2 * 2 = ?")
print(f"2 * 3 = ?")
print(f"2 * 4 = ?")
print(f"2 * 5 = ?")
print(f"2 * 6 = ?")
print(f"2 * 7 = ?")
print(f"2 * 8 = ?")
print(f"2 * 9 = ?")
print(f"2 * 10 = ?")
print(f"2 * 11 = ?")
print(f"2 * 12 = ?")

################################################

for n in range(1, 13):
    print(f"2 * {n} = {2 * n}")

print("- " * 39)

for n in range(1, 13):
    print(f"3 * {n} = {3 * n}")

print("- " * 39)

for n in range(1, 13):
    print(f"4 * {n} = {4 * n}")

print("- " * 39)

for n in range(1, 13):
    print(f"5 * {n} = {5 * n}")

print("- " * 39)

################################################

2 * 1 = 2
2 * 2 = 4

print(f"2 * 1 = 2")
print(f"2 * 2 = 4")
...
..
print(f"11 * 10 = 110")

################################################
    
for i in range(2, 12):
    for n in range(1, 11):
        print(f"{i} * {n} = {i * n}")

    print("- " * 39)
    
################################################

for i in range(2, 25):
    for n in range(1, 13):
        print(f"{i} * {n} = {i * n}")

    print("- " * 39)

################################################################################################

Computer    

generation

i3     10
i5     15
i7     25

silicon chip
m1         i7 12 generation      
m2
m3
m4
m5

i7    13 seconds      100 m     ( 1 km)
m1    13 seconds      100 m     (40 km)

Server  car       

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
