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

"""

