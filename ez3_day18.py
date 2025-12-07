
"""

Day. 18

Procedural programming
1. Sequence   (T, L, P)
2. Selection  (if, else, elif)
3. loop       (for, while)
4. function   (p, a)

################################################################################################

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

10. summation
    => summation of 5 = 1 + 2 + 3 + 4 + 5 = 15

11. factorial(n) (မြှောက်ဖော်ကိန်း)
    => factorial of 5 = 1 * 2 * 3 * 4 * 5 = 120

12. reverse_string(s) (string ကိုနောက်ကစပြီး ပြောင်းပြန်ရေးခြင်း။) ( [::-1] )

13. count_vowels(s) (စာလုံးထဲက a, e, i, o, u ရေတွက်ခြင်း။)

14. count_vowels(s) (စာလုံးထဲက a, e, i, o, u ဘယ်နှစ်လုံးရှိလဲရေတွက်ခြင်း။)

15. sum_of_list(iter) (စာရင်းထဲက နံပါတ်တွေကို ပေါင်းခြင်း။)

16. max(lst) (အများဆုံးတန်ဖိုး ရှာခြင်း။)

17. min(lst) (အနည်းဆုံးတန်ဖိုး ရှာခြင်း။)

18. find_max_min(lst) အများဆုံးနဲ့ အနည်းဆုံးတန်ဖိုး ရှာခြင်း။ 

19. find_max_min_total_average(lst) အများဆုံးနဲ့ အနည်းဆုံးတန်ဖိုး ရှာခြင်း။ 

20. linear search

21. Binary Search

################################################################################################

1. is_even (တန်ဖိုးတစ်ခုခုကို 2 နဲ့စားလို့ အကြွင်း 0 ရရင် စုံကိန်းဖြစ်ပါတယ်။)( n % 2 == 0)


def is_even(n):
    if n % 2 == 0:
        return True
    else:
        return False


def is_even(n):
    return n % 2 == 0
    
    
################################################
        
2. is_odd (တန်ဖိုးတစ်ခုခုကို 2 နဲ့စားလို့ အကြွင်း 1 ရရင် မကိန်းဖြစ်ပါတယ်။) ( n % 2 == 1 )


def is_odd(n):
    if n % 2 == 1:
        return True
    else:
        return False
        

def is_odd(n):
    return n % 2 == 1
    

def is_odd(n):
    return not (n % 2 == 0)


def is_odd(n):
    return n % 2 != 0

            
################################################

"apple 1 +-"
                                                          
3. is_number (0 1 2 3 4 5 6 7 8 9 စတာတွေဟာ နံပါတ်တွေဖြစ်ကြပါတယ်။) ( c in "0123456789" )


def is_number(c):
    if c in "0123456789":
        return True
    else:
        return False


def is_number(c):
    return c in "0123456789"


################################################

is_alphabet (a to z တွေနဲ့ ကကြီး ခကွေးလိုမျိုးတွေက အက္ခရာဖြစ်ပါတယ်။)

4. English alphabet


def is_english_alphabet(c):
    return c in "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
    
    
def is_english_alphabet(c):
    return ord(c) in list(range(65, 91)) + list(range(97, 123))


################################################    

5. English alphabet + Myanmar alphabet by unicode


65 to 90          A to Z

97 to 122         a to z

4096 to  4129     က to အ


def is_alphabet(c):
    return ord(c) in list(range(65, 91)) + list(range(97, 123)) + list(range(4096, 4130))

################################################

6. Myanmar alphabet

def is_myn_alphabet(c):
    return ord(c) in list(range(4096, 4130))

################################################

7. palindrome (နောက်ပြန်ဖတ်လျှင်လည်း ထပ်တူညီသော စကား) eg. madam 

abcdefg  ==  gfedcba
str  ==  str[::-1]


def is_palindrome(w, /):
    return w == w[::-1]


################################################

8. Greater number   ( n1 > n2 )


n1   n2

n1 > n2:  n1
n2 > n1:  n2
n1 == n2: None

n1 n2

greater        
less than
equal

################################################


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

    else:
        return None
        

def greater_number(n1, n2):
    if n1 > n2:
        return n1

    elif n2 > n1:
        return n2

    else:
        return n2
        

def greater_number(n1, n2):
    if n1 > n2:
        return n1
    else:
        return n2


################################################

9. less number ( n1 < n2 )


def less_number(n1, n2):
    if n1 < n2:
        return n1
    else:
        return n2


print(less_number(1, 2)) # 1
print(less_number(3, 2)) # 2
print(less_number(3, 3)) # 3

################################################

10. Summation

Summation of 5 = 1 + 2 + 3 + 4 + 5 = 15
Summation of 6 = 1 + 2 + 3 + 4 + 5 + 6 = 21

Summation of 5 = 1 to 5 = range(1, 6)
Summation of 6 = 1 to 6 = range(1, 7)
Summation of n = 1 to n = range(1, n+1)

ans = 0
ans += 1    ->  1
ans += 2    ->  3
ans += 3    ->  6
ans += 4    ->  10
ans += 5    ->  15


def summation(n):
    t = 0

    for i in range(1, n + 1):
        t += i

    return t


summation_6 = summation(6)
print(summation_6)

################################################

11. Factorial

Factorialof 5 = 1 * 2 * 3 * 4 * 5 = 120

ans = 1
ans *= 1    ->  1
ans *= 2    ->  2
ans *= 3    ->  6
ans *= 4    ->  24
ans *= 5    ->  120


def factorial(n):
    f = 1
    for i in range(1, n+1):
        f *= i
    return f


f_5 = factorial(5)
print(f_5)

################################################

12. reverse_string


def reverse_string(s):
    return s[::-1]


print(reverse_string("I go to school."))

################################################

13. count vowels()

"aeiou"


def count_vowels(s):
    t = 0
    for c in s:
        if c in "aeiouAEIOU":
            t += 1
    return t


print(count_vowels("I go to school by bicycle."))

################################################

14. count vowels()

"I go to school."

I = 1
o = 4

{}
{"I": 1, }
{"I": 1, "o": 1 }

d["I"] = 1
d["o"] = 1
d["o"] += 1

"o" in d

t[c] = 1    <-- add new item
t[c] += 1   <-- + 1

################################################

def count_vowels(s):
    t = {} # {"I": 1, "o": 2, "i": 1}
    for c in s:
        # print(c)
        if c in "aeiouAEIOU":
            if c in t:
                t[c] += 1
            else:
                t[c] = 1
            # print(t)                           
    return t


print(count_vowels("I go to school by bicycle."))

################################################


def count_vowels(s):
    t = {} # {"I": 1, "o": 2, "i": 1}
    total = 0
    for c in s:
        # print(c)
        if c in "aeiouAEIOU":
            total += 1
            if c in t:
                t[c] += 1
            else:
                t[c] = 1
            # print(t)
                              
    return t, total


print(count_vowels("I go to school by bicycle."))

################################################################################################

Day. 19

15. sum_of_list(iter) (စာရင်းထဲက နံပါတ်တွေကို ပေါင်းခြင်း။)
16. max(lst) (အများဆုံးတန်ဖိုး ရှာခြင်း။)
17. min(lst) (အနည်းဆုံးတန်ဖိုး ရှာခြင်း။)
18. find_max_min(lst) အများဆုံးနဲ့ အနည်းဆုံးတန်ဖိုး ရှာခြင်း။ 
19. find_max_min_total_average(lst) အများဆုံးနဲ့ အနည်းဆုံးတန်ဖိုး ရှာခြင်း။ 
20. linear search
21. Binary Search

################################################################################################

15. sum_of_list(iter) (စာရင်းထဲက နံပါတ်တွေကို ပေါင်းခြင်း။)


def sum(iter):
    t = 0
    for i in iter:
        t += i
    return t

################################################

16. max(lst) (အများဆုံးတန်ဖိုး ရှာခြင်း။)


def greater_number(n1, n2, /):
    if n1 > n2:
        return n1
    else:
        return n2


def max(lst):
    m = lst[0] 
    for i in lst[1:]: 
        m = greater_number(m, i) 
    return m


x = [1, 5, 3, 7, 4, 12, 32, 432, 65, 567, 93]
print(max(x))    

################################################

17. min(lst) (အနည်းဆုံးတန်ဖိုး ရှာခြင်း။)


def less_number(n1, n2, /):
    if n1 < n2:
        return n1
    else:
        return n2


def min(lst):
    m = lst[0]
    for i in lst[1:]:
        m = less_number(m, i)
    return m


x = [5, 3, 7, 4, 12, 32, 432, 65, 567, 93, 1]
print(min(x))

################################################

18. find_max_min(lst) အများဆုံးနဲ့ အနည်းဆုံးတန်ဖိုး ရှာခြင်း။ 

def greater_number(n1, n2, /):
    if n1 > n2:
        return n1
    else:
        return n2


def less_number(n1, n2, /):
    if n1 < n2:
        return n1
    else:
        return n2


def max(lst):
    m = lst[0]
    for i in lst[1:]:
        m = greater_number(m, i)
    return m


def min(lst):
    m = lst[0]
    for i in lst[1:]:
        m = less_number(m, i)
    return m


def max_min(lst):
    return max(lst), min(lst)


x = [5, 3, 7, 4, 12, 32, 432, 65, 567, 93, 1]

max_number, min_number = max_min(x)

print(max_min(x))
print(max_number)
print(min_number)

################################################

19. find_max_min_total_average(lst) အများဆုံးနဲ့ အနည်းဆုံးတန်ဖိုး ရှာခြင်း။ 

[1, 1, 2, 3, 3, 4, 4, 2]

max = 4
min = 1
total = 20
average = t/n = 20/8 = 2.5

################################################


def greater_number(n1, n2, /):
    if n1 > n2:
        return n1
    else:
        return n2


def less_number(n1, n2, /):
    if n1 < n2:
        return n1
    else:
        return n2


def max(lst):
    m = lst[0]
    for i in lst[1:]:
        m = greater_number(m, i)
    return m


def min(lst):
    m = lst[0]
    for i in lst[1:]:
        m = less_number(m, i)
    return m


def sum(iter):
    t = 0
    for i in iter:
        t += i
    return t


def avg(lst):
    return sum(lst)/len(lst)


def max_min(lst):
    return max(lst), min(lst)


def max_min_total_average(lst):
    return max(lst), min(lst), sum(lst), avg(lst)


x = [1, 1, 2, 3, 3, 4, 4, 2]

print(max_min_total_average(x))

################################################

20. linear search

################################################

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

linear search

84
"Hydrogen"   -    0    1
"Gold"       -   78   79
"Radium"     -   83   84

range      -  1 to 84

1_000      -  1 to  1_000

1_000_000  -  1 to  1_000_000

n          -  1 to  n

################################################

iterate and compare
- for atom in atoms:
- atom == "Gold" 

reduce time 
- break

for atom in atoms:
    print(atom)
    if atom == "Carbon":
        print("We found Carbon.")
        break

################################################


def linear_search(collection, element):
    for e in collection:
        if e == element:
            return True
    return False
    
    
element = input("Element : ")
c1 = linear_search(atoms, element)

if c1:
    print(f"We found {element}.")

################################################

21. Binary Search

[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

1    left
5    middle
10   right

################################################

[10, 30, 40, 50, 70, 72, 74, 81, 98, 131, 164]

0

middle = 72
[10, 30, 40, 50, 70]

middle = 40
[10, 30]

middle = 30
[10,]

middle = 10
[]

don't found

################################################

1. sort 
2. middle value, compare equal
3. if value is smaller, left
   if value is greater, right

4. if found, break
5. if empty, break

################################################

e = 10

1. c = [10, 30, 40, 50, 70, 72, 74, 81, 98, 131, 164]       11

2. middle value (m = t//2 -> 5 ),  c[m] ->  72
   compare equal ( middle == e )

3. if value is smaller, left
   - if e < middle, c = c[:m] # 01234, [10, 30, 40, 50, 70]
   if value is greater, right
   - - if e > middle, c = c[m+1:] # 6789 10, [74, 81, 98, 131, 164] 
   
################################################
  
e = 10
  
c = [10, 30, 40, 50, 70, 72, 74, 81, 98, 131, 164]   11, 5  
m = 72
middle == e
e < middle -> c[:m] 

###

c = [10, 30, 40, 50, 70]   5, 2
m = 40
middle == e
e < middle -> c[:m] 

###

c = [10, 30]  2, 1
m = 30
middle == e
e < middle -> c[:m]

###

c = [10]  1, 0
m = 10
middle == e -> if found, break

################################################
  
e = 0
  
c = [10, 30, 40, 50, 70, 72, 74, 81, 98, 131, 164]   11, 5  
m = 72
middle == e
e < middle -> c[:m] 

###

c = [10, 30, 40, 50, 70]   5, 2
m = 40
middle == e
e < middle -> c[:m] 

###

c = [10, 30]  2, 1
m = 30
middle == e
e < middle -> c[:m]

###

c = [10]  1, 0
m = 10
middle == e 
e < middle -> c[:m] 

###

c = [], length = 0
if empty, break

################################################

e = 10

c = [10, 30, 40, 50, 70, 72, 74, 81, 98, 131, 164]

t = len(c) # 11
m = t // 2 # 5
middle = c[m] # 72

if middle == e:
    print("found")
    # break

elif e < middle:
    c = c[:m] # [10, 30, 40, 50, 70]

elif e > middle:
    c = c[m+1:] # [74, 81, 98, 131, 164]
    
################################################

72 -> 1
10 -> 4

Infinite loop
- while

################################################

e = 10

c = [10, 30, 40, 50, 70, 72, 74, 81, 98, 131, 164] # 11
print(c)
print("- " * 39)

while len(c) > 0:
    t = len(c)  #   11  5  2  1
    m = t // 2  #    5  2  1  0
    middle = c[m] # 72 40 30 10
    print(middle)
    if middle == e:
        print("found")
        print("- " * 39)
        break

    elif e < middle:
        c = c[:m]  # [10, 30, 40, 50, 70]  [10, 30] [10]
        print(c)
        print("- " * 39)

    elif e > middle:
        c = c[m + 1:]  # [74, 81, 98, 131, 164]
        print(c)
        print("- " * 39)
        
################################################

[10, 30, 40, 50, 70, 72, 74, 81, 98, 131, 164]
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
72
[10, 30, 40, 50, 70]
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
40
[10, 30]
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
30
[10]
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
10
found
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 

################################################

[10, 30, 40, 50, 70, 72, 74, 81, 98, 131, 164]
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
72
[74, 81, 98, 131, 164]
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
98
[131, 164]
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
164
found
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 

################################################

84

"Hydrogen"   -   0     1     6
"Gold"       -   78   79     4
"Radium"     -   83   84     5

linear search -> 1 to 84
binary search -> 1 to 6

84

42
21
10
5
2
1

################################################

1_000_000
linear search -> 1 to 1_000_000    10
binary search -> 1 to 19            -

1.500000
2.250000
3.125000
4.62500
5.31250
6.15625
7.7812
8.3906
9.1953
10.976
11.488
12.244
13.122
14.61
15.30
16.15
17.7
18.3
19.1

################################################

c = ['Aluminium', 'Antimony', 'Argon', 'Arsenic', 'Astatine', 'Barium', 'Barium', 'Beryllium', 'Boron', 'Bromine', 'Cadmium', 'Calcium', 'Carbon', 'Cerium', 'Cesium', 'Chlorine', 'Chromium', 'Cobalt', 'Copper', 'Dysprosium', 'Erbium', 'Europium', 'Fluorine', 'Francium', 'Gadolinium', 'Gallium', 'Germanium', 'Gold', 'Hafnium', 'Helium', 'Holmium', 'Hydrogen', 'Indium', 'Iodine', 'Iron', 'Krypton', 'Lanthanum', 'Lithium', 'Lutetium', 'Magnesium', 'Manganese', 'ManganeseGermanium', 'Mercury', 'Molybdenum', 'Neodymium', 'Neon', 'Nickel', 'Niobium', 'Nitrogen', 'Oxygen', 'Palladium', 'Phosphorus', 'Platinum', 'Potassium', 'Praseodymium', 'Promethium', 'Radium', 'Radon', 'Rhodium', 'Rubidium', 'Ruthenium', 'Samarium', 'Scandium', 'Selenium', 'Silicon', 'Silver', 'Sodium', 'Strontium', 'Strontium', 'Sulfur', 'Tantalum', 'Technetium', 'Tellurium', 'Terbium', 'Thulium', 'Tin', 'Titanium', 'Tungsten', 'Vanadium', 'Xenon', 'Ytterbium', 'Yttrium', 'Zinc', 'Zirconium']

e = 'Scandium'

print(c)
print("- " * 39)

while len(c) > 0:
    t = len(c)  #   11  5  2  1
    m = t // 2  #    5  2  1  0
    middle = c[m] # 72 40 30 10
    print(middle)
    if middle == e:
        print("found")
        print("- " * 39)
        break

    elif e < middle:
        c = c[:m]  # [10, 30, 40, 50, 70]  [10, 30] [10]
        print(c)
        print("- " * 39)

    elif e > middle:
        c = c[m + 1:]  # [74, 81, 98, 131, 164]
        print(c)
        print("- " * 39)

################################################

atoms = ['Aluminium', 'Antimony', 'Argon', 'Arsenic', 'Astatine', 'Barium', 'Barium', 'Beryllium', 'Boron', 'Bromine', 'Cadmium', 'Calcium', 'Carbon', 'Cerium', 'Cesium', 'Chlorine', 'Chromium', 'Cobalt', 'Copper', 'Dysprosium', 'Erbium', 'Europium', 'Fluorine', 'Francium', 'Gadolinium', 'Gallium', 'Germanium', 'Gold', 'Hafnium', 'Helium', 'Holmium', 'Hydrogen', 'Indium', 'Iodine', 'Iron', 'Krypton', 'Lanthanum', 'Lithium', 'Lutetium', 'Magnesium', 'Manganese', 'ManganeseGermanium', 'Mercury', 'Molybdenum', 'Neodymium', 'Neon', 'Nickel', 'Niobium', 'Nitrogen', 'Oxygen', 'Palladium', 'Phosphorus', 'Platinum', 'Potassium', 'Praseodymium', 'Promethium', 'Radium', 'Radon', 'Rhodium', 'Rubidium', 'Ruthenium', 'Samarium', 'Scandium', 'Selenium', 'Silicon', 'Silver', 'Sodium', 'Strontium', 'Strontium', 'Sulfur', 'Tantalum', 'Technetium', 'Tellurium', 'Terbium', 'Thulium', 'Tin', 'Titanium', 'Tungsten', 'Vanadium', 'Xenon', 'Ytterbium', 'Yttrium', 'Zinc', 'Zirconium']


def linear_search(collection, element):
    for e in collection:
        if e == element:
            return True
    return False


def binary_search(c, e):
    while len(c) > 0:
        t = len(c)
        m = t // 2
        middle = c[m]

        if middle == e:
            return True
        elif e < middle:
            c = c[:m]
        elif e > middle:
            c = c[m + 1:]
    return False


element = input("Element : ")

if linear_search(atoms, element):
    print(f"We found {element}.")

if binary_search(atoms, element):
    print(f"We found {element}.")
    
################################################################################################

"""


