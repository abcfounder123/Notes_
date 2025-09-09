"""

A. Creating six kinds of parameterized functions        
   (standard function & lambda function) 

B. Tuple packing and unpacking of collections 

C. Control flow and function exercises 
   - Handling Excel data 
   - tac ti toe 


################################################

A. Creating six kinds of parameterized functions        
   (standard function & lambda function) 

1. standard/ normal parameter  


def add(a, b):
    return a + b


ans = add(1, 2)
print(ans)


def linear(a, b, c):
    return a ** 2 + b ** 2 + c


ans = linear(3, 2, 1)
print(ans)

################################################

2. default parameter


def linear(a, b, c=0):
    return a ** 2 + b ** 2 + c


ans = linear(3, 2)
print(ans)

################################################

3. positional only parameter  

def add(a, b, /):
    return a + b


ans = add(1, 2)
print(ans)

################################################

4. keword only parameter

def linear(*, a, b, c=0):
    return a ** 2 + b ** 2 + c


ans = linear(a=3, b=2)
print(ans)


################################################

5. variable-length positional parameter
 
def add(*numbers): # (1, 2, ...)
    t = 0
    for n in numbers:
        t += n
    return t


d = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100]

ans = add(*d) 
print(ans)

################################################

6. variable-length keyword parameter 


def linear(**features):
    print(features)


ans = linear(room=3, bath=4, air=4, city="")
print(ans)

################################################

B. Tuple packing and unpacking of collections 

packing    -> tuple
unpacking  -> collection

print([1, 2, 3])
print(1, 2, 3)

d = [1, 2, 3]
print(d)
print(*d)

################################################

lambda

1. lambda function
2. anonymous one-line function
3. inline function
4. function literal ( mathematical function )
5. expression function
6. throwaway function
7. arrow function ( => ) ( in js )

name             -> add
parameter list   -> (a, b)
result           -> a + b

################################################

1. standard/ normal parameter  

def add(a, b):
    return a + b


add2 = lambda a, b: a + b

################################################

2. default parameter

parameter list -> (a, b, c=0)
result         -> a ** 2 + b ** 2 + c


def linear(a, b, c=0):
    return a ** 2 + b ** 2 + c


linear = lambda a, b, c=0: a ** 2 + b ** 2 + c

################################################

3. positional only parameter  

parameter list -> (a, b, /)
result         -> a + b


def add(a, b, /):
    return a + b


add = lambda a, b, /: a + b

################################################

4. keword only parameter

parameter list -> (*, a, b, c=0)
result         -> a ** 2 + b ** 2 + c


def linear(*, a, b, c=0):
    return a ** 2 + b ** 2 + c


linear = lambda *, a, b, c=0: a ** 2 + b ** 2 + c 

################################################

5. variable-length positional parameter

parameter list -> (*numbers)
result         ->  t

 
def add(*numbers): # (1, 2, ...)
    t = 0
    for n in numbers:
        t += n
    return t
    
    
add = lambda *numbers: result by list comprehension

d = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100]

ans = add(*d) 
print(ans)

################################################

6. variable-length keyword parameter 

parameter list -> (**features)
result         ->  result
effect         ->  print(features)


def linear(**features):
    print(features)


linear = lambda **features: print(features)  

ans = linear(room=3, bath=4, air=4, city="")
print(ans)

################################################################################################

C. Control flow and function exercises 
   - Handling Excel data 
  

Input Data

2024.xlsh
No   Date             Temperature(C)  
1    1.1.2024(6:00)       27              
2    1.1.2024(12:00)      30              
3    1.1.2024(22:00)      29

################################################

Output Data

t2.xlsh
No   Date             Temperature(C)  Temperature(F)
1    1.1.2024(6:00)       27              80.6
2    1.1.2024(12:00)      30              86.0
3    1.1.2024(22:00)      29

################################################

Sample Data

2024.xlsx

No   Date             Temperature(C)  

1    1.1.2024(6:00)       27         
2    1.1.2024(12:00)      30              
3    1.1.2024(22:00)      29

################################################

1. Creating data frame

   No             Date  Temperature(C)
0   1   1.1.2024(6:00)              27
1   2  1.1.2024(12:00)              30
2   3  1.1.2024(22:00)              29


pandas.DataFrame(t_2024)

################################################

2. Creating excel file

to_excel("file_name.xlsx")

################################################

import pandas

t1 = {"No": 1, "Date": "1.1.2024(6:00)", "Temperature(C)": 27}
t2 = {"No": 2, "Date": "1.1.2024(12:00)", "Temperature(C)": 30}
t3 = {"No": 3, "Date": "1.1.2024(22:00)", "Temperature(C)": 29}

t_2024 = [t1, t2, t3]

d = pandas.DataFrame(t_2024)
d.to_excel("t2_2024.xlsx")

################################################

3. Reading data from excel file

read_excel("file_name")

################################################

4. Checking columns' data

print(t) # all
print(t["Date"])
print(t["Temperature(C)"])

################################################

5. Creating list by using column' data

list(t["column name"])

[t["column name"]]

################################################

6. Creating new column

t["new column name"] = f

################################################

7. Deleting old column

del t["Temperature(C)"]

################################################

8. Creating new excel file

to_excel("new_file_name.xlsx")

################################################


import pandas


def c_f(celcius):
    return (celcius * 9 / 5) + 32


t = pandas.read_excel("t_2024.xlsx")
c = list(t["Temperature(C)"])  # [27, 30, 29]
f = []                         # [80.6, 86.0, 84.2]

for x in c:
    f.append(c_f(x))

t["F"] = f
del t["Temperature(C)"]
t.to_excel("t2_2024.xlsx")

################################################

9.Creating function


def e_c(*, file_name, column_name, fun, new_column_name, new_file_name=None, del_old_column=False):

    import pandas

    t = pandas.read_excel(file_name)

    c = list(t[column_name])
    f = []

    for x in c:
        f.append(fun(x))

    t[new_column_name] = f

    if del_old_column: del t[column_name]

    if new_file_name:
        t.to_excel(new_file_name)
    else:
        t.to_excel(file_name)


################################################################################################

10. Using function

# C to F, new file, delete old column
e_c(file_name="t_2024.xlsx", column_name="Temperature(C)", fun=lambda celcius: (celcius * 9 / 5) + 32, new_column_name="Degree Fahrenheit", new_file_name="2024 Temperature in Degree Fahrenheit.xlsx", del_old_column=True)

# C to C-1 because of wrong sensor
e_c(file_name="t_2024.xlsx", column_name="Temperature(C)", fun=lambda celcius: celcius - 1, new_column_name="Temperature(C)")

# F to C, new file with two colums
e_c(file_name="2024 Temperature in Degree Fahrenheit.xlsx", column_name="Degree Fahrenheit", fun=lambda f:(f - 32) * 5 / 9, new_column_name="Degree Celsius", new_file_name="2024 Temperature in degree F & C.xlsx")

################################################################################################

Control flow and function exercises 
   - tac ti toe 

တစ်တီတူး သင်ခန်းစာများစုစည်းမှု 

1. လူနှစ်ယောက်ဆော့ဖို့ ရေးသားခြင်း

2. လူနဲ့ ကွန်ပြူတာဆော့ဖို့ ရေးသားခြင်း

3. tkinter သုံးပြီး window application ရေးသားခြင်း

အထက်ပါ အပိုင်းသုံးပိုင်း ပါဝင်ပါတယ်။

( နည်းနည်းလောက် သိထားရင်ပဲ လိုက်လုပ်လို့ ရပါတယ်။ )

###########################

lesson.1  လူနှစ်ယောက်ဆော့ဖို့ရေးသားခြင်း

https://m.youtube.com/watch?feature=youtu.be&v=De4mVPvcdoU

( lesson.1 source code )

https://m.facebook.com/groups/2255969184681998/permalink/3171142789831295/

###########################

lesson.2 လူနဲ့ကွန်ပြူတာဆော့ဖို့ရေးသားခြင်း

https://m.youtube.com/watch?feature=youtu.be&v=K19iVkLvLxs

###########################

lesson.3 tkinter သုံးပြီး window application ရေးသားခြင်း

lesson.1  ( GUI ဖန်တီးခြင်း )

https://youtu.be/HpulS6htG90

lesson.2   ( winner သတ်မှတ်ခြင်း )

https://youtu.be/uBsEscClp8g

lesson.3  ( သရေသတ်မှတ်ခြင်း ) ( application ထုတ်ခြင်း )

https://youtu.be/uZIL0G5mxJA
  
################################################################################################

"""
