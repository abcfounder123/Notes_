
"""

1. List Comprehension
ရှိပြီးသား list တစ်ခုကို အခြေခံပြီး list အသစ်တစ်ခုကို တိုတိုတုတ်တုတ်နဲ့ အလွယ်တကူ တည်ဆောက်တဲ့ နည်းလမ်းဖြစ်ပါတယ်။
ကြာချိန်က ပုံမှန် for loop ထက် ပိုမြန်ပါတယ်။
ရင်းနှီးသွားပြီဆိုရင် For loop ထက်လည်း ဖတ်ရလွယ်ပါတယ်။

-----------------------------------------

2. Decorator
မူရင်း function ကို မပြင်ချင်တဲ့အခါ function အသစ်တစ်ခုနဲ့  လုပ်ဆောင်ချက်အသစ်တွေ ထပ်ပေါင်းထည့်တာမျိုးပါ။
တတိယမြောက် function ကို ဘယ်လိုအမည်ပေးမလဲဆိုတာမျိုး သိရပါမယ်။

-----------------------------------------

3. Generator
Data တွေကို တစ်ခါတည်း အကုန်မထုတ်ပေးဘဲ လိုအပ်တဲ့အချိန်မှ တစ်ခုချင်းစီ ထုတ်ပေးတဲ့ function မျိုးပါ။
Memory သက်သာဖို့ ရည်ရွယ်ပါတယ်။
စားပွဲပေါ်မှာ laptop တစ်လုံးချင်းစီပြသလိုမျိုး ဖြစ်ပါမယ်။

-----------------------------------------

4. Lambda function 
အမည်ပေးစရာမလိုတဲ့ တစ်ခါသုံး function ဖြစ်ပါတယ်။

-----------------------------------------

5. Higher-Order Functions

higher ဆိုတာက ပိုကြီးတာကို ပြောတာပါ။first order function ထက် ပိုကြီးတာတွေပေါ့။တနည်းအားဖြင့် second order function, third order function, . . .  တွေကို ပေါင်းပြီး ခေါ်လိုက်တဲ့ အခေါ်အဝေါ်ပေါ့။

သင်္ချာမှာ first order function ဆိုတာက f(x) ကို ပြောတာပါ။
x တန်ဖိုးထည့်ရင် y တန်ဖိုးထွက်မယ်ဆိုတာမျိုးပါ။
first order function ထုတ်ပေးရင်တော့ second order function ဖြစ်သွားပါမယ်။
second order function ထုတ်ပေးရင်တော့ third order function ဖြစ်သွားပါမယ်။

အလွယ်ပြောရရင် function ထုတ်ပေးတဲ့ function မှန်သမျှကို higher-order function လို့ ခေါ်နိုင်ပါတယ်။

-----------------------------------------

6. Closure

Closing something လို့ အဓိပ္ပါယ်ရပါတယ်။

ပုံမှန်အားဖြင့် local data တွေက ဖျက်ခံရပါတယ်။
Closed လုပ်ထားရင်တော့ ဆက်ပြီးရှိနေပါတယ်။

Data တွေကို Global အနေနဲ့ မသုံးချင်တဲ့အခါ local မှာထားရင်လည်း ဖျက်ခံရမှာစိုးတဲ့အခါ closure ဆိုတဲ့ နည်းလမ်းကို အသုံးပြုပါတယ်။

-----------------------------------------

7.  Map
ကီလိုဂရမ်ကနေ ပေါင်အဖြစ် ပြောင်းတာမျိုး ၊ ဒေါ်လာကို ကျပ်ပြောင်းတာမျိုး data တွေကို transform လုပ်ဖို့အတွက် သုံးပါတယ်။

-----------------------------------------

8. Filter
လိုအပ်တဲ့ data ကို စစ်ထုတ်ဖို့အတွက် သုံးပါတယ်။
စုံကိန်းတွေကိုပဲ စစ်ထုတ်တာမျိုး ၊ အောင်စာရင်းထဲက ဂုဏ်ထူးထွက်တဲ့ ကျောင်းသားတွေကိုပဲ စစ်ထုတ်တာမျိုးပေါ့။

-----------------------------------------

9. Reduce 
data တွေကို တစ်ခုတည်းအဖြစ် လျော့ချဖို့သုံးပါတယ်။
ဘာသာရပ်ခြောက်ခုရဲ့ အမှတ်စာရင်းခြောက်ခုကို စုစုပါင်းရမှတ်ဆိုပြီး တစ်ခုတည်းအဖြစ် လျော့ချလိုက်တာမျိုးပါ။

-----------------------------------------

10. Data ပြောင်းလဲနည်း သုံးမျိုး 

Data တွေကို Transform, filter, reduce ဆိုပြီး ပုံစံသုံးမျိုးနဲ့ ပြောင်းလဲနိုင်ပါတယ်။

Transform လုပ်ချင်တဲ့အခါ map ကို သုံးနိုင်ပါတယ်။
1. map => kg to lb  => 10 to 10

လိုချင်တာကို စစ်ထုတ်ချင်တဲ့အခါ filter ကို သုံးနိုင်ပါတယ်။
2. filter => even numbers from list => 10 to 5

တစ်ခုတည်းအဖြစ် လျော့ချချင်တဲ့အခါ reduce ကို သုံးနိုင်ပါတယ်။
3. reduce => all data -> 1 data (total marks)

----------------------------------------------------------------------------------


1. List Comprehension
   - list to new list
   - Transforming data
   - Filtering data

#########################################

1. list to new list

l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
new2 = [n + 5 for n in l]
print(new2)

2. Transforming data (Kg to Lb)

kgs = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
lbs = [round(kg * 2.2, 2) for kg in kgs]
print(lbs)

3. Filtering data (even number)

l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers2 = [n for n in l if n % 2 == 0]

print(even_numbers2)

#########################################

1. list to new list

[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]     + 5
[6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
new = []
for n in l:
    new.append(n + 5)

l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
new2 = [n + 5 for n in l]
print(new2)

#########################################

2. Transforming data (Kg to Lb)

kgs = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
lbs = [kg * 2.2 for kg in kgs]
print(lbs)

kgs = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
lbs = [round(kg * 2.2, 2) for kg in kgs]
print(lbs)

#########################################

3. Filtering data (even number)

l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = []

for n in l:
    if n % 2 == 0:
        even_numbers.append(n)

print(even_numbers)


l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers2 = [n for n in l if n % 2 == 0]

print(even_numbers2)

##################################################################################

2. Decorator
   - new and old (different name)
   - old to new  (same name)

#########################################

1. new and old (different name)


def f2(x):
    def f3():
        print("-" * 41)
        x()
        print("-" * 41)
    return f3


def f1():
    print("Hello")


z = f2(f1)

f1()
f1()
f1()
f1()
f1()

z()

#########################################

2. old to new  (same name)

def f2(x):
    def f3():
        print("-" * 41)
        x()
        print("-" * 41)
    return f3


def f1():
    print("Hello")


f1 = f2(f1)

f1()
f1()
f1()
f1()
f1()

#########################################

def f2(x):
    def f3():
        print("-" * 41)
        x()
        print("-" * 41)
    return f3

@f2
def f1():
    print("Hello")


f1()
f1()
f1()
f1()
f1()

#########################################

f1 = f2(f1)

@f2
def f1():
    print("Hello")

##################################################################################

3. Generator
   - yield
   - eg.range, summation, A to Z


def generator():
    while True:
        yield 1


#########################################

1. range


def f(start, stop, step):
    ans = start
    while ans < stop:
        yield ans
        ans += step


number_sequence = f(2, 11, 2)
print(next(number_sequence))
print(next(number_sequence))
print(next(number_sequence))
print(next(number_sequence))
print(next(number_sequence))

#########################################

2. summation

summation of 1 = 1
summation of 2 = 1 + 2 = 3                2
summation of 3 = 1 + 2 + 3 = 6            3
summation of 4 = 1 + 2 + 3 + 4 = 10       4


def summation():
    ans = 1
    n = 2
    while True:
        yield ans
        ans += n
        n += 1


s = summation()
print(next(s))
print(next(s))
print(next(s))
print(next(s))

#########################################


def summation():
    ans = 1
    n = 2
    while True:
        yield ans
        ans += n
        n += 1

n = 1
for s in summation():
    print(f"Summation of {n} = {s}")
    if n == 100:
        break
    n += 1

#########################################

3. factorial


def factorial():
    ans = 1
    n = 2
    while True:
        yield ans
        ans *= n
        n += 1


n = 1
for s in factorial():
    print(f"Factorial of {n} = {s}")
    if n == 10:
        break
    n += 1

#########################################

4. even_number


def even_number():
    ans = 2
    while True:
        yield ans
        ans += 2


n = 1
for e in even_number():
    print(e)
    if n == 100:
        break
    n += 1

#########################################

5. A to Z


def generator():
    n = 65
    while n < 91:
        yield chr(n)
        n += 1


for c in generator():
    print(c)

##################################################################################

4. Lambda

lambda x, y:x + y
lambda x, y:x - y
lambda x, y=0: x + y
lambda x, y, /: x + y
lambda :print("-" * 42)


def add(x, y):
    return x + y


def sub(x, y):
    return x - y


def add(x, y=0):
    return x + y


def add(x, y, /):
    return x + y


def line():
    print("-" * 42)


#########################################

For garbage collection

x = 1
y = 2
z = x + y
print(z)
>> int(1), int(2) ->  int(3)
>> 28 bytes 28 bytes 28 bytes -> 84 bytes, int 3

print(1 + 2)
>>28 bytes 28 bytes 28 bytes -> 0 bytes , int 0

#########################################

Test purpose

line = lambda :print("-" * 42)
line()


def line():
    print("-" * 42)


line()

##################################################################################

5. Higher-Order Functions

First-Order Functions -> f(x)

x = 3
y = 2x = 6


def f(x):
    y = 2 * x
    return y

#########################################

Second-Order Functions (produce First-Order Functions)


def s(a):

    def f(x):
        y = 2 * x
        return y

    return f


s(a) <- Second-Order Functions
f(x) <- First-Order Functions

#########################################

Third-Order Functions (produce Second-Order Functions)

##################################################################################

6. Closure

- a process of closing somthing
- closing different data => s(2), s(3), s(7)

- data hiding
- function factories
- decorators


def s(a):

    def f(x):
        y = a * x
        return y

    return f


x = s(2)
print(x.__closure__)

#########################################

z = s(2) is same as z = f that closed a=2


def f(x):
    y = 2 * x
    return y


#########################################

z = s(3) is same as z = f that closed a=3


def f(x):
    y = 3 * x
    return y


#########################################


def s(a):

    def f(x):
        y = a * x
        return y

    return f


multiply_2 = s(2)  # a=2
print(multiply_2(1))      # 2 * x = 2
print(multiply_2(2))      # 2 * x = 4
print(multiply_2(3))      # 2 * x = 6

multiply_3 = s(3)  # a=3
print(multiply_3(1))      # 3 * x = 3
print(multiply_3(2))      # 3 * x = 6
print(multiply_3(3))      # 3 * x = 9

multiply_79 = s(79)

#########################################


def add_factory(n):
    def add(x):
        return x + n
    return add


add_1 = add_factory(1) # closed 1
print(add_1(2))

add_7 = add_factory(7) # closed 7
print(add_7(2))

#########################################


def factory(age_by_country):

    def alcohol_permit(age):
        return age >= age_by_country

    return alcohol_permit


age_by_country = 16 # 19, 16, 21, 18 by location of country
age = 18

alcohol_permit = factory(age_by_country)  # 19, 16, 21, 18

if alcohol_permit(age):
    print("You can buy.")

else:
    print("You can not buy.")

##################################################################################


def s(a, b, c):

    def f1(x):
        y = a + x
        return y

    def f2(x):
        y = a + b + x
        return y

    def f3(x):
        y = a + b + c + x
        return y

    return f1, f2, f3


x, y, z = s(1, 2, 3)

print(s.__closure__)     # None
print(x.__closure__)     # closed  1
print(y.__closure__)     # closed  1 and 2
print(z.__closure__)     # closed  1 and 2 and 3

##################################################################################

7. Map

- create a connection between fun and data
- transform(kg to lb)

#########################################

>> transform(kg to lb)


def f1(kg):
    return round(kg * 2.2, 2)


kgs = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

#########################################

for kg in kgs:               # for loop
    lbs.append(f1(kg))


lbs = [f1(kg) for kg in kgs] # list comprehension

lbs = map(f1, kgs)           # map

#########################################

List comprehension example


def f1(kg):
    print("h")
    return round(kg * 2.2, 2)


kgs = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
l = [f1(kg) for kg in kgs] # 10 s

print(l)

#########################################

f1
f1
f1
f1
f1
f1
f1
f1
f1
f1
[2.2, 4.4, 6.6, 8.8, 11.0, 13.2, 15.4, 17.6, 19.8, 22.0]

#########################################

Map example


def f1(kg):
    print("h")
    return round(kg * 2.2, 2)


kgs = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
l = map(f1, kgs)

print(next(l))  # 1s

#########################################

f1
2.2

##################################################################################

Time consumption

all data => 1 hour

1 page  => 1 sec

##################################################################################

Memory consumption

all int => 10
1 int   => 1

lbs = [2.2, 4.4, 6.6, 8.8, 11.0, 13.2, 15.4, 17.6, 19.8, 22.0]
list = 50 bytes
float 10 = 300 bytes
total = 350 bytes

next(l)
float 1 = 30 bytes = 0 bytes

##################################################################################

kgs = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
lbs = [f1(kg) for kg in kgs]

list      => 50
int 10    => 280
lbs       => 50
float 10  => 300 bytes
total     => 680 bytes

########################################

kgs = range(1, 11)
l = map(f1, kgs)
print(next(l))  #  1 from range, f1(1) => 2.2

range(1, 11) => 30
map     => 30 byte
int 1   => 28 byte  => 0 bytes
float 1 => 30 bytes => 0 bytes

total   => 60 to 118

##################################################################################

Pip line

1000 GB  (1 page = 1MB )

database = 1 page (next value)
pip_line = map(negative_word, database)

total = 0  -> 10 -> 18 -> 100000
total += next(pip_line)

##################################################################################

In List Comprehension or 'for loop',
if 1 error, None of result.


def f1(kg):
    print("f1")
    return round(kg * 2.2, 2)


kgs = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "abc"]   # 11 => 10 + 1(error)
lbs = [f1(kg) for kg in kgs]
print(lbs)

#########################################

Map can work well until error.


def f1(kg):
    print("f1")
    return round(kg * 2.2, 2)


kgs = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "abc"]   # 11 => 10 + 1(error)
lbs = map(f1, kgs)
print(next(lbs))
print(next(lbs))
print(next(lbs))
print(next(lbs))
print(next(lbs))
print(next(lbs))
print(next(lbs))
print(next(lbs))
print(next(lbs))
print(next(lbs))
# print(next(lbs))  # error

##################################################################################

8. Filter
- Filtering data

#########################################

Filtering data (even number)

1. for loop example

def is_even(n):
    return n % 2 == 0


l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = []

for n in l:
    if is_even(n):
        even_numbers.append(n)

print(even_numbers)

#########################################

2. LC example

l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
leven_numbers = [n for n in l if is_even(n)]   # [2, 4, 6, 8, 10]

print(leven_numbers)

#########################################

2. filter example

l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
f = filter(is_even, l)

print(next(f))
print(next(f))

#########################################


def is_even(n):
    print(f"is even({n})")
    return n % 2 == 0


l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
f = filter(is_even, l)

print(next(f))  #  1 from list , is_even(1) => 2 from list , is_even(2) => 2
print(next(f))  #  3 from list , is_even(3) => 4 from list , is_even(4) => 4

#########################################

Time and memory

After 10s,  [2, 4, 6, 8, 10]


2            after 2s
4            after 2s
6            after 2s
8            after 2s
10           after 2s

##################################################################################

9. Reduce

- reducing data
- all data to 1 data

#########################################

numbers to total
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10] to 55

#########################################

from functools import reduce


def add(a, b):
    return a + b


l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
r = reduce(add, l)  # add(1, 2) = 3 -> add(3, 3) = 6 -> add(6, 4) = 10 ... => 55

print(r)

##################################################################################

10. Data (Transform, filter, reduce)

1. map => kg to lb  => 10 to 10

2. filter => even numbers from list => 10 to 5

3. reduce => all data -> 1 data (total marks)

##################################################################################

11. Recursion

1. Direct Recursion ( tail, head, tree, nested )
2. Indirect Recursion

Recursion example => fibonacci

Recursion and cache
1. Normal recursion
2. Recursion with cache
3. Recursion with lru cache  (Least Recently Used Cache)

#########################################

a. Tail Recursion

def f(n):
    if n > 0:
        print(n)
        f(n-1)  # tail
    return None


f(3)

#########################################

if 3 > 0:
    print(3)
    if 2 > 0:
        print(2)
        if 1 > 0:
            print(1)
            if 0 > 0:
                print(0)
                f(- 1)
            return None # f(0)
        return None  # f(1)
    return None  # f(2)
return None   # f(3)


if 3 > 0:
    print(3)
    if 2 > 0:
        print(2)
        if 1 > 0:
            print(1)
            if 0 > 0:
                print(0)
                f(0 - 1)

3
2
1


#########################################

b. Head Recursion

def f(n):
    if n > 0:
        f(n - 1)  # head
        print(n)
    return None


f(3)

#########################################

if 3 > 0:
    if 2 > 0:
        if 1 > 0:
            if 0 > 0:
                f(0 - 1)
                print(0)
            return None # f(0)
            print(1)
        return None  # f(1)
        print(2)
    return None # f(2)
    print(3)
return None  # f(3)


if 3 > 0:
    if 2 > 0:
        if 1 > 0:
            if 0 > 0:
                f(0 - 1)
                print(0)
            print(1)
        print(2)
    print(3)

1
2
3

#########################################

Tail and Head


def t(n):
    if n > 0:
        print(n)
        t(n - 1) # tail


def h(n):
    if n > 0:
        h(n - 1)  # head
        print(n)


t(5)  #  5 4 3 2 1
h(5)  #  1 2 3 4 5

#########################################

c. Tree Recursion

2 or more recursive program

f()      => recursive program
f()      => recursive program

#########################################


def f(n):
    if n > 0:
        print(n)
        f(n - 1)   # calling once
        f(n - 1)   # calling twice


f(3)

#########################################

if 3 > 0:
    print(3)
    if 2 > 0:
        print(2)
        if 1 > 0:
            print(1)
            if 0 > 0:
                print(0)
                f(0 - 1)
                f(0 - 1)
            if 0 > 0:
                print(0)
                f(0 - 1)
                f(0 - 1)

        if 1 > 0:
            print(1)
            if 0 > 0:
                print(0)
                f(0 - 1)
                f(0 - 1)
            if 0 > 0:
                print(0)
                f(0 - 1)
                f(0 - 1)
    if 2 > 0:
        print(2)
        if 1 > 0:
            print(1)
            if 0 > 0:
                print(0)
                f(0 - 1)
                f(0 - 1)
            if 0 > 0:
                print(0)
                f(0 - 1)
                f(0 - 1)
        if 1 > 0:
            print(1)
            if 0 > 0:
                print(0)
                f(0 - 1)
                f(0 - 1)
            if 0 > 0:
                print(0)
                f(0 - 1)
                f(0 - 1)

#########################################


                           f(3)

                 f(2)                 f(2)

            f(1)     f(1)          f(1)        f(1)

        f(0) f(0)  f(0) f(0)    f(0) f(0)     f(0) f(0)

#########################################

                                                f(4)

                           f(3)                                              f(3)

                 f(2)                   f(2)                     f(2)                   f(2)

            f(1)     f(1)          f(1)        f(1)         f(1)     f(1)          f(1)        f(1)

        f(0) f(0)  f(0) f(0)    f(0) f(0)     f(0) f(0)  f(0) f(0)  f(0) f(0)    f(0) f(0)     f(0) f(0)


4
3
2
1
1
2
1
1
3
2
1
1
2
1
1

#########################################


f(5)

5
4
3
2
1
1
2
1
1
3
2
1
1
2
1
1
4
3
2
1
1
2
1
1
3
2
1
1
2
1
1

##################################################################################

d. Nested Recursion

f()      => normal recursive program
f(f())   => nested recursive program

#########################################


def f(n):
    print(f"f({n})")
    if n > 100:
        return n - 10
    else:
        return f(f(n+11))


print(f(99))

#########################################

f(99)
=>  return f(f(99 + 11))  =>  f(f(110))
=>  return f(f(99 + 11))  =>  f(100)
=>  return f(f(99 + 11))  =>  f(f(111))
=>  return f(f(99 + 11))  =>  f(101)
=>  return f(f(99 + 11))  =>  91

f(99)
f(110)
f(100)
f(111)
f(101)
91

##################################################################################

2. Indirect Recursion

Indirect recursion between A() and B().

A() calls B() and B() calls A().

A(5) => 5
B(4) => 4
A(3) => 3
B(2) => 2
A(1) => 1
B(0) =>

#########################################


def A(n):
    print(f"A({n})", end=" => ")
    if n > 0:
        print(n)
        B(n-1)


def B(n):
    print(f"B({n})", end=" => ")
    if n > 0:
        print(n)
        A(n-1)


A(5)

##################################################################################

Recursion example => fibonacci

f0 = 0
f1 = 1

f2 = 1
f3 = 2
f4 = 3
f5 = 5
f6 = f5 + f4
f10 = f9 + f8
fn = f(n-1) + f(n-2)

#########################################

def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)
        
#########################################

             fib(2)

        fib(1)    fib(0)



                       fib(3)

                fib(2)        fib(1)

            fib(1)    fib(0)


                                                           fib(5)

                                    fib(4)                                       fib(3)

                         fib(3)                 fib(2)                    fib(2)        fib(1)

                 fib(2)        fib(1)       fib(1)    fib(0)          fib(1)    fib(0)

             fib(1)    fib(0)

#########################################

1. Normal recursion

c = [0, ]


def fib(n):
    c[0] += 1
    print(f"f({n})")
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)


print(fib(25))
print(c[0])

#########################################

2. Recursion with cache

c = [0, ]

cache = {0: 0,
         1: 1,
         }


def fib(n):
    c[0] += 1
    print(f"f({n})")

    if n in cache:
        return cache[n]
    else:
        ans = fib(n-1) + fib(n-2)

    cache[n] = ans
    return ans


print(fib(25))
print(c[0])

#########################################

3. Recursion with lru cache


from functools import lru_cache


c = [0, ]

@lru_cache()
def fib(n):
    c[0] += 1
    print(f"f({n})")
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)


print(fib(25))
print(c[0])

#########################################

1. Normal recursion         => 242785
2. Recursion with cache     => 49
3. Recursion with lru cache => 26

##################################################################################

"""



