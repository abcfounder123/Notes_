"""

1. is_even (တန်ဖိုးတစ်ခုခုကို 2 နဲ့စားလို့ အကြွင်း 0 ရရင် စုံကိန်းဖြစ်ပါတယ်။)( n % 2 == 0)

2. is_odd (တန်ဖိုးတစ်ခုခုကို 2 နဲ့စားလို့ အကြွင်း 1 ရရင် မကိန်းဖြစ်ပါတယ်။) ( n % 2 == 1 )

3. is_number (0 1 2 3 4 5 6 7 8 9 စတာတွေဟာ နံပါတ်တွေဖြစ်ကြပါတယ်။) ( c in "0123456789" )

is_alphabet (a to z တွေနဲ့ ကကြီး ခကွေးလိုမျိုးတွေက အက္ခရာဖြစ်ပါတယ်။)

4. English alphabet

5. English alphabet + Myanmar alphabet by unicode

6. Myanmar alphabet

7. palindrome (နောက်ပြန်ဖတ်လျှင်လည်း ထပ်တူညီသော စကား) eg. madam ( str == str[::-1] )

8. greater number (ပိုကြီးတဲ့ နံပါတ်) ( n1 > n2 ) 

9. less number (ပိုကြီးတဲ့ နံပါတ်) ( n1 < n2 )

10. leap year (ရက်ထပ်နှစ်) (and, or)
    1. divisible by 400 ( eg. 2000, 1600 )    ( y % 400 == 0 )
    2. divisible by 4 + not divisible by 100   ( y % 4 == 0 and y % 100 != 0 )
    - Rule.1 or Rule.2
    
=> divisible by 4, + 1 days  
=> -3d by 400 years 

11. summation
    => summation of 5 = 1 + 2 + 3 + 4 + 5 = 15
    
12. factorial(n) (မြှောက်ဖော်ကိန်း)
    => factorial of 5 = 1 * 2 * 3 * 4 * 5 = 120
    
13. reverse_string(s) (string ကိုနောက်ကစပြီး ပြောင်းပြန်ရေးခြင်း။) ( [::-1] )

14. count_vowels(s) (စာလုံးထဲက a, e, i, o, u ရေတွက်ခြင်း။)

15. count_vowels(s) (စာလုံးထဲက a, e, i, o, u ဘယ်နှစ်လုံးရှိလဲရေတွက်ခြင်း။)

16. sum_of_list(lst) (စာရင်းထဲက နံပါတ်တွေကို ပေါင်းခြင်း။)

17. max(lst) (အများဆုံးတန်ဖိုး ရှာခြင်း။)

18. min(lst) (အနည်းဆုံးတန်ဖိုး ရှာခြင်း။)

19. find_max_min(lst) အများဆုံးနဲ့ အနည်းဆုံးတန်ဖိုး ရှာခြင်း။ 

20. linear search

21. Uppercase and Lowercase

22. Binary Search

...

...

...

50.

################################################################################################

1. is_even (တန်ဖိုးတစ်ခုခုကို 2 နဲ့စားလို့ အကြွင်း 0 ရရင် စုံကိန်းဖြစ်ပါတယ်။)( n % 2 == 0)


def is_even(n):
    if n % 2 == 0:
        return True
    else:
        return False


def is_even(n, /):
    '''
    တန်ဖိုးတစ်ခုခုကို 2 နဲ့စားလို့ အကြွင်း 0 ရရင် စုံကိန်းဖြစ်ပါတယ်။( n % 2 == 0)
    param   ->   int
    return  ->   bool

    eg. is_even(4)  --->  True
        is_even(5)  --->  False
    '''
    return n % 2 == 0


result = is_even(5)
print(result)

################################################

Checking function (help)

1. parameter list => (n, /) => No.3

2. 
input  => int
output => bool

3. 
effect => -
result => bool

4. Type of function
fun No.2 ( result only function ) (pure function)

################################################

2. is_odd (တန်ဖိုးတစ်ခုခုကို 2 နဲ့စားလို့ အကြွင်း 1 ရရင် မကိန်းဖြစ်ပါတယ်။) ( n % 2 == 1 )


def is_odd(n, /):
    return n % 2 == 1


print(is_odd(5))

################################################

3. is_number (0 1 2 3 4 5 6 7 8 9 စတာတွေဟာ နံပါတ်တွေဖြစ်ကြပါတယ်။) ( c in "0123456789" )


def is_number(c):
    return c in "0123456789"


s = "Myanmar = 70, English = 74, Celsius = 28"

for c in s:
    if is_number(c):
        print(f"{c} is numerical value.")
    else:
        print(f"{c} is not numerical value.")

################################################

4. English alphabet

is_alphabet (a to z တွေနဲ့ ကကြီး ခကွေးလိုမျိုးတွေက အက္ခရာဖြစ်ပါတယ်။)


def is_alphabet(c, /):
    return c in "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"

################################################

5. English alphabet + Myanmar alphabet by unicode

65 90         A to Z
97  122       a to z
4096, 4129    က to အ


def is_alphabet(c, /):
    return ord(c) in (list(range(65, 91)) + list(range(97, 123)) + list(range(4096, 4130)))


print(is_alphabet("အ"))

################################################

6. Myanmar alphabet


def is_myn_alphabet(c, /):
    return ord(c) in list(range(4096, 4130))


print(is_myn_alphabet("a"))

################################################

7. palindrome (နောက်ပြန်ဖတ်လျှင်လည်း ထပ်တူညီသော စကား) eg. madam ( str == str[::-1] )
   eg. w = apple, rw = elppa,
   

def palindrome(w, /):
    return w == w[::-1]


print(palindrome("apple"))
print(palindrome("madam"))

################################################

8. greater number (ပိုကြီးတဲ့ နံပါတ်) ( n1 > n2 ) 


def greater_number(n1, n2):
    if n1 > n2:
        return n1

    if n2 > n1:
        return n2

    if n1 == n2:
        return None 


def greater_number(n1, n2):
    if n1 > n2:
        return n1

    elif n2 > n1:
        return n2

    else: # "equal"
        return None 


def greater_number(n1, n2):
    if n1 > n2:
        greater = n1

    elif n2 > n1:
        greater = n2

    else: # "equal"
        greater = None

    return greater
    
    
def greater_number(n1, n2):
    if n1 > n2:
        return n1
    else:
        return n2

################################################

9. less number (ပိုကြီးတဲ့ နံပါတ်) ( n1 < n2 )

def less_number(n1, n2):
    if n1 < n2:
        return n1
    else:
        return n2


################################################

10. leap year (ရက်ထပ်နှစ်) (and, or)

# 1. divisible by 400 ( eg. 2000, 1600 )    ( y % 400 == 0 )
# 2. divisible by 4 + not divisible by 100   ( y % 4 == 0 and y % 100 != 0 )
# Rule.1 or Rule.2

# eg. 1600  (divisible by 400) rule No.1

# eg. 1704  (divisible by 4, not divisible by 100)  rule No.2
# eg. 1700  (divisible by 4, divisible by 100)      rule No.2.2
# eg. 1703  (not divisible by 4, not divisible by 100)  rule No.2.1


def is_leap_year(year):
    print(f"rule 1 = {year % 400 == 0}")
    print(f"rule 2.1 = {year % 4 == 0}")
    print(f"rule 2.2 = {year % 100 != 0}")
    return ( year % 400 == 0 ) or ( year % 4 == 0 and year % 100 != 0 )


print(is_leap_year(2024))

################################################

=> divisible by 4, + 1 days  
=> -3d by 400 years 

################################################

# 24 h = 1 d, 365 d = 1 year
# 1 d = 1 round of earth                 (24 h)
# 1 year = 1 round of earth to the sun   (24 * 354) + 6 h
# 4 year = 6 + 6 + 6 + 6 = 1 day (24 h)

# 1601(6), 1602(12), 1603(18), 1604(24) -> divisible by 4, + 1 days  
# 1700(100 years later)                 -> not add a day
# 2000 (400 years later)                -> add a day

# 6 hours = 5h 45.6 minutes
# 1 year = 14.4 minutes
# 100 year = not add a day (1440  minutes)

# 400 year = add a day  ( -3d by 400 years )
# 2025

################################################

11. summation
    => summation of 5 = 1 + 2 + 3 + 4 + 5 = 15

# 5 = 1 to 5     => range(1, 6)
# 100 = 1 to 100 => range(1, 101)
# n = 1 to n     => range(1, n+1)

# summation of 5 = 1 + 2 + 3 + 4 + 5 = 15
# t = 0,
# t += 1 = 1
# t += 2 = 3
# t += 3 = 6
# t += 4 = 10
# t += 5 = 15


def summation(n, /):
    t = 0
    for i in range(1, n+1): # 5 = range(1, 6) = 1, 2, 3, 4, 5
        t += i
    return t

print(summation(5))

################################################

12. factorial(n) (မြှောက်ဖော်ကိန်း)
    => factorial of 5 = 1 * 2 * 3 * 4 * 5 = 120
    
# factorial of 5 = 1 * 2 * 3 * 4 * 5 = 120
# t = 1
# t *= 1 = 1
# t *= 2 = 2
# t *= 3 = 6
# t *= 4 = 24
# t *= 5 = 120

def factorial(n, /):
    t = 1
    for i in range(1, n+1): # 5 = range(1, 6) = 1, 2, 3, 4, 5
        t *= i
    return t

print(factorial(5))

################################################

13. reverse_string(s) (string ကိုနောက်ကစပြီး ပြောင်းပြန်ရေးခြင်း။) ( [::-1] )


def reverse_string(s, /):
    return s[::-1]


print(reverse_string("I go to school.")) # .loohcs ot og I

################################################

14. count_vowels(s) (စာလုံးထဲက a, e, i, o, u ရေတွက်ခြင်း။)


def count_vowels(s):
    t = 0
    for c in s:
        if c in "aeiouAEIOU":
            t += 1
    return t


print(count_vowels("I go to school."))

################################################

15. count_vowels(s) (စာလုံးထဲက a, e, i, o, u ဘယ်နှစ်လုံးရှိလဲရေတွက်ခြင်း။)

# t = {}
# t[k] = v
# t["I"] = 1 => {"I": 1, }
# t["o"] = 1 => {"I": 1, "o": 1 }
# t["o"] += 1 => {"I": 1, "o": 2 }


def count_vowels(s):
    t = {}
    for c in s:
        if c in "aeiouAEIOU":
            if c not in t:
                t[c] = 1
            else:
                t[c] += 1

    return t


print(count_vowels("I go to school."))

################################################

16. sum_of_list(lst) (စာရင်းထဲက နံပါတ်တွေကို ပေါင်းခြင်း။)


def sum(lst):
    t = 0
    for n in lst:
        t += n
    return t


marks = [63, 65, 64, 78, 59, 75]

print(sum(marks))

################################################

17. max(lst) (အများဆုံးတန်ဖိုး ရှာခြင်း။)


def greater_number(n1, n2):
    if n1 > n2:
        return n1
    else:
        return n2


def max(lst):
    m = lst[0] # first value => 63

    for n in lst[1:]: # 65, 64, 78, 59, 75
        m = greater_number(m, n) # 63, 65 = 65.  65, 64 = 65. 65, 78 = 78. 78, 59 = 78. 78, 75 = 78

    return m


marks = [63, 65, 99, 64, 78, 97]
print(max(marks))


################################################

18. min(lst) (အနည်းဆုံးတန်ဖိုး ရှာခြင်း။)

def less_number(n1, n2):
    if n1 < n2:
        return n1
    else:
        return n2


def min(lst):
    m = lst[0] # first value => 63

    for n in lst[1:]: # 65, 64, 78, 59, 75
        m = less_number(m, n) # 63, 65 = 65.  65, 64 = 65. 65, 78 = 78. 78, 59 = 78. 78, 75 = 78

    return m


marks = [63, 65, 99, 64, 78, 97]
print(min(marks))


################################################

19. find_max_min(lst) အများဆုံးနဲ့ အနည်းဆုံးတန်ဖိုး ရှာခြင်း။ 


def greater_number(n1, n2):
    if n1 > n2:
        return n1
    else:
        return n2


def less_number(n1, n2):
    if n1 < n2:
        return n1
    else:
        return n2


def max(lst):
    m = lst[0] # first value => 63

    for n in lst[1:]: # 65, 64, 78, 59, 75
        m = greater_number(m, n) # 63, 65 = 65.  65, 64 = 65. 65, 78 = 78. 78, 59 = 78. 78, 75 = 78

    return m


def min(lst):
    m = lst[0] # first value => 63

    for n in lst[1:]: # 65, 64, 78, 59, 75
        m = less_number(m, n) # 63, 65 = 65.  65, 64 = 65. 65, 78 = 78. 78, 59 = 78. 78, 75 = 78

    return m


def min_max(lst):
    return (min(lst), max(lst))


marks = [63, 65, 99, 64, 78, 97]
print(min_max(marks))

################################################################################################

20. linear search


atoms = ["Hydrogen", "Helium", "Lithium", "Beryllium",
         "Boron", "Carbon", "Nitrogen", "Oxygen", "Fluorine",
         "Neon", "Sodium", "Magnesium", "Aluminium", "Silicon",
         "Phosphorus", "Sulfur", "Chlorine", "Argon", "Potassium",
         "Calcium", "Scandium", "Titanium", "Vanadium", "Chromium",
         "Manganese", "Iron", "Cobalt", "Nickel", "Copper", "Zinc",
         "Manganese" "Germanium", "strontium",
         "Gallium", "Germanium", "Arsenic", "Selenium", "Bromine",
         "Krypton", "Rubidium", "Strontium", "Yttrium", "Zirconium",
         "Niobium", "Molybdenum", "Technetium", "Ruthenium", "Rhodium",
         "Palladium", "Silver", "Cadmium", "Indium", "Tin", "Antimony", "Barium",
         "Tellurium", "Iodine", "Xenon", "Cesium", "Barium", "Lanthanum",
         "Cerium", "Praseodymium", "Neodymium", "Promethium", "Samarium",
         "Europium", "Gadolinium", "Terbium", "Dysprosium", "Holmium",
         "Erbium", "Thulium", "Ytterbium", "Lutetium", "Hafnium", "Tantalum",
         "Tungsten", "Platinum", "Gold",
         "Mercury", "Astatine", "Radon", "Francium", "Radium"]

################################################

20.1.Normal Search

for i in atoms:
    if i == "Lithium":
        print("We found Lithium.")
        break

################################################
      
20.2.Search index

for i in range(len(atoms)): # 84 => 0 to 83
    if atoms[i] == "Lithium":
        print("We found Lithium. \nIndex of li = ", i)
        break

################################################
        
20.3.Search index and position   
 
for i in range(len(atoms)): # 84 => 0 to 83
    if atoms[i] == "Lithium":
        print("We found Lithium.")
        print("Index of li = ", i)
        print("Position of li =", i + 1)
        break

################################################

20.4.Search index and position of input data        
        
name = input("Enter a search term: ")

for i in range(len(atoms)):
    if atoms[i] == name:
        print(f"We found {name}.")
        print(f"Index of {name} = ", i)
        print(f"Position of {name} =", i + 1)
        print("- " * 40)

################################################

20.5.Search and count (0, +1)

name = input("Enter a search term: ")
n = 0

for i in range(len(atoms)):
    if atoms[i] == name:
        n += 1
        print(f"We found {name}.")
        print(f"Position of {name} =", i + 1)
        print("- " * 40)

print(f"Count of {name} = {n}")

################################################

20.6.Uppercase and Lowercase should be the same element.  (all to lowercase)

name = input("Enter a search term: ")  
n = 0

for i in range(len(atoms)):
    if atoms[i].lower() == name.lower(): # # LITHIUM, Lithium => lithium
        n += 1
        print(f"We found {name}.")
        print(f"Position of {name} =", i + 1)
        print("- " * 40)

print(f"Count of {name} = {n}")

################################################

20.7.Uppercase and Lowercase should be the same element.  (all to Uppercase)

name = input("Enter a search term: ")
n = 0

for i in range(len(atoms)):
    if atoms[i].upper() == name.upper(): # # LITHIUM, Lithium => LITHIUM
        n += 1
        print(f"We found {name}.")
        print(f"Position of {name} =", i + 1)
        print("- " * 40)

print(f"Count of {name} = {n}")

################################################

20.8.Effect only function

def linear_search(collection, element):
    n = 0
    for i in range(len(collection)):
        if collection[i].upper() == element.upper():  # # LITHIUM, Lithium => lithium
            n += 1
            print(f"We found {element}.")
            print(f"Position of {element} =", i + 1)
    print(f"Count of {element} = {n}")
    print("- " * 40)
    
################################################

20.9.Result only function

def linear_search(collection, element):
    for i in range(len(collection)):
        if collection[i].upper() == element.upper():  
            return True
    return False
    
################################################

20.10.Searching all index of apple 
   
def linear_search(collection, element):
    l = []
    for i in range(len(collection)):
        if collection[i].upper() == element.upper():  # # LITHIUM, Lithium => lithium
            l.append(i)
    return l


fruits = ["banana", "orange", "apple", "mangoes", "apple"]

apple = linear_search(fruits, "apple")  # [2, 4]
print(apple)

################################################

20.11.Searching all positions of apple 

def linear_search(collection, element):
    l = []
    for i in range(len(collection)):
        if collection[i].upper() == element.upper():
            l.append(i + 1)
    return l


fruits = ["banana", "orange", "apple", "mangoes", "apple"]

apple = linear_search(fruits, "apple")  # [3, 5]
print(apple)

################################################

20.12.Count and Searching all positions

def linear_search(collection, element):
    p = []
    n = 0
    for i in range(len(collection)):
        if collection[i].upper() == element.upper():
            p.append(i + 1)
            n += 1
    return n, p


fruits = ["banana", "orange", "apple", "mangoes", "apple"]

apple = linear_search(fruits, "apple")  # (2, [3, 5])
print(apple)

################################################

21. Upper and Lower 

21.1. Uppercase character to lowercase character

A -> 65
a -> 97
A to a  ( +32 )

u = "A"
l = chr(ord(u) + 32)
print(l)

################################################

21.2. Lowercase character to uppercase character
A -> 65
a -> 97
a to A  ( -32 )


l = "a"
u = chr(ord(l) - 32)
print(u)

################################################

21.3. Uppercase character to lowercase character

s = "APPLE"

for c in s:
    l = chr(ord(c) + 32)
    print(l)


a
p
p
l
e

################################################

21.4. Uppercase character string to lowercase character string

s = "APPLE"
ans = ""

for c in s:
    l = chr(ord(c) + 32)
    ans = ans + l

print(ans) # apple

################################################

21.5. Lowercase character string to Uppercase character string

s = "apple"
ans = ""

for c in s:
    l = chr(ord(c) - 32)
    ans = ans + l

print(ans) # APPLE

################################################

21.6. Test Case and Error handling

A ->   65  =>  33 => !
=> c in "abcdefghijklmnopqrstuvwxyz"

################################################

21.7. L to U

s = "ApplEfiwhfbwebfGIGG-+ I go to school."
ans = ""

for c in s:
    if c in "abcdefghijklmnopqrstuvwxyz":
        ans = ans + chr(ord(c) - 32)
    else:
        ans = ans + c

print(ans)


################################################

21.8. U to L

s = "ApplEfiwhfbwebfGIGG-+ I go to school."
ans = ""

for c in s:
    if c in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
        ans = ans + chr(ord(c) + 32)
    else:
        ans = ans + c

print(ans)


################################################

21.9. effect only function

def lower(s):
    ans = ""

    for c in s:
        if c in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
            ans = ans + chr(ord(c) + 32)
        else:
            ans = ans + c

    print(ans)


lower("ApplEfiwhfbwebfGIGG-+ I go to school.") # applefiwhfbwebfgigg-+ i go to school.

################################################

21.10. result only function

def lower(s):
    ans = ""

    for c in s:
        if c in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
            ans = ans + chr(ord(c) + 32)
        else:
            ans = ans + c

    return ans


x = lower("Lithium") # lithium
print(x)

################################################

21.11.  lower in linearsearch

def lower(s):
    ans = ""

    for c in s:
        if c in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
            ans = ans + chr(ord(c) + 32)
        else:
            ans = ans + c

    return ans


# count and all positions
def linear_search(collection, element):
    p = []
    n = 0
    for i in range(len(collection)):
        if lower(collection[i]) == lower(element):
            p.append(i + 1)
            n += 1
    return n, p


fruits = ["banana", "orange", "apple", "mangoes", "apple"]

apple = linear_search(fruits, "Apple")  # (2, [3, 5])
print(apple)


################################################

21.12. upper in linearsearch

def upper(s):
    ans = ""

    for c in s:
        if c in "abcdefghijklmnopqrstuvwxyz":
            ans = ans + chr(ord(c) - 32)
        else:
            ans = ans + c

    return ans


# count and all positions
def linear_search(collection, element):
    p = []
    n = 0
    for i in range(len(collection)):
        if upper(collection[i]) == upper(element):
            p.append(i + 1)
            n += 1
    return n, p


fruits = ["banana", "orange", "apple", "mangoes", "apple"]

apple = linear_search(fruits, "Apple")  # (2, [3, 5])
print(apple)


################################################

c. sort() => if str, sort by ordinal No.

A -> 65
B -> 66

[7, 1, 2, 5, 8] => [1, 2, 5, 7, 8]
"BCA"           => 66 67 65 =>  65 66 67 =  "ABC"
"BCa"           => 66 67 97 =>  "BCa" 


################################################################################################

22. Binary search

1. sort

2. middle value, compare
3. if value is greater, Right
   if value is smaller, left
   
4. if found, break
5. if empty, break 


################################################

[9, 4, 3, 2, 6, 1, 8, 5]   # 6 sec

[1, 2, 3, 4, 5, 6, 8, 9]  

0

middle = 5
[1, 2, 3, 4,]

middle = 3
[1, 2]

middle = 2
[1]
  
middle = 1, empty = don't found  (4)

################################################


[100, 207, 208, 301, 315, 1000, 1001, 3000] 

2000

middle = 315
[315, 1000, 1001, 3000] 

middle = 1001
[1001, 3000] 

middle = 3000
[1001,]

middle = 1001, empty = don't found    (4)

################################################


[100, 207, 208, 301, 315, 1000, 1001, 3000] 

207

m = 315
[100, 207, 208, 301,]

m = 208
[100, 207,]

m = 207, found 207, break (3)

################################################

Binary search
1. sort

2. middle value, compare
3. if value is smaller, left
   if value is greater, Right
  
4. if found, break
5. if empty, break

middle value = c[t//2]
compare
- equal -> m == e
- if value is smaller, e < m
  - Left c[:m] 
- if value is greater, e > m
  - Right c[m:] 
- break
- empty , len == 0, len < 1
- not empty, len != 0, len > 0

################################################

last one element for left => [1] 
l = c[:0] -> empty

################################################

last one element for right => [9]
r = [0:]  -> [9]
never empty and need to stop process by ourself => if len(collection) == 1: break

################################################

22. Binary search

collection = [1, 2, 3, 4, 5, 6, 8, 9] # 8
e = 10


while len(collection) > 0: # [9]
    total = len(collection) # 1
    m = total // 2          # 0
    middle_value = collection[m] # [1, 2, 3, 4, 5, 6, 8, 9] -> 5, [1, 2, 3, 4] -> 3, [1, 2] -> 2, [1,] -> 1

    # print(collection, middle_value)

    #  middle value, compare
    if middle_value == e:
        print(f"found {e}.")
        break

    # if value is smaller, left
    elif e < middle_value:
        collection = collection[:m] # [1, 2, 3, 4] -> [1, 2], [1,] , [:0] -> []

    # if value is greater, Right
    elif e > middle_value:
        if len(collection) == 1: # for last element
            break

        collection = collection[m:] #  [5, 6, 8, 9],  [8, 9], [9] , r = [0:]  -> [last]

################################################

linear Vs Binary

"Lithium"  ->   3, 6
"Gold"     ->   78, 6

1          ->   1, 19
1000000    ->   1000000, 19

################################################

while len(collection) > 0: 
    total = len(collection) 
    m = total // 2        
    middle_value = collection[m] 

    print(collection, middle_value)
    print()

    #  middle value, compare
    if middle_value == e:
        print(f"found {e}.")
        break

    # if value is smaller, left
    elif e < middle_value:
        collection = collection[:m] 

    # if value is greater, Right
    elif e > middle_value:
        if len(collection) == 1:
            break

        collection = collection[m:]

################################################

22.1. Effect only function

def binary_search(collection, e):
    n = 0
    collection = sorted(collection)
    print(collection)
    while len(collection) > 0:  # [9]
        total = len(collection)  # 1
        m = total // 2  # 0
        middle_value = collection[m]  # [1, 2, 3, 4, 5, 6, 8, 9] -> 5, [1, 2, 3, 4] -> 3, [1, 2] -> 2, [1,] -> 1

        print(collection, middle_value)
        print()

        #  middle value, compare
        if middle_value == e:
            print(f"found {e}.")
            break

        # if value is smaller, left
        elif e < middle_value:
            collection = collection[:m]  # [1, 2, 3, 4] -> [1, 2], [1,] , [:0] -> []

        # if value is greater, Right
        elif e > middle_value:
            if len(collection) == 1:
                break

            collection = collection[m:]  # [5, 6, 8, 9],  [8, 9], [9] , r = [0:]  -> [last]
        n += 1
    print(n)
    
    
################################################

22.2.Result only function 


def binary_search(collection, e):
    e = e.capitalize()
    collection = sorted(collection)
    while len(collection) > 0:  # [9]
        total = len(collection)  # 1
        m = total // 2  # 0
        middle_value = collection[m]  # [1, 2, 3, 4, 5, 6, 8, 9] -> 5, [1, 2, 3, 4] -> 3, [1, 2] -> 2, [1,] -> 1

        #print(collection, middle_value)
        #print()

        #  middle value, compare
        if middle_value == e:
            return True

        # if value is smaller, left
        elif e < middle_value:
            collection = collection[:m]  # [1, 2, 3, 4] -> [1, 2], [1,] , [:0] -> []

        # if value is greater, Right
        elif e > middle_value:
            if len(collection) == 1:
                break

            collection = collection[m:]  # [5, 6, 8, 9],  [8, 9], [9] , r = [0:]  -> [last]

    return False


################################################

22.3. Final results of linear search and binary search (for education purpose)


def linear_search(collection, element):
    for i in range(len(collection)):
        if collection[i].upper() == element.upper():
            return True
    return False


def binary_search(collection, e):
    e = e.capitalize()
    collection = sorted(collection)
    while len(collection) > 0:  # [9]
        total = len(collection)  # 1
        m = total // 2  # 0
        middle_value = collection[m]  # [1, 2, 3, 4, 5, 6, 8, 9] -> 5, [1, 2, 3, 4] -> 3, [1, 2] -> 2, [1,] -> 1

        #print(collection, middle_value)
        #print()

        #  middle value, compare
        if middle_value == e:
            return True

        # if value is smaller, left
        elif e < middle_value:
            collection = collection[:m]  # [1, 2, 3, 4] -> [1, 2], [1,] , [:0] -> []

        # if value is greater, Right
        elif e > middle_value:
            if len(collection) == 1:
                break

            collection = collection[m:]  # [5, 6, 8, 9],  [8, 9], [9] , r = [0:]  -> [last]

    return False


atoms = ["Hydrogen", "Helium", "Lithium", "Beryllium",
         "Boron", "Carbon", "Nitrogen", "Oxygen", "Fluorine",
         "Neon", "Sodium", "Magnesium", "Aluminium", "Silicon",
         "Phosphorus", "Sulfur", "Chlorine", "Argon", "Potassium",
         "Calcium", "Scandium", "Titanium", "Vanadium", "Chromium",
         "Manganese", "Iron", "Cobalt", "Nickel", "Copper", "Zinc",
         "Manganese" "Germanium", "Strontium",
         "Gallium", "Germanium", "Arsenic", "Selenium", "Bromine",
         "Krypton", "Rubidium", "Strontium", "Yttrium", "Zirconium",
         "Niobium", "Molybdenum", "Technetium", "Ruthenium", "Rhodium",
         "Palladium", "Silver", "Cadmium", "Indium", "Tin", "Antimony", "Barium",
         "Tellurium", "Iodine", "Xenon", "Cesium", "Barium", "Lanthanum",
         "Cerium", "Praseodymium", "Neodymium", "Promethium", "Samarium",
         "Europium", "Gadolinium", "Terbium", "Dysprosium", "Holmium",
         "Erbium", "Thulium", "Ytterbium", "Lutetium", "Hafnium", "Tantalum",
         "Tungsten", "Platinum", "Gold",
         "Mercury", "Astatine", "Radon", "Francium", "Radium"]

ans = linear_search(atoms, "gold")
print(ans)

ans = binary_search(atoms, "gold")
print(ans)


ans = linear_search(atoms, "X")
print(ans)

ans = binary_search(atoms, "X")
print(ans)

################################################################################################

leap year (ရက်ထပ်နှစ်) (and, or)

# 1. divisible by 400 ( eg. 2000, 1600 )    ( y % 400 == 0 )
# 2. divisible by 4 + not divisible by 100   ( y % 4 == 0 and y % 100 != 0 )
# Rule.1 or Rule.2
1 or ( 2.1 and 2.2 )

# eg. 1600  (divisible by 400) rule No.1

# eg. 1704  (divisible by 4, not divisible by 100)  rule No.2
# eg. 1700  (divisible by 4, divisible by 100)      rule No.2.2
# eg. 1703  (not divisible by 4, not divisible by 100)  rule No.2.1


def is_leap_year(year):
    print(f"rule 1 = {year % 400 == 0}")
    print(f"rule 2.1 = {year % 4 == 0}")
    print(f"rule 2.2 = {year % 100 != 0}")
    return ( year % 400 == 0 ) or ( year % 4 == 0 and year % 100 != 0 )
    

def is_leap_year(year):
    return ( year % 400 == 0 ) or ( year % 4 == 0 and year % 100 != 0 )


print(is_leap_year(1600))

################################################

=> divisible by 4, + 1 days  
=> -3d by 400 years 

################################################

# 24 h = 1 d, 365 d = 1 year
# 1 d = 1 round of earth                 (24 h)
# 1 year = 1 round of earth to the sun   (24 * 365) + 6 h
# 4 year = 6 + 6 + 6 + 6 = 1 day (24 h)

# 1601(6), 1602(12), 1603(18), 1604(24) -> divisible by 4, + 1 days  
# 1700(100 years later)                 -> not add a day
# 2000 (400 years later)                -> add a day

# 6 hours = 5h 45.6 minutes
# 1 year = 14.4 minutes
# 100 year = not add a day (1440  minutes)  

# 400 year = add a day  ( -3d by 400 years )

################################################################################################

"""

