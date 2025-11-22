
"""

Procedural programming
1. sequence  (top, left, p)
2. selection (if, elif, else)
3. looping   (for, while)
4. function (Procedure)

################################################

Day.13 (looping) (control flow)

1. looping, iteration
2. nested loop
3. for and range
4. for and indexing, indexing by length
5. for and break ( °C )
6. While loop
7. Control Flow
8. Function

################################################

1. looping, iteration

x = "Temperature 100°C." # 18

for i in x: # i = T, i = e
    print(i)


x = ["apple", "banana", 'orange']

for i in x:
    print(i)
    

x = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for i in x:
    print(i)

################################################

2. nested loop

x = ["apple", "banana", 'orange']

for i in x: # "apple"
    print(i)
    for j in i:
        print(j)

################################################

3. for and range

x = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for i in x:
    print(i)

for i in range(0, 11, 1):
    print(i)
    
    
for i in range(11):
    print(i)
    
    
# iteration ( 1 to 10 )
for i in range(1, 11):
    print(f"{i}.Hello")

# looping (5 times)
for _ in range(5):
    print("Hello")
    print('- ' * 42)



for i in range(100):
    pass


for _ in range(100):
    pass

################################################

4. for and indexing, indexing by length

x = "Temperature 100°C." # 0 to 17

for i in range(18): # 0 to 17
    print(x[i])


x = "Temperature 100°C." # 0 to 17

for i in range(len(x)): # 0 to 17
    print(x[i])

################################################

5. for and break ( °C )
        
x = "Temperature 100°C. I want Fahrenheit." # 0 to 36

for i in range(len(x)): # 37
    print(i)
    if x[i] == '°' and x[i+1] == "C":
        print("We found °C at", i)
        break

################################################

x = "Temperature 100°C. I want Fahrenheit.100°C  100°C 100°C 100°C"  # 0 to 36
n = 0

for i in range(len(x)):  # 37
    print(i)
    if x[i] == '°' and x[i + 1] == "C":
        print("We found °C at", i)
        n += 1
        if n >= 2: break

################################################################################################

6. While loop


if condition:
    pass

while condition:
    pass
    
################################################    

condition = False

while not condition:
    user_name = input("User name = ")
    password = input("Password = ")

    if user_name == "Mg Mg" and password == "123456":
        print("Facebook open.")
        condition = True

    else:
        print("Try again.")
        
################################################
        
c = ""        
        
x[13]
"" + "3" = "3"

x[12]
"3" + "2" = "32"
"2" + "3" = "23"

x[11]
"1" + "23" = "123"

################################################

x = "Temperature 11027°C. I want Fahrenheit." 

p = 17
n = 1
t = ""

while x[p-n] in "0123456789":
    t = x[p-n] + t  # "7" => "27" => "027" => "1027" => "11027"
    n += 1

print(t) # "11027"

################################################################################################

7. Control Flow

x = "Temperature 100°C. I want Kelvin."  # 14

for i in range(len(x)): # 37
    # print(i)
    if x[i] == '°' and x[i+1] == "C":
        print("We found °C at", i)

        p = i
        n = 1
        t = ""

        while x[p - n] in "0123456789":
            t = x[p - n] + t  # "7" => "27"
            n += 1

        print("Temperature value in °C =", t)
        print("Temperature value in Kelvin =", float(t) + 273)

################################################

Temperature 100°C. I want Kelvin.
Temperature 100°C. I want Fahrenheit.

################################################

x = input("Chat gpt => ") # Temperature 100°C. I want Fahrenheit.

for i in range(len(x)): # 37
    if x[i] == '°' and x[i+1] == "C":
        p = i
        n = 1
        t = ""

        while x[p - n] in "0123456789":
            t = x[p - n] + t  # "100"
            n += 1

        celsius = float(t) # "100"  => 100.0

        if "Kelvin" in x:
            print("Temperature value in Kelvin =", celsius + 273)

        if "Fahrenheit" in x:
            print("Temperature value in Fahrenheit =", (celsius * 9 / 5) + 32)

################################################

Floating-point value  => "0123456789."

x = input("Chat gpt => ") # Temperature 100°C. I want Fahrenheit.

for i in range(len(x)): # 37
    if x[i] == '°' and x[i+1] == "C":
        p = i
        n = 1
        t = ""

        while x[p - n] in "0123456789.":
            t = x[p - n] + t  # "100"
            n += 1

        celsius = float(t) # "100"  => 100.0

        if "Kelvin" in x:
            print("Temperature value in Kelvin =", celsius + 273)

        if "Fahrenheit" in x:
            print("Temperature value in Fahrenheit =", (celsius * 9 / 5) + 32)

################################################

8. Function


def c_kf():
    x = input("Chat gpt => ")  # Temperature 100°C. I want Fahrenheit.

    for i in range(len(x)):  # 37
        if x[i] == '°' and x[i + 1] == "C":
            p = i
            n = 1
            t = ""

            while x[p - n] in "0123456789.":
                t = x[p - n] + t  # "100"
                n += 1

            celsius = float(t)  # "100"  => 100.0

            if "Kelvin" in x:
                print("Temperature value in Kelvin =", celsius + 273)

            if "Fahrenheit" in x:
                print("Temperature value in Fahrenheit =", (celsius * 9 / 5) + 32)


while True:
    c_kf()
    ans = input("Do you want to stop? (yes/no)\n>> ")
    if ans == "yes":
        break

################################################################################################

"""


