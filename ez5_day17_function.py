
"""

Procedural programming
1. Sequence (top, left, p)
2. Selection (if, else, elif)
3. Loop      (for, while)
4. Function

################################################

1. Function introduction
- print(), int(), len(), int(input())
- Function invoke, Function call
- Why?
  - 1. Readability, reuse
  - 2. Decomposition 
- Where?
  - 1. built-in module       - direct
  - 2. preinstalled module   - math.sqrt(16)
  - 3. external module       - 650000
 
2. Module, package and framwork 
- function (collection of program)        (one purpose - add(), sub(), sqrt()) 
- module   (file)(collection of fun)      (one work - math.py, login.py)
- package  (folder)(collection of module) (one group - frontend folder)
- framwork (folder)(collection of folder) (one project)
 
3. Function name 
- function name (naming rules)
- same name (last one)
- should not give the same name

4. Parameterized function
- parameterized function  => add(x, y)
- parameter list          => (x, y)
- first parameter         =>  x

5. Argument
- positional arguments    => add(1, 2)
- 1st positional argument => 1 
- keyword arguments       => add(x=1, y=2)
- keyword arguments of x  => 1

6. Global and Local
- global variable  => all
- local variable   => local
- same name of global and local => local first -> global -> built-in

7. Standard form (3)

8. Types of arameters (6)

################################################

1. Function introduction

dollar = int(input("Dollar = "))
kyats = dollar * 5000
print("Kyats =", kyats)

dollar = int(input("Dollar = "))
kyats = dollar * 5000
print("Kyats =", kyats)

dollar = int(input("Dollar = "))
kyats = dollar * 5000
print("Kyats =", kyats)

dollar = int(input("Dollar = "))
kyats = dollar * 5000
print("Kyats =", kyats)

dollar = int(input("Dollar = "))
kyats = dollar * 5000
print("Kyats =", kyats)

################################################

dollar = float(input("Dollar = "))
kyats = dollar * 5000
print("Kyats =", kyats)

dollar = float(input("Dollar = "))
kyats = dollar * 5000
print("Kyats =", kyats)

dollar = float(input("Dollar = "))
kyats = dollar * 5000
print("Kyats =", kyats)

dollar = float(input("Dollar = "))
kyats = dollar * 5000
print("Kyats =", kyats)

dollar = float(input("Dollar = "))
kyats = dollar * 5000
print("Kyats =", kyats)

################################################

dollar = float(input("Dollar = "))
kyats = dollar * 5000
print(f"{dollar} is {kyats}Kyats.")

################################################

def dollar_kyats():
    dollar = int(input("Dollar = "))
    kyats = dollar * 5000
    print("Kyats =", kyats)
    

dollar_kyats()
dollar_kyats()
dollar_kyats()
dollar_kyats()
dollar_kyats()

################################################

def dollar_kyats():
    dollar = float(input("Dollar = "))
    kyats = dollar * 5000
    print("Kyats =", kyats)
    

dollar_kyats()
dollar_kyats()
dollar_kyats()
dollar_kyats()
dollar_kyats()

################################################

def dollar_kyats():
    dollar = float(input("Dollar = "))
    kyats = dollar * 5000
    print(f"{dollar} is {kyats}Kyats.")
    

dollar_kyats()
dollar_kyats()
dollar_kyats()
dollar_kyats()
dollar_kyats()

################################################

2. Module, package and framwork 

- function (collection of program)        (one purpose - input_username()) 
- module   (file)(collection of fun)      (one work - login.py)
- package  (folder)(collection of module) (one group - frontend folder)
- framwork (folder)(collection of folder) (one project)
 
1. input_username()
2. login.py
3. Flask, Bottle (backend)
4. Django (one project)

frontend
- login.py     100 + input_username()
- post.py      100
- react.py     100

database
- sql.py       100
- nosql.py     100

backend
- user.py      100
- admin.py     100

################################################

4. Parameterized function

parameterized function  => add(x, y)
parameter list          => (x, y)  <--- tuple
first parameter         =>  x
second parameter        =>  y

def add(x, y):
    print(x + y)


add(1, 2)

################################################

7. Standard form (3)

1. positional only
2. keyword only
3. pos + kw


def add(x, y):
    print(x + y)


add(1, 2)
add(x=1, y=2)
add(1, y=2)

################################################

8. Types of parameters (6)

1. Normal parameters                                  (x, y)
2. Default parameters                                 (x, y=0)
3. Positional only parameters                         (x, y, /)
4. Keyword only parameters                            (*, x, y)
5. Variable-length positional only parameters         (*x)
6. Variable-length keyword only parameters            (**x)

################################################

Day.18

Function
1. Function define      =>   def
2. Function name        =>   add
3. Parameter list       =>   ()
4. Parameters           =>   n1, n2
5. Code block           =>   :
6. Documentation string =>   triple quotes (help, doc)
7. Function body        =>   programs , ans = n1 + n2
8. return statement     =>   stop, return value

help()
1. Function name
2. Parameter list
3. documentation string 

doc
1. documentation string

################################################


def add(n1, n2):
    '''documentation string'''
    ans = n1 + n2
    return ans


################################################

1. Normal parameters, Standard parameters (x, y)


def add(x, y):
    return x + y
    
    
add(1, 2)
add(x=1, y=2)
add(1, y=2)


################################################

2. Default parameters (x, y=10)

y = Default parameters 
10 = Default value, Default arguments


def add(x, y=10):
    return x + y


print(add(1))
print(add(1, 2))

################################################

formula = x**2 + y++2 + a


def f(x, y, a=0):
    return x**2 + y++2 + a
    

################################################


def info(name, age, grade, country="Myanmar"):
    print(name, age, grade, country)


info("Mg Mg", 10, 5)

################################################

3. Positional only parameters (x, y, /)

Simple is better than complex.


def add(x, y, /):
    return x + y


add(1, 2)
add(2, 1)

################################################

4. Keyword only parameters (*, x, y)

Complex is better than complicated.


def info(*, name, age, grade, country="Myanmar"):
    print(name, age, grade, country)


info(age=10, name="Mg Mg", grade=5)

################################################

5. Variable-length positional only parameters (*x)

We want all simple informations.

* = all
*x = all values for x


x = ()
x = (1,)
x = (1, 2) 
x = (1, 2, "apple")
x = (1, 2, "apple", 1.5)

################################################


def f(*x):
    print(x)


f()
f(1)
f(1, 2)
f(1, 2, "apple")
f(1, 2, "apple", 1.5, 1, 2, 3 , 4, 5, 6, 7, 8, 9,10)

################################################

income_1.xlsh
income_2.xlsh
...
...
income_10.xlsh


No   Date       income($)
1.   1.1.2015    100
2.   2.1.2015    200
..
...
365.


No   Date       income($)
1.   1.1.2016    100
2.   2.1.2016    200
..
...
366.

No   Date       income($)
1.   1.1.2017    100
2.   2.1.2017    200
..
...
355 - holidays(10) = 345


No   Date       income($)
1.   1.1.2020    -
2.   2.1.2020    -
..
...
0

################################################

We want all simple informations.

add()                                =>   0
add(1)                               =>   1
add(1, 2)                            =>   3 
add(1, 2, 3)                         =>   6
add(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)   =>   55

################################################


def add(*numbers): # numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
    total = 0
    for number in numbers:
        total += number
    print(total)


add()
add(1)
add(1, 2)
add(1, 2, 3)
add(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

################################################

6. Variable-length keyword only parameters (**x)

** = all item 
**x = all item for x

item = key + value

################################################

We want all complex informations.

name = "Mg Mg"
age = 10
grade = 5
ph_no = "09123456"
country = "Myanmar"
weight = 50

################################################

simple informations      => (1, 2, 3, 4, 5)

complicated informations => ("Mg Mg", 10, 5, 50)

complex informations     => {'name': 'Mg Mg', 'age': 10, 'grade': 5, 'weight': 50}

################################################


def info(**x):
    print(x)


info()
info(name="Mg Mg")
info(name="Mg Mg", age=10)
info(name="Mg Mg", age=10, grade=5, weight=50)
info(name="Mg Mg", age=10, grade=5, weight=50, country="Myanmar", ph_no="09123456")


{}
{'name': 'Mg Mg'}
{'name': 'Mg Mg', 'age': 10}
{'name': 'Mg Mg', 'age': 10, 'grade': 5, 'weight': 50}
{'name': 'Mg Mg', 'age': 10, 'grade': 5, 'weight': 50, 'country': 'Myanmar', 'ph_no': '09123456'}


################################################################################################

Fixed length Vs variable length

################################################

1. Fixed length of simple data.


def add(x, y, /):
    return x + y


add(1, 2)

################################################

2. Fixed length of complex data.


def info(*, name, age):
    print(name, age)


info(name="Mg Mg", age=10)

################################################

3. Variable length of simple data.


def add(*x):
    print(x)


add()
add(1)
add(1, 2)
add(1, 2, 3)
add(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

################################################

4. Variable length of complex data.


def info(*x):
    print(x)


info()
info(name="Mg Mg")
info(name="Mg Mg", age=10)
info(name="Mg Mg", age=10, grade=5, weight=50)
info(name="Mg Mg", age=10, grade=5, weight=50, country="Myanmar", ph_no="09123456")

################################################################################################

Day.19

1. (a, b, c)                            Form.1, 2, 3
2. (name, age, country="Myanmar")       Form.1, 2, 3
3. (n1, n2, n3, /)                      Form.1
4. (*, name, age, country)              Form.2
5. (*unlimited_pos)                     Form.1
6. (**unlimited_kwargs)                 Form.2

################################################

Positional arguments   =>   args         =>  tuple
Keyword arguments      =>   kw, kwargs   =>  dict

################################################

1. No.3 (Simple is better than complex.)


def add(x, y, /):
    return x + y


add(1, 2)
add(2, 1)

################################################

2. No.4 (Complex is better than complicated.)


def info(*, name, age, grade):
    print(name, age, grade, country)


info(age=10, name="Mg Mg", grade=5)

################################################

3.  No.1 + No.4

x, y          =>  form.1, 2, 3
name, age     =>  form.2



def f(x, y, *, name, age):
    print(x, y, name, age)


f(1, 2, name="abc", age=10)
f(x=1, y=2, name="abc", age=10)
f(1, y=2, name="abc", age=10)


################################################

4. No.3 + No.1 + No.4


a, b, c       =>  form.1
x, y          =>  form.1, 2, 3
name, age     =>  form.2

(a, b, c, /, x, y, *, name, age)

Step.1 => Check parameter list (/, *)
Step.2 => Divide

- a, b, c     - pos 
- x, y        - 1, 2, 3
- name, age   - kw


def f(a, b, c, /, x, y, *, name, age):
    print(a, b, c, x, y, name, age)
    
    
f(1, 2, 3, 4, 5, name="abc", age=10)
f(1, 2, 3, x=4, y=5, name="abc", age=10)
f(1, 2, 3, 4, y=5, name="abc", age=10)

################################################

5. No.3 + No.4 + No.2

form.1   -->  left
form.2   -->  right
1, 2, 3  -->  middle

a, b, c       =>  form.1              No.3
name, age     =>  form.2              No.4
country       =>  form.2("Myanmar")   No.4 + No.2

(a, b, c, /, *, name, age, country="Myanmar")     

################################################

(x, y)        =>  form.1, 2, 3

(a, b, c, /, x, y, *, name, age, country="Myanmar")     

################################################

(d, e, f)        =>  form.1

(a, b, c, d, e, f, /, x, y, *, name, age, country="Myanmar") 

################################################

ph_no        =>  form.2

(a, b, c, d, e, f, /, x, y, *, name, age, ph_no, country="Myanmar") 

################################################

city = "Yangon"

(a, b, c, d, e, f, /, x, y, *, name, age, ph_no, city="Yangon", country="Myanmar") 

################################################

z        =>  form.1, 2, 3

(a, b, c, d, e, f, /, x, y, z, *, name, age, ph_no, city="Yangon", country="Myanmar") 

################################################################################################

6. No.5  (variable length + simple data)


def add(*args):
    total = 0
    for number in args:
        total += number
    return total


ans = add(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
print(ans)

################################################

7. No.6  (variable length + complex data)


def info(**kw):
    print(kw)


info(name="Mg Mg", age=10, grade=5, weight=50)

################################################

8. No.3 + No.6

at least 3 values by pos and more items

def f(a, b, c, /, **kwargs):
    print(a, b, c)
    print(kwargs)


f(1, 2, 3)
f(1, 2, 3, name="abc", age=10)

################################################

9. No.3 + No.5

at least 3 values by pos and more values


def f(a, b, c, /, *args):
    print(a, b, c)
    print(args)


f(1, 2, 3, 4, 100, 1000)

################################################

10. No.4 + No.6

at least 2 values by name and more items

user_name, password
gender, age, country, .....


def f(*, user_name, password, **kwargs):
    print(user_name, password)
    print(kwargs)


f(user_name="abc", password="123456", country="Myanmar", age=10)

################################################

11. No.5 + No.4

at least 2 values by name and more values


def f(*args, user_name, password):
    print(args)
    print(user_name, password)



f(user_name="abc", password="123456")
f(1, 2, 3, user_name="abc", password="123456")

################################################

12. No.3 + No.5 + No.4 + No.6


at least 3 values by pos and more values
No.3 + No.5       =>  pos (left)

a, b, c, /
*args

at least 2 values by name and more items
No.4 + No.6       =>  name (right)

*, user_name, password
**kwargs

################################################


def f(a, b, c, /, *args, user_name, password, **kwargs):
    print(a, b, c)
    print(args)
    print(user_name, password)
    print(kwargs)


f(1, 2, 3, user_name="abc", password="123456")

f(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, country="Myanmar", age=10, user_name="abc", password="123456")

################################################

Passing correct values to function

a = 20
b = 10
c = 30
args = (100, 200, 300)

user_name = "Mg Mg"
password = "123456"
kw = {'country': 'Myanmar', 'age': 10}

f(20, 10, 30, 100, 200, 300, user_name="Mg Mg", password="123456", country='Myanmar', age=10)

################################################

13. No.5 + No.6 (all forms, variable length)

all values, all items


def f(*args, **kwargs):
    print(args)
    print(kwargs)
    print("- " * 42)


f()
f(1, 2, 3)
f(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
f(user_name="Mg Mg", password="123456")
f(user_name="Mg Mg", password="123456", country='Myanmar', age=10)
f(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, user_name="Mg Mg", password="123456", country='Myanmar', age=10)

################################################################################################

Arguments

1. Positional arguments
2. Keyword arguments
3. Default arguments    
4. Positional only arguments
5. Keyword only arguments
6. Arbitrary positional only arguments, Arbitrary positional arguments
7. Arbitrary keyword only arguments, Arbitrary keyword arguments

You should be able to see the connection behind it just by knowing the name.

################################################


def add(x, y):
    pass


add(1, 2)     #  Positional Arguments
add(x=1, y=2) #  Keyword Arguments

################################################


def add(x, y, /):
    pass


add(1, 2)  # Positional only arguments

################################################


def add(*, x, y):
    pass


add(x=1, y=2) #  Keyword only arguments

################################################


def add(*args):
    total = 0
    for number in args:
        total += number
    return total
    

add(1)
add(1, 2)
add(1, 2, 3, 4, 5)  # Arbitrary positional arguments

################################################


def info(**kw):
    print(kw)


info(name="Mg Mg")
info(name="Mg Mg", age=10)
info(name="Mg Mg", age=10, grade=5, weight=50)  # Arbitrary keyword arguments

################################################################################################

You should be able to see the connection behind it just by knowing the name.

Arguments ရဲ့ အမည်တွေနဲ့ ပတ်သတ်ပြီး လေ့ကျင့်ရမှာက

အမည်သိရုံနဲ့ နောက်ကွယ်က ချိတ်ဆက်မှုကို မြင်နိုင်ရပါမယ်။

1. Positional arguments လို့ ပြောခဲ့မယ်ဆိုရင် နောက်ကွယ်မှာ ဖန်တီးထားတဲ့ စည်းမျဉ်းအမျိုးအစားက နံပါတ်ဘယ်လောက်ဖြစ်မလဲ။

2. Positional only arguments လို့ ပြောခဲ့မယ်ဆိုရင် နောက်ကွယ်မှာ ဖန်တီးထားတဲ့ စည်းမျဉ်းအမျိုးအစားက နံပါတ်ဘယ်လောက်ဖြစ်မလဲ။

3. Keyword only arguments လို့ ပြောခဲ့မယ်ဆိုရင် နောက်ကွယ်မှာ ဖန်တီးထားတဲ့ စည်းမျဉ်းအမျိုးအစားက နံပါတ်ဘယ်လောက်ဖြစ်မလဲ။

4. Arbitrary positional arguments လို့ ပြောခဲ့မယ်ဆိုရင် နောက်ကွယ်မှာ ဖန်တီးထားတဲ့ စည်းမျဉ်းအမျိုးအစားက နံပါတ်ဘယ်လောက်ဖြစ်မလဲ။

5. Arbitrary keyword arguments လို့ ပြောခဲ့မယ်ဆိုရင် နောက်ကွယ်မှာ ဖန်တီးထားတဲ့ စည်းမျဉ်းအမျိုးအစားက နံပါတ်ဘယ်လောက်ဖြစ်မလဲ။

6. Default arguments လို့ ပြောခဲ့မယ်ဆိုရင် နောက်ကွယ်မှာ ဖန်တီးထားတဲ့ စည်းမျဉ်းအမျိုးအစားက နံပါတ်ဘယ်လောက်ဖြစ်မလဲ။

7. Keyword arguments လို့ ပြောခဲ့မယ်ဆိုရင် နောက်ကွယ်မှာ ဖန်တီးထားတဲ့ စည်းမျဉ်းအမျိုးအစားက နံပါတ်ဘယ်လောက်ဖြစ်မလဲ။


ဘာလို့ သင်ရလဲဆိုတော့ documentation ဖတ်တတ်ဖို့ပါ။

အမည်အမျိုးမျိုးနဲ့ လှည့်ပတ်ရေးထားကြတော့ တစ်ခုချင်းစီကို သိထားတဲ့သူက ချက်ချင်းနားလည်နိုင်ပေမယ့် မသိတဲ့သူကြတော့လည်း ပိုရှုတ်သွားကြပါတယ်။

################################################################################################

"""
