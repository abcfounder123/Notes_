
"""

Day.19

1. is_even (တန်ဖိုးတစ်ခုခုကို 2 နဲ့စားလို့ အကြွင်း 0 ရရင် စုံကိန်းဖြစ်ပါတယ်။)( n % 2 == 0)

2. is_odd (တန်ဖိုးတစ်ခုခုကို 2 နဲ့စားလို့ အကြွင်း 1 ရရင် မကိန်းဖြစ်ပါတယ်။) ( n % 2 == 1 )

3. is_number (0 1 2 3 4 5 6 7 8 9 စတာတွေဟာ နံပါတ်တွေဖြစ်ကြပါတယ်။) ( c in "0123456789" )

is_alphabet (a to z တွေနဲ့ ကကြီး ခကွေးလိုမျိုးတွေက အက္ခရာဖြစ်ပါတယ်။)

4. English alphabet

5. English alphabet + Myanmar alphabet by unicode

6. Myanmar alphabet

7. palindrome (နောက်ပြန်ဖတ်လျှင်လည်း ထပ်တူညီသော စကား) eg. madam ( str == str[::-1] )

8. greater number (ပိုကြီးတဲ့ နံပါတ်) ( n1 > n2 ) 

9. less number ( n1 < n2 )

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

################################################################################################


1. is_even (တန်ဖိုးတစ်ခုခုကို 2 နဲ့စားလို့ အကြွင်း 0 ရရင် စုံကိန်းဖြစ်ပါတယ်။)( n % 2 == 0)


def is_even(n):
    if n % 2 == 0:
        print("even number")
    else:
        print("not even number")


def is_even(n):
    if n % 2 == 0:
        return True
    else:
        return False


def is_even(n):
    return n % 2 == 0


numbers = [1, 3, 2, 6, 8, 28, 100, 20]

for number in numbers:
    if is_even(number):
        print(f"{number} is an even number.")
    else:
        print(f"{number} is not an even number.")

################################################

2. is_odd (တန်ဖိုးတစ်ခုခုကို 2 နဲ့စားလို့ အကြွင်း 1 ရရင် မကိန်းဖြစ်ပါတယ်။) ( n % 2 == 1 )

def is_odd(n):
    return n % 2 == 1
    
################################################

3. is_number (0 1 2 3 4 5 6 7 8 9 စတာတွေဟာ နံပါတ်တွေဖြစ်ကြပါတယ်။) ( c in "0123456789" )


def is_number(c):
    return c in "0123456789"


s = "ahgfwekhfh14schd382"

for c in s:
    if is_number(c):
        print(f"{c} is a number letter.")
    else:
        print(f"{c} is not a number letter.")

################################################

4. English alphabet


def is_alphabet(c):
    return c in "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
    

s = "I go to school."
for c in s:
    if is_alphabet(c):
        print(f"{c} is an alphabet.")

################################################

5. English alphabet + Myanmar alphabet by unicode

65 to 90        A to Z            list(range(65, 91))
97 to 122       a to z            list(range(97, 123))
4096 to 4129    က to အ          list(range(4096, 4130))

list(range(65, 91)) + list(range(97, 123))  

[65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122]


def is_alphabet(c):
    return ord(c) in list(range(65, 91)) + list(range(97, 123)) + list(range(4096, 4130))


s = "AI go to က အ 193 2school."
for c in s:
    if is_alphabet(c):
        print(f"{c} is an alphabet.")

################################################

6. Myanmar alphabet


def is_myn_alphabet(c):
    return ord(c) in list(range(4096, 4130))


################################################

7. palindrome (နောက်ပြန်ဖတ်လျှင်လည်း ထပ်တူညီသော စကား) eg. madam ( str == str[::-1] )

"madam"
"abcd" == "dcba"

x = "abcd"
r = x[::-1]     # "dcba"
print(x)
print(r)

def is_palindrome(s):
    return s == s[::-1]

################################################

8. greater number (ပိုကြီးတဲ့ နံပါတ်) ( n1 > n2 ) 

n1   n2

n1 > n2    ->   n1
n2 > n1    ->   n2
n1 == n2   ->   None


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

9. less number  ( n1 < n2 )


def less_number(n1, n2):
    if n1 < n2:
        return n1

    else:
        return n2
        

################################################

11. summation
    => summation of 5 = 1 + 2 + 3 + 4 + 5 = 15
    
summation of 5 = 1 + 2 + 3 + 4 + 5 = 15     
summation of 6 = 1 + 2 + 3 + 4 + 5 + 6 = 21

summation of 5 = 1 to 5 = range(1, 6)
summation of 6 = 1 to 6 = range(1, 7)
summation of 7 = 1 to 7 = range(1, 8)
summation of n = 1 to n = range(1, n+1)

summation of 5

1 to 5
ans = 0
ans += 1     --->   1
ans += 2     --->   3
ans += 3     --->   6
ans += 4     --->   10
ans += 5     --->   15


def summation(n):
    ans = 0
    for i in range(1, n+1): # 1 2 3 4 5
        ans += i
    return ans


print(summation(10))
    
################################################

12. factorial(n) (မြှောက်ဖော်ကိန်း)
    => factorial of 5 = 1 * 2 * 3 * 4 * 5 = 120
    
factorial of 5 = 1 * 2 * 3 * 4 * 5 = 120
 
1 to 5
ans = 1
ans *= 1     --->   1
ans *= 2     --->   2
ans *= 3     --->   6
ans *= 4     --->   24
ans *= 5     --->   120


def factorial(n):
    ans = 1
    for i in range(1, n+1): # 1 2 3 4 5
        ans *= i
    return ans


print(factorial(5))
    
################################################

13. reverse_string(s) (string ကိုနောက်ကစပြီး ပြောင်းပြန်ရေးခြင်း။) ( [::-1] )


def reverse_string(s):
    return s[::-1]


x = "I go to school."
print(reverse_string(x))


################################################

14. count_vowels(s) (စာလုံးထဲက a, e, i, o, u ရေတွက်ခြင်း။)

x = "I go to school."

t = 0
t += 1      1
t += 1      2
t += 1      3
t += 1      4
t += 1      5


def count_vowels(s):
    t = 0
    for c in s:
        if c in "AEIOUaeiou":
            t += 1
    return t

            
x = "I go to school."
print(count_vowels(x))

################################################

15. count_vowels(s) (စာလုံးထဲက a, e, i, o, u ဘယ်နှစ်လုံးရှိလဲရေတွက်ခြင်း။)

x = "I go to school."

t = 0
t += 1      1
t += 1      2
t += 1      3
t += 1      4
t += 1      5

I    ->   1
o    ->   4

d = {}

Add item
d["I"] = 1          ->    {'I': 1}
d["o"] = 1          ->    {'I': 1, 'o': 1}

Update value
d["o"] += 1         ->    {'I': 1, 'o': 2} 
d["o"] += 1         ->    {'I': 1, 'o': 3}
d["o"] += 1         ->    {'I': 1, 'o': 4}


def count_vowels(s):
    d = {}
    for c in s:
        if c in "AEIOUaeiou":
            if c not in d:
                d[c] = 1
            else:
                d[c] += 1
    return d


x = "I go to school by bus."
print(count_vowels(x))

################################################


def count_vowels(s):
    d = {}
    t = 0
    for c in s:
        if c in "AEIOUaeiou":
            t += 1
            if c not in d:
                d[c] = 1
            else:
                d[c] += 1
    return t, d


x = "I go to school by bus."
print(count_vowels(x))


################################################

16. sum_of_list(lst) (စာရင်းထဲက နံပါတ်တွေကို ပေါင်းခြင်း။)


def sum(lst):
    t = 0
    for n in lst:
        t += n
    return t


x = [10, 30, 40, 50, 100, 1, 2]
print(sum(x))

################################################ 

17. max(lst) (အများဆုံးတန်ဖိုး ရှာခြင်း။)

x = [10, 30, 100, 40, 50]

m = 10
10, 30         m = 30
30, 100        m = 100
100, 40        m = 100
100, 50        m = 100


def greater_number(n1, n2):
    if n1 > n2:
        return n1

    else:
        return n2


def max(lst):
    m = x[0] 
    for n in lst[1:]:
        m = greater_number(m, n)
    return m


x = [10, 30, 100, 40, 50]
print(max(x))

################################################

18. min(lst) (အနည်းဆုံးတန်ဖိုး ရှာခြင်း။)

x = [10, 30, 100, 40, 50]

m = 10
10, 30         m = 10
m, 100         m = 10
m, 40          m = 10
m, 50          m = 10


def less_number(n1, n2):
    if n1 < n2:
        return n1
    else:
        return n2


def min(lst):
    m = x[0]
    for n in lst[1:]:
        m = less_number(m, n)
    return m


x = [10, 30, 100, 40, 50, 2]
print(min(x))

################################################

19. find_max_min(lst) အများဆုံးနဲ့ အနည်းဆုံးတန်ဖိုး ရှာခြင်း။ 


def find_max_min(lst):
    return max(lst), min(lst)


################################################


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
    m = x[0]
    for n in lst[1:]:
        m = greater_number(m, n)
    return m


def min(lst):
    m = x[0]
    for n in lst[1:]:
        m = less_number(m, n)
    return m


def find_max_min(lst):
    return max(lst), min(lst)
    
    
################################################


def max_min(lst):
    max = x[0]
    min = x[0]

    for n in lst[1:]:
        if max > n:
             pass
        else:
            max = n

    for n in lst[1:]:
        if min < n:
             pass
        else:
            min = n

    return  max, min
    
    
################################################################################################

"""
