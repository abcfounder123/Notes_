"""

Function
- readability

################################################

1. effect only

def c_f(celcius):
    fahrenheit = (celcius * 9 / 5) + 32
    ans = f"{celcius} °C is equal to {fahrenheit} °F."
    print(ans)

################################################    

2. result only  ( pure function )

def c_f(celcius):
    fahrenheit = (celcius * 9 / 5) + 32
    return fahrenheit
    
################################################

3. effect & results

def c_f(celcius):
    fahrenheit = (celcius * 9 / 5) + 32
    ans = f"{celcius} °C is equal to {fahrenheit} °F."
    print(ans)
    return fahrenheit
    
################################################

4. Normal usage

# collection of code
def c_f():
    celcius = int(input("Enter degree celcius : "))
    fahrenheit = (celcius * 9 / 5) + 32
    ans = f"{celcius} °C is equal to {fahrenheit} °F."
    print(ans)

# parameterized function
def c_f(celcius):
    fahrenheit = (celcius * 9 / 5) + 32
    ans = f"{celcius} °C is equal to {fahrenheit} °F."
    print(ans)

# normal usage.1
def c_f(celcius):
    fahrenheit = (celcius * 9 / 5) + 32
    return fahrenheit

# normal usage.2
def c_f(celcius):
    return (celcius * 9 / 5) + 32

################################################

# 8 steps
def c_f(celcius):
    fahrenheit = (celcius * 9 / 5) + 32
    return fahrenheit
    

c_f(100)

1. 100                int()

2. c_f()

3. celcius = 100      assign

4. 3  -> * /          mul, div
   4  -> +            add
   14 -> =            assign
   
5. return

################################################

# 7 steps
def c_f(celcius):
    return (celcius * 9 / 5) + 32
    
    
c_f(100)

1. 100                int()

2. c_f()

3. celcius = 100      assign

4. 3  -> * /          mul, div
   4  -> +            add
   
5. return

################################################

2024.xlsh

No   Date             Temperature(C)  Temperature(F)
1    1.1.2024(6:00)       27              80.6
2    1.1.2024(12:00)      30              86.0
3    1.1.2024(22:00)      29

################################################

1. normal

def c_f(celcius):
    return (celcius * 9 / 5) + 32


c = [27, 30, 29, 28, 31, 26, 25, 29, 26]
f = []

f.append(c_f(c[0]))
f.append(c_f(c[1]))
f.append(c_f(c[2]))
f.append(c_f(c[3]))
f.append(c_f(c[4]))
f.append(c_f(c[5]))
f.append(c_f(c[6]))
f.append(c_f(c[7]))
f.append(c_f(c[8]))

print(f)

################################################

2. original for loop


for x in c:
    f.append(c_f(x))

print(f)


################################################

3. for loop (indexing)

for n in range(9):
    f.append(c_f(c[n]))

print(f)


################################################

# Python style Vs C style

# 2 steps
f.append(c_f(x))
1. c_f
2. append

# 3 steps
f.append(c_f(c[n]))
1. c[n]    ->  get
2. c_f
3. append

################################################

4. Write for all data (3 months data, one year data, 10 years data)


for x in c:
    f.append(c_f(x))
    

for n in range(len(c)):
    f.append(c_f(c[n]))


################################################################################################


"""

