"""
Function

1. collection of code

def c_f():
    celcius = int(input("Enter degree celcius : "))
    fahrenheit = (celcius * 9 / 5) + 32
    ans = f"{celcius} °C is equal to {fahrenheit} °F."
    print(ans)
    
################################################

2. parameterized function

def c_f(celcius):
    fahrenheit = (celcius * 9 / 5) + 32
    ans = f"{celcius} °C is equal to {fahrenheit} °F."
    print(ans)
    
################################################

3. pure function

def c_f(celcius):
    fahrenheit = (celcius * 9 / 5) + 32
    return fahrenheit

def c_f(celcius):
    return (celcius * 9 / 5) + 32

################################################    

# iteration
for n in range(1000): # 0 to 999 -> 1000
    print(n, "apple")


# repeatation purpose
for _ in range(1000): # 0 to 999 -> 1000
    print("apple")
    
################################################

def c_f(celcius):
    fahrenheit = (celcius * 9 / 5) + 32
    ans = f"{celcius} °C is equal to {fahrenheit} °F."
    print(ans)


celsius_list = [27, 30, 26, 28, 32, 29, 29, 30, 27, 27, 30, 26, 28, 32, 29, 29, 30, 27, 27, 30, 26, 28, 32, 29, 29, 30, 27, 27, 30, 26, 28, 32, 29, 29, 30, 27, 27, 30, 26, 28, 32, 29, 29, 30, 27, 27, 30, 26, 28, 32, 29, 29, 30, 27]

for i in celsius_list:
    c_f(i)
    
################################################    
    
function    ---> collection of code    
c_f         ---> function name    
()          ---> parameter list/tuple
celcius     ---> first parameter

################################################

def add(n1, n2):
    print(n1 + n2)

add         ---> function name    
()          ---> parameter list/tuple
n1          ---> first parameter
n2          ---> second parameter

################################################

Parameters

1. normal parameter                               (x, y)
2. default parameter                              (x, y, b=0)
3. positional only parameter                      (x, y, /)       2
4. keword only parameter                          (*, x, y)
5. variable-length positional parameter 
6. variable-length keyword parameter  

################################################

x ** 2 + y ** 2 + b
x ** 2 + y ** 2 + 0

def f(x, y, b=0):
    z = x ** 2 + y ** 2 + b
    print(z)
    
################################################

f           ---> function name    
()          ---> parameter list/tuple
x           ---> first parameter       normal parameter       x
y           ---> second parameter      normal parameter       y
b           ---> third parameter       default parameter      b=0
0           ---> default value

################################################

Standard form
1. assign value by position
2. assign value by keyword name
3. assign value by position and keyword name

################################################

2. default parameter

def add(n1, n2):
    print(n1 + n2)


add(3, 4) # assign value by position
add(n1=3, n2=4) # assign value by keyword name
add(3, n2=4) # assign value by position and keyword name

################################################

3. positional only parameter

def add(n1, n2, /):
    print(n1 + n2)

add          ---> function name    
()           ---> parameter list/tuple
n1           ---> first parameter       normal parameter       x
n2           ---> second parameter      normal parameter       y
/            ---> third parameter       positional only parameter  /

################################################

4. keword only parameter

def add(*, n1, n2): 
    print(n1 + n2)

add          ---> function name    
()           ---> parameter list/tuple
*            ---> first parameter        keword only parameter  *
n1           ---> second parameter       normal parameter       x
n2           ---> third parameter        normal parameter       y

################################################




"""