
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

"""


