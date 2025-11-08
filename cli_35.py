"""
1. Water Intake Calculator

weight = float(input("Enter your weight in kg: "))
min = weight * 0.033
max = weight * 0.050
print(f"You should drink from {min:.2f} liters to {max:.2f} litres.")

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

calories_burned = int(input("Calories burned: "))
steps = calories_burned / 0.04
print(f"Number of steps : {steps:.2f} steps")

################################################

32. Storage Converter (GB to MB & KB)

b -> kb -> mb -> gb
b -> gb
k = e3 = 1000
M = e6 = 1_000_000
G = e9 = 1_000_000_000


gb = float(input("Enter storage in GB: "))
mb = gb * 1024  # 2 ** 10  Vs  10 ** 3
kb = mb * 1024
print(f"{gb} GB is equal to {mb} MB or {kb} KB")

################################################

33.

bytes_size = int(input("Enter size in bytes: "))

kb = bytes_size / 1024
mb = kb / 1024
gb = mb / 1024
print(f"{bytes_size} bytes = {kb:.2f} KB = {mb:.2f} MB = {gb:.2f} GB")

################################################

34.

bytes_size = int(input("Enter size in bytes: "))

gb = bytes_size // 1e9
mb = (bytes_size % 1e9) // 1e6
kb = ((bytes_size % 1e9) % 1e6) // 1e3
b = ((bytes_size % 1e9) % 1e6) % 1e3

print(f"{gb}billion {mb}million {kb}thousand and {b}")

################################################################################################

35. 1e9 --> 1024 ** 3

################################################################################################

34.

b
kb  = 1000.0 = 1e3                 (1000)           ( 1024 )
mb  = 1000000.0 = 1e6              (1000 ** 2)      ( 1024 ** 2 )
gb  = 1_000_000_000.0 bytes = 1e9  (1000 ** 3)      ( 1024 ** 3 )

1kg = 1000g 
12000 g = 1.2kg

         12_345_678_900       bytes
         
      12 GB     345_678_900 bytes
         
              345 MB      678_900   bytes
              
                       678 KB    900  bytes
         
 12 GB  345 MB  678 KB  900  bytes
 
################################################ 

bytes_size = int(input("Enter size in bytes: ")) # 12_345_678_900       bytes

gb = bytes_size // 1e9                       # 12 GB
mb = (bytes_size % 1e9) // 1e6               # 345 MB
kb = ((bytes_size % 1e9) % 1e6) // 1e3       # 678 KB
b = ((bytes_size % 1e9) % 1e6) % 1e3         # 900  bytes

print(f"{gb} GB {mb} MB {kb} KB and {b} bytes")

################################################

35.

bytes_size = int(input("Enter size in bytes: ")) # 12_345_678_900       bytes

gb = bytes_size // (1024 ** 3)                      # 11 GB
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

7. Check Disk Usage (Total and Free Space)

import psutil
disk = psutil.disk_usage('/')
t = disk.total / ( 1024 ** 3 )
f = disk.free / ( 1024 ** 3 )
print(f"Total Disk Space:", t, "GB")
print(f"Free Disk Space:", f, "GB")

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

################################################

10. BMI (Body Mass Index) Calculator

weight = float(input("Enter weight in kg: "))
height = float(input("Enter height in meters: "))
bmi = weight / (height ** 2)
print(f"Your BMI is: {bmi}")

weight = float(input("Enter weight in lb: ")) / 2.2
height = float(input("Enter height in feet: ")) / 3.281
bmi = weight / (height ** 2)
print(f"Your BMI is: {bmi}")


weight = float(input("Enter weight in lb: ")) / 2.2
height_f = float(input("Enter height in feet: ")) / 3.281
height_i = float(input("Enter height in inches: ")) / 39.372
height = height_f + height_i
bmi = weight / (height ** 2)
print(f"Your BMI is: {bmi}")

weight = float(input("Enter weight in lb: ")) / 2.2
height_f = float(input("Enter height in feet: ")) / 3.281
height_i = float(input("Enter height in inches: ")) / 39.372
height = height_f + height_i
bmi = weight / (height ** 2)
print(f"Your BMI is: {bmi}")

################################################

11. Heart Rate Zones Calculator

32

188 bpm

< 94         ( sit )

> 94         ( walk )

> 131 bpm    ( run )


64

< 78         ( sit )

> 78         ( walk )

> 109 bpm    ( run )

50 %

10 ?      = 10 * 50 / 100 = 5
100?      = 1000 * 50 / 100 = 500

10 ?      = 10 * 0.5 = 5
100?      = 1000 * 0.5 = 500

age = int(input("Enter your age: "))
max_heart_rate = 220 - age

print(f"Maximum Heart Rate: {max_heart_rate} bpm")
print(f"Fat Burn Zone (50-70%): {max_heart_rate * 0.5} - {max_heart_rate * 0.7} bpm")
print(f"Cardio Zone (70-85%): {max_heart_rate * 0.7} - {max_heart_rate * 0.85} bpm")
print(f"Peak Zone (85-100%): {max_heart_rate * 0.85} - {max_heart_rate} bpm")

summation 4 = 1 + 2 + 3 + 4 = 10

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
print("Gravitational Force:", G * (m1 * m2) / (r ** 2), "N")

################################################

18. Kinetic Energy ( 1/2.m.v**2 )

mass = float(input("Enter mass (kg): "))
velocity = float(input("Enter velocity (m/s): "))
print("Kinetic Energy:", 0.5 * mass * velocity ** 2, "J")

################################################

19. Potential Energy

mass = float(input("Enter mass (kg): "))
height = float(input("Enter height (m): "))
g = 9.81
ans = mass * g * height
print("Potential Energy:", ans, "J")

################################################

20. Power Calculation (Electrical Power)

voltage = float(input("Enter voltage (V): "))
current = float(input("Enter current (A): "))

print("Power:", voltage * current, "W")

################################################

21. Frequency and Wavelength (Wave Equation)

speed = float(input("Enter wave speed (m/s): "))
wavelength = float(input("Enter wavelength (m): "))
print("Frequency:", speed / wavelength, "Hz")

################################################

22. Momentum

mass = float(input("Enter mass (kg): "))
velocity = float(input("Enter velocity (m/s): "))
print("Momentum:", mass * velocity, "kg·m/s")

################################################

23. Ideal Gas Law Calculator (PV = nRT)

V = float(input("Enter volume (L): "))
n = float(input("Enter number of moles: "))
R = 0.0821  # Gas constant (L·atm/mol·K)
T = float(input("Enter temperature (K): "))
print("Pressure:", (n * R * T) / V, "atm")

################################################

24. Percentage Composition

element_mass = float(input("Enter mass of the element (g): "))
compound_mass = float(input("Enter total mass of the compound (g): "))
print("Percentage composition:", (element_mass / compound_mass) * 100, "%")

################################################

25. Heat Energy Calculation (q = mcΔT) (mass * specific_heat * temp_change)

mass = float(input("Enter mass (g): "))
specific_heat = float(input("Enter specific heat capacity (J/g·°C): "))
temp_change = float(input("Enter temperature change (°C): "))
print("Heat energy:", mass * specific_heat * temp_change, "J")

################################################

26. Avogadro’s Law Calculator (V1/n1 = V2/n2)    (1g/? = 10g/1000)

V1 = float(input("Enter initial volume (L): "))
n1 = float(input("Enter initial moles: "))
n2 = float(input("Enter final moles: "))
print("Final volume:", (V1 * n2) / n1, "L")

################################################

27. Running Pace Calculator

distance = float(input("Enter distance in kilometers: "))
time_minutes = float(input("Enter time taken in minutes: "))

pace = time_minutes / distance
print(f"Your running pace is {pace:.2f} minutes per km.")

################################################

28. Fuel Efficiency Converter (L/100km to MPG) (miles per gallon)

liters_per_100km = float(input("Enter fuel efficiency in L/100km: "))
mpg = 235.215 / liters_per_100km

print(mpg, "MPG")

################################################

29. Square Root Calculator

number = float(input("Enter a number: "))
sqrt = number ** (1/2)
print(f"The square root of {number} is {sqrt}")

# Cube Root Calculator
number = float(input("Enter a number: "))
print(f"The cube root of {number} is {number ** (1/3)}")

################################################

30. Simple Interest  ( (p * r * t) / 100 )

principal amount ( the beginning balance )
interest rate ( per year )  ( "100 %" means that "/ 100" ) ( 1% --> 1/100 )
time ( number of time periods ) ( always 1 year )

100_000
10 %    
1year -> 100_000 + 10_000

100000
10%    ->  100000 * 10/100 
10%    ->  100000 * 0.1     => 10000
5 years                     => 10000 * 5

p = float(input("Enter principal amount: "))
r = float(input("Enter interest rate (%): ")) / 100  # 0.1, 0.2
t = float(input("Enter time (years): "))
print("Simple Interest:", p * r * t)

################################################

31. compound interest (10%)

100_000
1 years => 100_000 + 10_000 => 110_000
2 years => 110_000 + 11_000 => 121_000
3 years => 121_000 + 12_100 => 133_100

################################################

p = 100_000

i = p * 0.1             # 10000
p = p + i               # 110000
print(f"1 year = {p}")

i = p * 0.1             # 11000
p = p + i               # 121000
print(f"2 year = {p}")

i = p * 0.1             # 12100
p = p + i               # 133100
print(f"3 year = {p}")

i = p * 0.1             # 12100
p = p + i               # 133100
print(f"4 year = {p}")

i = p * 0.1             # 12100
p = p + i               # 133100
print(f"5 year = {p}")

################################################

p = float(input("Enter principal amount: "))
r = float(input("Enter interest rate (%): ")) / 100 
t = int(input("Enter time (years): "))

for n in range(1, t+1):
    i = p * r
    p = p + i  
    print(f"{n} year = {p}")

################################################

32. 

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

################################################

for r in range(1, 13):
    print(f"1 * {r} = {1 * r}")

print("- " * 40)

for n in range(1, 13):
    print(f"2 * {n} = {2 * n}")

print("- " * 40)

for n in range(1, 13):
    print(f"3 * {n} = {3 * n}")

print("- " * 40)

for n in range(1, 13):
    print(f"4 * {n} = {4 * n}")
    
################################################

for l in range(1, 13):
    for r in range(1, 13):
        print(f"{l} * {r} = {l * r}")

    print("- " * 40)

################################################################################################

"""

