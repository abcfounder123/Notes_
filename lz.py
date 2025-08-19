"""

Lazy class ဆိုတာက အိမ်စာမပါပဲ တစ်ခါတည်း အလွတ်နီးပါးရအောင် သင်ပေးတဲ့ အတန်းပါ။

1. Mindset
2. Limit
3. Behaviour
4. Ethics
5. Imaginary
6. Step
7. Simple
8. Imperative paradigm(procedure, object), Declarative paradigm (functional)
9. Procedural programming (procedure)

################################################

1. Sequence(time)
2. Selection
3. Iteration 
4. Function

################################################

1. data types
2. control flow (sequence, selection, iteration)
3. function (procedure)

################################################

1. time (sequence)
   - top to b
   - left to right
   - parenthesis 

################################################

p0  computer open
p1  song open
p2  song close
p3  computer close

################################################

012123

p0 p1
p2 p1
p2 p3

p3(p2(p1(p2(p1(p0)))))

################################################

p3(p0) p1(p0)
p2 p1
p2 p3

03012123

################################################

abc  ( data types 15 )

apple ( type casting, ... )

practice 

grammer ( syntax )

################################################

1. Data types
  - str
    - character (chr)
    - character string ( str )
    - documentation string ( doc )

  - number
    - int       --->   integer 
    - float     --->   decimal/floating-point number
    - complex   --->   complex number

  - 8
    - normal list  2   (list, tuple)
    - unique list  2   (set, frozenset)
    - binary list  2   (bytearray, bytes)
    - number list  1   (range)(generator object)
    - item list    1   (dict)

  - condition           bool
    
  - memoryview

  - None Type           None

################################################

range

1, 2, 3, 4, ..., 100
start = 1
stop = 101
step = 1

################################################

odd 50  = 1, 3, 5, to 99
start = 1
stop = 100
step = 2

even 50 = 2, 4, 6, to 100
start = 2
stop = 101
step = 2

reversed odd 50 = 99, 97, 95 to 1
start = 99
stop = 0
step = -2

reversed even 50 = 100, 98, 96, 94 to 2
start = 100
stop = 1
step = -2

################################################

1. Data type 

################################################

1.1. built-in data types ( 15)

1. str
2. int
3. float
4. complex
5. list
6. tuple
7. range
8. dict
9. set
10. frozenset
11. bool
12. bytes
13. bytearray
14. memoryview
15. NoneType(None)

################################################

1. mutable, immutable
   - list, set, bytearray, dict
   
2. unordered, ordered (indexing)
   - set, frozen set, dict
   
################################################

1.2.Creating built-in data types with notations

notations
1. quotes
2. .
3. j
4. []
5. (), (comma)
6. {}  (set)
7. b
8. {} (dict)

Notation is value.
1. 1
2. True, False
3. None

No notation 
1. frozenset()
2. bytearray()
3. range()
4. memoryview()

################################################

1.3.Creating built-in data types with name ( type casting )

1. str
2. int
3. float
4. complex
5. list
6. tuple
7. range
8. dict
9. set
10. frozenset
11. bool
12. bytes
13. bytearray
14. memoryview

################################################

15. NoneType      <---   only notation value None

################################################

1.4.Python has five rules for naming identifiers(labels).

(one, alpha, number, o, r)

1. An identifier must contain at least one character.
2. The first character of an identifier must be an alphabet or the underscore.
3. The remaining characters may be alphabets, underscores, numbers.
4. Qther characters are not permitted.
5. A reserved keyword cannot be used as an identifier.
6. meaningful

################################################

"""

# 1.5.Checking data type

b''
b'apple'

bytearray(b'')
bytearray(b'apple')

memoryview(b"apple")
# <memory at 0x1005f2080>

''
' '
'1000'
"1000"
'''1000'''
"""1000"""

0j
3 + 2j
1j

0
-1
+1
1_000
1_000_000
1_000_000_000
1000000000

0.0
-1.0
+1.0
1.0
1000.0
.01
100.
0.
1_000_000.0
1e6
1e-6
0.000001

["apple", "banana", "orange"]
[]
list()

()
tuple()
("Mg Mg", 20, 5.5)

range(0, 10)
range(2, 101, 2)

{"name": "Mg Mg", "age": 20, "height": 5.5}

{
    "name": "Mg Mg",
    "age": 20,
    "height": 5.5
}

{}

{"apple", "banana", "orange"}
set()
frozenset()
frozenset({'apple', 'orange', 'banana'})  # frozenset
frozenset(['apple', 'orange', 'banana'])
frozenset(('apple', 'orange', 'banana'))

1000
0
int()

True
False
bool()

None

{}
{1, }

(1 + 2) * 3
(1)
("apple")

(1,)
("apple",)
1, 2, 3
1,

"1000"
str(1000)

1000
int("1000")

1000.0
float(1000)
float("1000")
2.6
1 + 1.6

float(1) + 1.6
1.0 + 1.6

################################################

# 1.6.boolean value exercise

0
0.0
0j

1
1000
12.5
0.1
0.000001
1e6

{}  # empty dict
set()  # empty set
[]  # empty list
()  # empty tuple
frozenset()  # empty frozenset
""  # empty str
''
""""""
''''''
b""
bytearray(b"")

################################################


"""

1. indexing  ( +, - )

   - left  (positive index) (0) 
   - right (negative index) (1)
   
   - f3  (richest_3 = countries[2] )
   - l3  (p3 = countries[-3] )
   
   - range (-t to t-1)
   - hard = total - abs(easy) 
      
   - middle_country
     - total = odd, m = t // 2
     - total = even, rm = t // 2, lm = rm - 1

################################################

middle_country 

1 2 3 4 5 6 7     
a b c d e f  
0 1 2 3 4 5 6   left   +      
7 6 5 4 3 2 1   right  -     

total = odd, middle = 1
m = t // 2

total = even, middle = 2
rm = t // 2
lm = rm - 1 
   
################################################   
   
2. slicing
   - collection (total)
   - positive and negative for each item
   - result, start:stop:step
   - blank ---> [:4], [-4:]
   - dataset
     - first five, last five
     - inverse

################################################

basic

a b c d e f g    x
0 1 2 3 4 5 6   (+)
7 6 5 4 3 2 1   (-)

bcde -> start = b, stop = f
1234 -> x[1:5:1]
6543 -> x[-6:-2:1]

edcb -> e, a, -1
4321 -> x[4:0:-1]
3456 -> x[-3:-7:-1]

################################################

blank

first 4  
  - 0, 1, 2, 3  
  - [0:4:1]
  - [0:4]
  - [:4]
  
last 4
  - -4, -3, -2, -1
  - [-4:0:1]
  - [-4:0]
  - [-4:]
  
inverse
[::-1]

################################################

# reverse engineering of middle 11 inverse

# [t // 2 - 5 : t // 2 + 6][::-1]
# [::-1] inverse
# m = t // 2
# s = m - 5
# stop = m + 6

################################################  
   
countries = list(range(1, 201))
print(countries)

# first 5, last 5 (easy index)
print(countries[:5])   #  0, 1, 2, 3, 4        #   0:5:1
print(countries[-5:])  # -5, -4, -3, -2, -1    #  -5:0:1

################################################ 

# first 5, last 5 (hard index)
# -200, -199, -198, -197, -196  -> -200:-195:1  -> -200:-195  -> :-195
print(countries[:-195]) 

# 195, 196, 197, 198, 199   ->  195:200:1  ->  195:
print(countries[195:])

################################################ 

- poorest five from richest dataset 
  -> -1, -2, -3, -4, -5        ->   -1:-6:-1     ->   :-6:-1     (easy index)
  -> 199, 198, 197, 196, 195   ->   199:194:-1   ->   :194:-1    (hard index)

################################################ 

richest dataset to  poorest dataset
:::   ->   0:200:1     ->   0, 1, 1, 3, ..., 199
::-1  ->  -1:-201:-1   ->   -1, -1, -3, ..., -200

################################################ 

################################################

1. Operand
   >> left operand
   >> right operand
   
     1    +    2
    /     |     \
  left    |     right
       operator
(addinional operation) 

1 + 2 (binary plus)
+1 (unary plus)

add()
pos()

sub()
neg()

################################################

2. Operator                 
   -  unary operator   --->   right operand                     
      1. unary plus    --->   + 1
      2. unary minus   --->   - 1
      3. logical NOT   --->   not True
      4. bitwise NOT   --->   ~ 5
        
   -  binary operator  --->   left operand, right operand
  
   -  Ternary operator --->   middle operand 

################################################

3. Precedence
   >> parenthesis        --->   ( )
   
   >> Arithmetic operator ( e, u, * /, + - )
   1. exponentiation     --->   **  
   2. unary +, -         --->   +1, -1
   3. multiplication     --->   *
      division   
         division           --->   /
         floor division     --->   //  (ceiling)      ( 2.5  ---> 2, 3 )
         modulus            --->   %
   4. addition           --->   +
      substraction       --->   -

      
(1 + 2) * 3   
3 * 3
9

1 + (2 * 3)
1 * 6
7

################################################

4. Associativity
   >> left sided bind
   >> right sided bind ( **, = )
   
2 ** 3 ** 4
8 ** 4
4096

2 ** 3 ** 4
2 ** 81
2417851639229258349412352
   
x = y = 1

################################################

3. Precedence
>> parenthesis        --->   ( )
   
Arithmetic operators (Perform mathematical operations)( e, u, * /, + - )(9)
1. exponentiation     --->   **  
2. unary +, -         --->   +1, -1, ~
3. multiplication     --->   *
   division   
   division           --->   /
   floor division     --->   //
   modulus            --->   %
4. addition           --->   +
   substraction       --->   -
   
Bitwise Operators (Operate on bits)(shift, and, or2, not)(6)
5. Left shift         --->   <<
   Right shift        --->   >>

6. Bitwise AND        --->   &

7. Bitwise XOR        --->   ^

8. Bitwise OR         --->   |

2. Bitwise NOT        --->   ~

9. 
Comparison Operators (Compare values)(6)
   Equal to           --->   ==              
   Not equal to       --->   !=
   Greater than       --->   >
   Less than          --->   <
   Greater than or equal to   --->   >=
   Less than or equal to      --->   <=

Identity Operators (Compare memory locations)
   Identical objects          --->   is
   Not identical objects      --->   is not

Membership Operators (Test for membership in sequences)
   Present in the sequence    --->   in
   Not present in the sequence --->   not in

Logical Operators (Combine conditional statements)
10.Logical NOT        --->   not
11.Logical AND        --->   and
12.Logical OR         --->   or

13. Ternary Operator
14.Assignment Operators (Assign values to variables) (13)
    Simple assignment --->   =
    Add and assign    --->   +=
15. Walrus Operator   --->   :=

################################################

5. Notes

e, 
u,   -, +, ~
* /, 
+ -                         

shift                         bitwise
and       
xor
or

C                           
not                           logical
and
or

t                             
assignment                    =, **=, *=, /=, //=, %=, +=, -=, <<=, >>=, &=, ^=,|=   
walrus                        :=

################################################

6. Built-in Operators ( 7 )

1. Arithmetic Operators        (9)
2. Bitwise Operators           (6)
3. Comparison Operators        (6)
4. Identity Operators          (2)
5. Membership Operators        (2)
6. Logical Operators           (3)
7. Assignment Operators       (13)
   Walrus                      (1)
                            
   ternary                      1  
   
                               43
                              
################################################
################################################

1. Arithmetic operators in programming

Seconds to Seconds, Minutes, Hours and days ( 90350 )

1hour = 3600 seconds
1day = 24 hours 
1min = 60 seconds

90350 sec // 3600 = 25      h
90350 sec % 3600 = 350      sec

25 h // 24 = 1   day
25 h %  24 = 1   h

350 sec // 60 = 5    min
350 sec % 60 = 50    sec

             90350       = 1 day 1:5:50
          /        |
        25h       350sec
      /   |      /   |
     1d   1h    5min 50sec
     
################################################

2. basic input, output

input 
- receive string value
- prompt letter

print
- print string value
- commma

################################################

3. Three components of programming

noise cancelling (zoom)
input   --->  mic (35db to 250db)
process --->  70db to 100db
output  --->  speaker

day hour minute
input   --->  keyboard (str value of seconds)
process --->  str to int, day, hour, minute
output  --->  standard output file

################################################

sec = int(input("Enter seconds:"))  # 90350

h = sec // 3600                     # 25
sm = sec % 3600                     # 350

day = h // 24                       # 1 d
hour = h % 24                       # 1 h

min = sm // 60                      # 5 min
sec = sm % 60                       # 50 sec

print(day, "day", hour, "hour", min, "minute", sec, "second")

################################################

4. Normal statements

fail statement
pass statement

################################################

5. Conditional statements
  
fail condition:  fail statement
pass condition:  pass statement

################################################

6. program flow
- ability to check the flow of programs

################################################

7. control flow 
- ability to control the flow of programs

################################################

8. program quality (13, 7, 6)

mark = int(input("Enter marks:"))  
exam_pass = mark >= 50  
fail = mark < 50    
if exam_pass:print("pass")
if fail:print("fail")

mark = int(input("Enter marks:")) 
print("Exam result")
if mark >= 50:print("pass")
if mark < 50:print("fail")

mark = int(input("Enter marks:"))
print("Exam result")
if mark >= 50:print("pass")
else:print("fail")

################################################

9. Selection(if, else)

fail or pass 
sleep or walk

################################################

################################################

CLI, GUI, Web base

################################################

1. Basic input & output
---> input -> prompt letter
---> print -> comma
---> format -> f" {}  {} {} "

################################################

1. Water Intake Calculator

weight = float(input("Enter your weight in kg: "))
min = weight * 0.033
max = weight * 0.050
print("You should drink from", min, "to", max, "liters of water per day.")

################################################

2. Area of the circle ( pi.r**2 )

r = float(input("Enter radius: "))
area = 3.14159 * r ** 2
print("Area of the circle:", area)               

################################################

3.Area of triangle ( 1/2.b.h)

base = float(input("Enter base: "))
height = float(input("Enter height: "))
area = 0.5 * base * height
print("Area of triangle:", area)

################################################

4. Hypotenuse ( c**2 = a**2 + b**2)

a = float(input("Enter first side: "))
b = float(input("Enter second side: "))
h = (a ** 2 + b ** 2) ** (1/2)
print("Hypotenuse:", h)

################################################

5. Ohm’s Law (Voltage, Current, Resistance)( V = IR )

voltage = float(input("Enter voltage (V): "))
resistance = float(input("Enter resistance (Ω): "))
current = voltage / resistance
print("Current:", current, "A")

################################################

6. Speed ( s = d / t )

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

8. Half-Life Calculator ( NO * 0.5 ** (time / half_life) )

initial_amount = float(input("Enter initial amount(g): "))
half_life = float(input("Enter half-life (years): "))  # 4.468e9 ( e9 = 1_000_000_000 )
time = float(input("Enter elapsed time (years): "))  # 4_000_000_000
ans = initial_amount * 0.5 ** (time / half_life)
print("Remaining amount:", ans)

################################################

9. Character to ASCII Code ( က )

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

12. bin, oct, hex  to decimal ( with code No )  "0b0011"

binary = input("Enter a binary number: ")
print("Decimal:", int(binary, base=0))

oct = input("Enter a octal number: ")
print("Decimal:", int(oct, base=0))

hex = input("Enter a hexadecimal number: ")
print("Decimal:", int(hex, base=0))

################################################

13. bin, oct, hex  to decimal ( without code No )  "0011"
binary = input("Enter a binary number: ")
print("Decimal:", int(binary, 2))

oct = input("Enter a octal number: ")
print("Decimal:", int(oct, 8))

hex = input("Enter a hexadecimal number: ")
print("Decimal:", int(hex, 16))

################################################
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

17. Kilometers to Miles

km = float(input("Enter distance in kilometers: "))
miles = km * 0.621371
print(f"{km} km is equal to {miles} miles")

################################################

18. Miles to Kilometers

miles = float(input("Enter distance in miles: "))
km = miles / 0.621371
print(f"{miles} miles is equal to {km} km")

################################################

19. Kilograms to Pounds

kg = float(input("Enter weight in kilograms: "))
pounds = kg * 2.20462
print(f"{kg} kg is equal to {pounds} pounds")

################################################

20. Pounds to Kilograms

pounds = float(input("Enter weight in pounds: "))
kg = pounds / 2.20462
print(f"{pounds} pounds is equal to {kg} kg")

################################################

21. Meters to Feet 

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
print(h, m, s)

################################################

25. Seconds to Seconds, Minutes, Hours and days ( 90350 )

seconds = int(input("Enter time in seconds: "))
h = seconds // 3600
m = (seconds % 3600) // 60
s = (seconds % 3600) % 60
d = h // 24
nh = h % 24
print(d, nh, m, s)

################################################

# * rate

26. Currency Converter (USD to MMK)

usd = float(input("Enter amount in USD: "))
exchange_rate = 6000  
mmk = usd * exchange_rate
print(f"{usd} USD is equal to {mmk} MMK")

################################################

27. Currency Converter (Custom Rate)

amount = float(input("Enter amount: "))
rate = float(input("Enter exchange rate: "))
converted = amount * rate
print(f"Converted amount: {converted}")

################################################

28. Length Converter (Meters to Feet)

meters = float(input("Enter length in meters: "))
feet = meters * 3.28084
print(f"{meters} meters is equal to {feet:.2f} feet")

################################################

29. Weight Converter (Kilograms to Pounds)

kg = float(input("Enter weight in kg: "))
pounds = kg * 2.20462
print(f"{kg} kg is equal to {pounds:.2f} pounds")

################################################

30. Speed Converter (Km/h to Mph)

kmh = float(input("Enter speed in km/h: "))
mph = kmh * 0.621371
print(f"{kmh} km/h is equal to {mph:.2f} mph")

################################################

31. Step-to-Calorie Converter

steps = int(input("Enter number of steps taken: "))
calories_burned = steps * 0.04  # Approximation for an average person
print(f"Calories burned: {calories_burned:.2f} kcal")

################################################

32. Storage Converter (GB to MB & KB)

gb = float(input("Enter storage in GB: "))
mb = gb * 1024  # 2 ** 10  Vs  10 ** 3
kb = mb * 1024
print(f"{gb} GB is equal to {mb} MB or {kb} KB")

################################################

33. bytes_size = int(input("Enter size in bytes: "))
kb = bytes_size / 1024
mb = kb / 1024
gb = mb / 1024 
print(f"{bytes_size} bytes = {kb:.2f} KB = {mb:.2f} MB = {gb:.2f} GB")

################################################

3_002_004_010 // e9 = 3 billion                  <---  giga bytes
3_002_004_010 % e9  = 2_004_010
(3_002_004_010 % e9) // e6 = 2 million           <---  mega bytes
(3_002_004_010 % e9) % e6 = 4_010
((3_002_004_010 % e9) % e6) // e3 = 4 thousand   <---  kilo bytes
((3_002_004_010 % e9) % e6) % e3 = 10            <---  bytes

e3, e6, e9 ---> 10 ** 3 ---> 1000
kb, mb, gb ---> 2 ** 10 ---> 1024

################################################

34. 

bytes_size = int(input("Enter size in bytes: "))

gb = bytes_size // 1e9
mb = (bytes_size % 1e9) // 1e6
kb = ((bytes_size % 1e9) % 1e6) // 1e3
b = ((bytes_size % 1e9) % 1e6) % 1e3

print(f"{gb}GB {mb}MB {kb}KB {b}B")

################################################

e_9 = 1024 ** 3
e_6 = 1024 ** 2
e_3 = 1024
gb = bytes_size // e_9
mb = (bytes_size % e_9) // e_6
kb = ((bytes_size % e_9) % e_6) // e_3
b = ((bytes_size % e_9) % e_6) % e_3

print(f"{gb}GB {mb}MB {kb}KB {b}B")

################################################

bytes_size = int(input("Enter size in bytes: "))
gb = bytes_size // 1024 ** 3 
mb = (bytes_size % 1024 ** 3) // 1024 ** 2 
kb = ((bytes_size % 1024 ** 3) % 1024 ** 2) // 1024  
b = ((bytes_size % 1024 ** 3) % 1024 ** 2) % 1024

print(f"{gb}GB {mb}MB {kb}KB {b}B")

################################################

35. Check Total RAM / Available RAM (Memory) 

import psutil

ram = psutil.virtual_memory()

total = ram.total / ( 1024 ** 3 )
available = ram.available / ( 1024 ** 3 )

print(f"Total RAM:", total, "GB")
print(f"Available RAM:", available, "GB")

################################################



"""