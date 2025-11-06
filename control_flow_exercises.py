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

20.

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

"""

