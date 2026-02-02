
"""

Built-in data types (15)

1 + 2.2         ->   3.2
1 + 5000        ->   5001

1kg + 2.2lb             ->   2kg
1 dollar + 5000 kyats   ->   2$

#################################################

Custom data types

class    -  Dollar
data     -  n
methods  -  add()

#################################################

ဘယ်လိုရေးတယ်ဆိုတာက Attributes exercises မှာ လေ့ကျင့်ရပါမယ်။

Custom data types မှာတော့ အခုရေးပေးထားတာကို နားလည်ရင် ရပါပြီ။

#################################################

Step.1 
Dollar ဆိုတဲ့ class ဒီဇိုင်းဆွဲတာပါ။

Step.2 
ကိုယ်စားပြုမယ့်စာတန်ဖိုးကို 1 dollar လို့ ပေးချင်တာပါ။

Step.3 
သင်္ကေတနဲ့ ပေါင်းချင်တာပါ။

Step.4 
Dollar နှစ်ခုပေါင်းတဲ့အခါ ရလဒ်ကို dollar အဖြစ်နဲ့ပဲ လိုချင်တာပါ။

Step.5 
Kyat ဆိုတဲ့ class ဒီဇိုင်းဆွဲတာပါ။

Step.6 
dollar နဲ့ kyats လိုမျိုး အမျိုးအစား မတူတာတွေကို မှန်မှန်ကန်ကန် ပေါင်းချင်တာပါ။

Step.7 
သင်္ကေတနဲ့ နှုတ်ချင်တာပါ။

Step.8 
သင်္ကေတနဲ့ object ဖန်တီးချင်တာပါ။

Step.9
သင်္ကေတနဲ့ တန်ဖိုးတူလား နှိုင်းယှဉ်ချင်တာပါ။

Step.10
dollar နဲ့ kyats လိုမျိုး အမျိုးအစား မတူတာတွေကို မှန်မှန်ကန်ကန် နှိုင်းယှဉ်ချင်တာပါ။

Step.11
Memory သက်သာအောင် တန်ဖိုးတူခဲ့ရင် တစ်ကြိမ်ပဲ ဖန်တီးပြီး ဝေမျှသုံးစေချင်တာပါ။

#################################################

Step.1 (Draw Dollar Type)

Dollar ဆိုတဲ့ class ဒီဇိုင်းဆွဲတာပါ။


class Dollar:
    def __init__(self, n):
        self.n = n

    def add(self, other):
        return self.n + other.n


x = Dollar(1)
print(x)
print(x.n)

y = Dollar(2)
print(y)
print(y.n)

ans = x.add(y)
print(ans)

#################################################

Step.2 (Representation string -> "1 dollar") 

ကိုယ်စားပြုမယ့်စာတန်ဖိုးကို 1 dollar လို့ ပေးချင်တာပါ။


class Dollar:
    def __init__(self, n):
        self.n = n

    def add(self, other):
        return self.n + other.n

    def __repr__(self):
        return f"{self.n} dollar"


x = Dollar(1)
print(x)

#################################################

Step.3 ( + ) (__add__) 

သင်္ကေတနဲ့ ပေါင်းချင်တာပါ။


class Dollar:
    def __init__(self, n):
        self.n = n

    def __add__(self, other):
        return self.n + other.n

    def __repr__(self):
        return f"{self.n} dollar"


x = Dollar(1)
y = Dollar(2)

ans = x.__add__(y)
print(ans)

ans = x + y
print(ans)

#################################################

Step.4 (result of addition => 3 dollar ) 

Dollar နှစ်ခုပေါင်းတဲ့အခါ ရလဒ်ကို dollar အဖြစ်နဲ့ပဲ လိုချင်တာပါ။

>> Dollar(self.n + other.n)

#################################################


class Dollar:
    def __init__(self, n):
        self.n = n

    def __add__(self, other):
        return Dollar(self.n + other.n)

    def __repr__(self):
        return f"{self.n} dollar"


x = Dollar(1)
y = Dollar(2)
ans = x + y
print(ans)

#################################################

Step.5 ( Design for Kyat )

Kyat ဆိုတဲ့ class ဒီဇိုင်းဆွဲတာပါ။

5000 kyats + 10000 kyats  = 15000 kyats


class Kyat:
    def __init__(self, n):
        self.n = n

    def __add__(self, other):
        return Kyat(self.n + other.n)

    def __repr__(self):
        return f"{self.n} kyat"


x = Kyat(5000)
y = Kyat(10000)
ans = x + y
print(ans)

#################################################

Step.6 (dollar + kyats)

dollar နဲ့ kyats လိုမျိုး အမျိုးအစား မတူတာတွေကို မှန်မှန်ကန်ကန် ပေါင်းချင်တာပါ။

1 dollar + 10000 kyats => 3 dollar
10000 kyats + 1 dollar => 15000 kyats

#################################################

if type(other) == Dollar:
    return Dollar(self.n + other.n)
if type(y) == Kyat:
    return Dollar(self.n + other.n/5000)

#################################################


class Dollar:
    def __init__(self, n):
        self.n = n

    def __add__(self, other):
        if type(other) == Dollar:
            return Dollar(self.n + other.n)
        if type(y) == Kyat:
            return Dollar(self.n + other.n/5000)

    def __repr__(self):
        return f"{self.n} dollar"


class Kyat:
    def __init__(self, n):
        self.n = n

    def __add__(self, other):
        if type(other) == Kyat:
            return Kyat(self.n + other.n)
        if type(other) == Dollar:
            return Kyat(self.n + other.n * 5000)

    def __repr__(self):
        return f"{self.n} kyat"


x = Dollar(1)
y = Kyat(10000)

ans = x + y
print(ans)

ans = y + x
print(ans)

#################################################

1 dollar + 2 dollar      => 3 dollar
a = Dollar(1)
b = Dollar(2)
print(a + b)

10000 kyats + 5000 kyats => 15000 kyats
x = Kyat(5000)
y = Kyat(10000)
print(x + y)

1 dollar + 10000 kyats => 3 dollar
print(a + y)

10000 kyats + 1 dollar => 15000 kyats
print(y + a)

#################################################

Step.7 ( - ) ( __sub__ )

သင်္ကေတနဲ့ နှုတ်ချင်တာပါ။


class Dollar:
    def __init__(self, n):
        self.n = n

    def __add__(self, other):
        if type(other) == Dollar:
            return Dollar(self.n + other.n)
        if type(y) == Kyat:
            return Dollar(self.n + other.n/5000)

    def __sub__(self, other):
        if type(other) == Dollar:
            return Dollar(self.n - other.n)
        if type(other) == Kyat:
            return Dollar(self.n - other.n/5000)

    def __repr__(self):
        return f"{self.n} dollar"


class Kyat:
    def __init__(self, n):
        self.n = n

    def __add__(self, other):
        if type(other) == Kyat:
            return Kyat(self.n + other.n)
        if type(other) == Dollar:
            return Kyat(self.n + other.n * 5000)

    def __sub__(self, other):
        if type(other) == Kyat:
            return Kyat(self.n - other.n)
        if type(other) == Dollar:
            return Kyat(self.n - other.n * 5000)

    def __repr__(self):
        return f"{self.n} kyat"


a = Dollar(1)
b = Dollar(2)
print(b - a)  # 1 d

x = Kyat(5000)
y = Kyat(10000)
print(y - x) # 5000 k

print(a - y) # 1$ - 10000 k = 1 - 2 = -1$
print(y - a) # 10000 k - 1$ = 10000 - 5000 = 5000 k

#################################################

Step.8 (literal)

သင်္ကေတနဲ့ object ဖန်တီးချင်တာပါ။

Create by name 
print(int(1) + int(2))

Create by symbol(literal) 
print(1 + 2)

#################################################

literal

print(int(1) + int(2))
print(1 + 2)

print(Dollar(1) + Dollar(2))
print(1 dollar + 2 dollar)

#################################################

Install external pakage
1. custom-literals
2. forbiddenfruit

from custom_literals import literal

@literal(int, float, name="dollar")
def f1(n):
    return Dollar(n)

#################################################

from custom_literals import literal


class Dollar:
    def __init__(self, n):
        self.n = n

    def __add__(self, other):
        if type(other) == Dollar:
            return Dollar(self.n + other.n)
        if type(other) == Kyat:
            return Dollar(self.n + other.n/5000)

    def __sub__(self, other):
        if type(other) == Dollar:
            return Dollar(self.n - other.n)
        if type(other) == Kyat:
            return Dollar(self.n - other.n/5000)

    def __repr__(self):
        return f"{self.n} dollar"


class Kyat:
    def __init__(self, n):
        self.n = n

    def __add__(self, other):
        if type(other) == Kyat:
            return Kyat(self.n + other.n)
        if type(other) == Dollar:
            return Kyat(self.n + other.n * 5000)

    def __sub__(self, other):
        if type(other) == Kyat:
            return Kyat(self.n - other.n)
        if type(other) == Dollar:
            return Kyat(self.n - other.n * 5000)

    def __repr__(self):
        return f"{self.n} kyat"


@literal(int, float, name="dollar")
def f1(n):
    return Dollar(n)


@literal(int, float, name="kyat")
def f2(n):
    return Kyat(n)


print(1 .dollar + 2 .dollar)
print(10000 .kyat + 5000 .kyat)
print(1 .dollar + 10000 .kyat)
print(10000 .kyat + 1 .dollar)

#################################################

Step.9 ( == ) ( __eq__ ) 

သင်္ကေတနဲ့ တန်ဖိုးတူလား နှိုင်းယှဉ်ချင်တာပါ။

== (equal to, equality operator)

equal number 

#################################################


from custom_literals import literal


class Dollar:
    def __init__(self, n):
        self.n = n

    def __add__(self, other):
        if type(other) == Dollar:
            return Dollar(self.n + other.n)
        if type(other) == Kyat:
            return Dollar(self.n + other.n/5000)

    def __sub__(self, other):
        if type(other) == Dollar:
            return Dollar(self.n - other.n)
        if type(other) == Kyat:
            return Dollar(self.n - other.n/5000)

    def __eq__(self, other):
        return self.n == other.n
       
    def __repr__(self):
        return f"{self.n} dollar"


class Kyat:
    def __init__(self, n):
        self.n = n

    def __add__(self, other):
        if type(other) == Kyat:
            return Kyat(self.n + other.n)
        if type(other) == Dollar:
            return Kyat(self.n + other.n * 5000)

    def __sub__(self, other):
        if type(other) == Kyat:
            return Kyat(self.n - other.n)
        if type(other) == Dollar:
            return Kyat(self.n - other.n * 5000)

    def __eq__(self, other):
        return self.n == other.n
        
    def __repr__(self):
        return f"{self.n} kyat"


@literal(int, float, name="dollar")
def f1(n):
    return Dollar(n)


@literal(int, float, name="kyat")
def f2(n):
    return Kyat(n)


print(1 .dollar == 1 .dollar)
print(5000 .kyat == 5000 .kyat)

#################################################

Step.10 ( dollar == kyat )

dollar နဲ့ kyats လိုမျိုး အမျိုးအစား မတူတာတွေကို မှန်မှန်ကန်ကန် နှိုင်းယှဉ်ချင်တာပါ။


from custom_literals import literal


class Dollar:
    def __init__(self, n):
        self.n = n

    def __add__(self, other):
        if type(other) == Dollar:
            return Dollar(self.n + other.n)
        if type(other) == Kyat:
            return Dollar(self.n + other.n/5000)

    def __sub__(self, other):
        if type(other) == Dollar:
            return Dollar(self.n - other.n)
        if type(other) == Kyat:
            return Dollar(self.n - other.n/5000)

    def __eq__(self, other):
        if type(other) == Dollar:
            return self.n == other.n
        if type(other) == Kyat:
            return self.n == other.n/5000

    def __repr__(self):
        return f"{self.n} dollar"


class Kyat:
    def __init__(self, n):
        self.n = n

    def __add__(self, other):
        if type(other) == Kyat:
            return Kyat(self.n + other.n)
        if type(other) == Dollar:
            return Kyat(self.n + other.n * 5000)

    def __sub__(self, other):
        if type(other) == Kyat:
            return Kyat(self.n - other.n)
        if type(other) == Dollar:
            return Kyat(self.n - other.n * 5000)

    def __eq__(self, other):
        if type(other) == Kyat:
            return self.n == other.n
        if type(other) == Dollar:
            return self.n == other.n * 5000

    def __repr__(self):
        return f"{self.n} kyat"


@literal(int, float, name="dollar")
def f1(n):
    return Dollar(n)


@literal(int, float, name="kyat")
def f2(n):
    return Kyat(n)


print(1 .dollar == 5000 .kyat)
print(5000 .kyat == 1 .dollar)

#################################################

"""

