
"""
Day.15

Looping
1. Iteration, Looping
2. Nested loop
3. for and range
4. for and indexing, indexing by length  (range(length))
5. for and break
6. for and count
7. for, count, break
8. while
9. for + while
10. Control flow (while, if, for)
11. while and break
12. while and count
13. while, count, break

Looping
- for
  - Iteration
  - Definite Looping
  
- while (True)
  - Indefinite Looping

################################################

user_name = input("User name = ")
password = input("Password = ")

if user_name == "Mg Mg" and password == "12345":
    print("Facebook account of Mg Mg is opened.")

################################################

condition = True

while condition:
    user_name = input("User name = ")
    password = input("Password = ")

    if user_name == "Mg Mg" and password == "12345":
        print("Facebook account of Mg Mg is opened.")
        condition = False
         
################################################

condition = False

while not condition:
    user_name = input("User name = ")
    password = input("Password = ")

    if user_name == "Mg Mg" and password == "12345":
        print("Facebook account of Mg Mg is opened.")
        condition = True

################################################

°C  => iterate (for + index)

################################################

x = "Temperature 156°C."

for i in range(len(x)):
    if x[i] == "°" and x[i+1] == "C":
        print(i)
 
################################################
 
156  => indefinite loop (while)

################################################
 
x = "Temperature 156°C."

p = 15
n = 1
temperature = ""

while x[p-n] in "0123456789":
    temperature = x[p-n] + temperature
    n += 1

print(temperature)  

################################################

9. for + while

x = "Temperature 100°C.I want Kelvin."

for i in range(len(x)):
    if x[i] == "°" and x[i+1] == "C":
        p = i  # 15
        n = 1
        temperature = ""

        while x[p - n] in "0123456789":
            temperature = x[p - n] + temperature # "6" + "" -> "5" + "6" -> "1" + "56" -> "156"
            n += 1

        print("Temperature value in °C =", temperature)
        c = int(temperature)
        print("Temperature value in Kelvin =", c + 273)
        print("Temperature value in °F =", (c * 9 / 5) + 32)

################################################

10. Control flow (while, if, for)


x = "Temperature 100°C.I want Kelvin.I want Fahrenheit."

for i in range(len(x)):
    if x[i] == "°" and x[i+1] == "C":
        p = i  # 15
        n = 1
        temperature = ""

        while x[p - n] in "0123456789":
            temperature = x[p - n] + temperature # "6" + "" -> "5" + "6" -> "1" + "56" -> "156"
            n += 1

        print("Temperature value in °C =", temperature)
        c = int(temperature)

        if "Kelvin" in x:print("Temperature value in Kelvin =", c + 273)
        if "Fahrenheit" in x:print("Temperature value in °F =", (c * 9 / 5) + 32)

################################################

float

x = "Temperature 27.5°C.I want Kelvin.I want Fahrenheit."

for i in range(len(x)):
    if x[i] == "°" and x[i+1] == "C":
        p = i  # 15
        n = 1
        temperature = ""

        while x[p - n] in "0123456789.":
            temperature = x[p - n] + temperature # "6" + "" -> "5" + "6" -> "1" + "56" -> "156"
            n += 1

        print("Temperature value in °C =", temperature)
        c = float(temperature)

        if "Kelvin" in x:print("Temperature value in Kelvin =", c + 273)
        if "Fahrenheit" in x:print("Temperature value in °F =", (c * 9 / 5) + 32)

################################################

Temperature 27.5°C.I want Kelvin.
Temperature 27.5°C.I want Fahrenheit.
Temperature 27.5°C.I want Kelvin.I want Fahrenheit.
Convert 27.5°C to Fahrenheit.

################################################

x = input("Chat gpt = ")

for i in range(len(x)):
    if x[i] == "°" and x[i+1] == "C":
        p = i  # 15
        n = 1
        temperature = ""

        while x[p - n] in "0123456789.":
            temperature = x[p - n] + temperature # "6" + "" -> "5" + "6" -> "1" + "56" -> "156"
            n += 1

        print("Temperature value in °C =", temperature)
        c = float(temperature)

        if "Kelvin" in x:print("Temperature value in Kelvin =", c + 273)
        if "Fahrenheit" in x:print("Temperature value in °F =", (c * 9 / 5) + 32)

################################################

Convert 27.5°F to Celsius.

################################################

x = input("Chat gpt = ")

for i in range(len(x)):
    if x[i] == "°" and x[i+1] == "F":
        p = i  # 15
        n = 1
        temperature = ""

        while x[p - n] in "0123456789.":
            temperature = x[p - n] + temperature # "6" + "" -> "5" + "6" -> "1" + "56" -> "156"
            n += 1

        print("Temperature value in °F =", temperature)
        f = float(temperature)

        if "Kelvin" in x:print("Temperature value in Kelvin =", ((f - 32) * 5 / 9) + 273)
        if "Celsius" in x:print("Temperature value in °C =", (f - 32) * 5 / 9)

################################################

11. while and break

if ans == "y": break


while True:
    x = input("Chat gpt = ")

    for i in range(len(x)):
        if x[i] == "°" and x[i + 1] == "F":
            p = i  # 15
            n = 1
            temperature = ""

            while x[p - n] in "0123456789.":
                temperature = x[p - n] + temperature  # "6" + "" -> "5" + "6" -> "1" + "56" -> "156"
                n += 1

            print("Temperature value in °F =", temperature)
            f = float(temperature)

            if "Kelvin" in x: print("Temperature value in Kelvin =", ((f - 32) * 5 / 9) + 273)
            if "Celsius" in x: print("Temperature value in °C =", (f - 32) * 5 / 9)

    ans = input("Quit? (y/n) = ")
    
    if ans == "y":
        break
        
################################################

12. while and count

condition = True
c = 0

while condition:
    user_name = input("User name = ")
    password = input("Password = ")

    c += 1

    if user_name == "Mg Mg" and password == "12345":
        print("Facebook account of Mg Mg is opened.")
        condition = False

    elif c == 3:
        print("Wait 24 hours.Lock.")  # false +  3
        condition = False

################################################

13. while, count, break

c = 0

while True:
    user_name = input("User name = ")
    password = input("Password = ")

    c += 1

    if user_name == "Mg Mg" and password == "12345":
        print("Facebook account of Mg Mg is opened.")
        break

    elif c == 3:
        print("Wait 24 hours.Lock.")  # false +  3
        break

################################################

Procedural programming
1. Sequence (t, l, p)
2. Selection (if, else, elif)
3. Looping   (for, while)
4. function  (procedure for login, procedure for length)

################################################


def f_ck():
    x = input("Chat gpt = ")

    for i in range(len(x)):
        if x[i] == "°" and x[i + 1] == "F":
            p = i  # 15
            n = 1
            temperature = ""

            while x[p - n] in "0123456789.":
                temperature = x[p - n] + temperature  # "6" + "" -> "5" + "6" -> "1" + "56" -> "156"
                n += 1

            print("Temperature value in °F =", temperature)
            f = float(temperature)

            if "Kelvin" in x: print("Temperature value in Kelvin =", ((f - 32) * 5 / 9) + 273)
            if "Celsius" in x: print("Temperature value in °C =", (f - 32) * 5 / 9)


################################################


def login():
    condition = True
    c = 0

    while condition:
        user_name = input("User name = ")
        password = input("Password = ")

        c += 1

        if user_name == "Mg Mg" and password == "12345":
            print("Facebook account of Mg Mg is opened.")
            condition = False

        elif c == 3:
            print("Wait 24 hours.Lock.")  # false +  3
            condition = False


def length(x):
    t = 0
    for _ in x:
        t += 1
    return t
    

x = "abffdhgfjgc"
y = "abffdhgfjgtydytdtdc"
print(length(x), length(y))

################################################################################################

"""
