
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

8. Types of arameters (6)

1. Normal parameters                                  (x, y)
2. Default parameters                                 (x, y=0)
3. Positional only parameters                         (x, y, /)
4. Keyword only parameters                            (*, x, y)
5. Variable-length positional only parameters
6. Variable-length keyword only parameters 

################################################

"""
