
"""

Exercises

1. is_even (တန်ဖိုးတစ်ခုခုကို 2 နဲ့စားလို့ အကြွင်း 0 ရရင် စုံကိန်းဖြစ်ပါတယ်။)( n % 2 == 0)

------------------------------------------

2. is_odd (တန်ဖိုးတစ်ခုခုကို 2 နဲ့စားလို့ အကြွင်း 1 ရရင် မကိန်းဖြစ်ပါတယ်။) ( n % 2 == 1 )

------------------------------------------

3. is_number (0 1 2 3 4 5 6 7 8 9 စတာတွေဟာ နံပါတ်တွေဖြစ်ကြပါတယ်။) ( c in "0123456789" )

------------------------------------------

is_alphabet (a to z တွေနဲ့ ကကြီး ခကွေးလိုမျိုးတွေက အက္ခရာဖြစ်ပါတယ်။)

4. English alphabet

------------------------------------------

5. English alphabet + Myanmar alphabet by unicode

------------------------------------------

6. Myanmar alphabet

------------------------------------------

7. palindrome (နောက်ပြန်ဖတ်လျှင်လည်း ထပ်တူညီသော စကား) eg. madam ( str == str[::-1] )

------------------------------------------

8. greater number (ပိုကြီးတဲ့ နံပါတ်) ( n1 > n2 )

------------------------------------------

9. less number ( n1 < n2 )

------------------------------------------

10. leap year (ရက်ထပ်နှစ်) (and, or)
    1. divisible by 400 ( eg. 2000, 1600 )    ( y % 400 == 0 )
    2. divisible by 4 + not divisible by 100   ( y % 4 == 0 and y % 100 != 0 )
    - Rule.1 or Rule.2

=> divisible by 4, + 1 days
=> -3d by 400 years

Modern calendar ?

------------------------------------------

11. summation
    => summation of 5 = 1 + 2 + 3 + 4 + 5 = 15

------------------------------------------

12. factorial(n) (မြှောက်ဖော်ကိန်း)
    => factorial of 5 = 1 * 2 * 3 * 4 * 5 = 120

------------------------------------------

13. reverse_string(s) (string ကိုနောက်ကစပြီး ပြောင်းပြန်ရေးခြင်း။) ( [::-1] )

------------------------------------------

14. count_vowels(s) (စာလုံးထဲက a, e, i, o, u ရေတွက်ခြင်း။)

------------------------------------------

15. count_vowels(s) (စာလုံးထဲက a, e, i, o, u ဘယ်နှစ်လုံးရှိလဲရေတွက်ခြင်း။)

------------------------------------------

16. sum_of_list(lst) (စာရင်းထဲက နံပါတ်တွေကို ပေါင်းခြင်း။)

------------------------------------------

17. max(lst) (အများဆုံးတန်ဖိုး ရှာခြင်း။)

------------------------------------------

18. min(lst) (အနည်းဆုံးတန်ဖိုး ရှာခြင်း။)

------------------------------------------

19. find_max_min(lst) အများဆုံးနဲ့ အနည်းဆုံးတန်ဖိုး ရှာခြင်း။

------------------------------------------

20. Uppercase and Lowercase

------------------------------------------

21. linear search

------------------------------------------

22. Binary Search

################################################################################################


1. is_even (တန်ဖိုးတစ်ခုခုကို 2 နဲ့စားလို့ အကြွင်း 0 ရရင် စုံကိန်းဖြစ်ပါတယ်။)( n % 2 == 0)


def is_even(n):
    return n % 2 == 0


------------------------------------------

2. is_odd (တန်ဖိုးတစ်ခုခုကို 2 နဲ့စားလို့ အကြွင်း 1 ရရင် မကိန်းဖြစ်ပါတယ်။) ( n % 2 == 1 )


def is_odd(n):
    return n % 2 == 1


------------------------------------------

def is_even(n):
    return n % 2 == 0


numbers = [100, 105, 3, 9, 1000, 4, 8, 6]
even = []

for number in numbers:
    if is_even(number):
        even.append(number)

print(even)

------------------------------------------

3. is_number (0 1 2 3 4 5 6 7 8 9 စတာတွေဟာ နံပါတ်တွေဖြစ်ကြပါတယ်။) ( c in "0123456789" )

"a"
"6"


def is_number(c):
    return c in "0123456789"


------------------------------------------

Test


def is_number(c):
    return c in "0123456789"


x = '''whgfjew dhu 38dhgjhwgd 383djcgw c8'''
n = 0

for c in x:
    if is_number(c):
        print(f"We found {c}")
        n += 1

print(n)

------------------------------------------

is_alphabet (a to z တွေနဲ့ ကကြီး ခကွေးလိုမျိုးတွေက အက္ခရာဖြစ်ပါတယ်။)

4. English alphabet, English alphabet by ordinal number


def is_alphabet(c):
    return c in "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"


def is_alphabet(c):
    return ord(c) in list(range(65, 91)) + list(range(97, 123))

------------------------------------------

[65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122]

------------------------------------------

5. English alphabet + Myanmar alphabet by ordinal number


def is_alphabet(c):
    return ord(c) in list(range(65, 91)) + list(range(97, 123)) + list(range(4096, 4130))


------------------------------------------

A = 65
Z = 90

a = 97
z = 122

က = 4096
အ = 4129

[65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 4096, 4097, 4098, 4099, 4100, 4101, 4102, 4103, 4104, 4105, 4106, 4107, 4108, 4109, 4110, 4111, 4112, 4113, 4114, 4115, 4116, 4117, 4118, 4119, 4120, 4121, 4122, 4123, 4124, 4125, 4126, 4127, 4128, 4129]

------------------------------------------

6. Myanmar alphabet


def is_alphabet(c):
    return ord(c) in list(range(4096, 4130))


------------------------------------------

7. palindrome (နောက်ပြန်ဖတ်လျှင်လည်း ထပ်တူညီသော စကား) eg. madam ( str == str[::-1] )


def palindrome(s):
    return s == s[::-1]


------------------------------------------

8. greater number (ပိုကြီးတဲ့ နံပါတ်) ( n1 > n2 )


def greater_number(n1, n2):
    if n1 > n2:
        return n1
    else:
        return n2


------------------------------------------

9. less number ( n1 < n2 )


def less_number(n1, n2):
    if n1 < n2:
        return n1
    else:
        return n2


------------------------------------------

"Three steps of greater number"

greater_number(2, 1)   =>  2      <-- n1           1sec    1    1
greater_number(1, 2)   =>  2      <-- n2           2       2    1
greater_number(2, 2)   =>  2      <-- n1 or n2     3       2    1


def greater_number(n1, n2):
    if n1 > n2:
        return n1
    elif n2 > n1:
        return n2
    elif n1 == n2:
        return n2


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

------------------------------------------

10. leap year (ရက်ထပ်နှစ်) (and, or)
    1. divisible by 400 ( eg. 2000, 1600 )       ( y % 400 == 0 )
    2. divisible by 4 and not divisible by 100   ( y % 4 == 0 and y % 100 != 0 )

Rule.1 or Rule.2

=> divisible by 4, + 1 days
=> -3d by 400 years
=>

------------------------------------------

Julian

1. divisible by 4  (y % 4 == 0)


def is_leap_year(y):
    return y % 4 == 0


------------------------------------------

Gregorian


def is_leap_year(y):
    return (y % 400 == 0) or (y % 4 == 0 and y % 100 != 0)


------------------------------------------

Modern calendar

?

------------------------------------------

11. summation
    => summation of 5 = 1 + 2 + 3 + 4 + 5 = 15


def summation(n):
    ans = 0
    for i in range(1, n + 1):
        ans += i
    return ans


------------------------------------------

12. factorial(n) (မြှောက်ဖော်ကိန်း)
    => factorial of 5 = 1 * 2 * 3 * 4 * 5 = 120


def factorial(n):
    ans = 1
    for i in range(1, n + 1):
        ans *= i
    return ans


------------------------------------------

13. reverse_string(s) (string ကိုနောက်ကစပြီး ပြောင်းပြန်ရေးခြင်း။) ( [::-1] )
    - "I go to school."
    - ".loohcs ot og I"


def reverse_string(s):
    return s[::-1]


------------------------------------------

14. count_vowels(s) (စာလုံးထဲက a, e, i, o, u ရေတွက်ခြင်း။)


def count_vowels(s):
    t = 0
    for c in s:
        if c in "aeiouAEIOU":
            t += 1
    return t


------------------------------------------

15. count_vowels(s) (စာလုံးထဲက a, e, i, o, u ဘယ်နှစ်လုံးရှိလဲရေတွက်ခြင်း။)

Add item to dict
d["I"] = 1

Update dict value
d["I"] = 2
d["I"] += 1

------------------------------------------


def count_vowels(s):
    d = {}
    for c in s:
        if c in "aeiouAEIOU":  # I
            if c not in d.keys():
                d[c] = 1
            else:
                d[c] += 1
    return d


------------------------------------------

16. sum_of_list(lst) (စာရင်းထဲက နံပါတ်တွေကို ပေါင်းခြင်း။)


def sum_of_list(lst):
    t = 0
    for n in lst:
        t += n
    return t


------------------------------------------


17. max(lst) (အများဆုံးတန်ဖိုး ရှာခြင်း။)


def max(l):
    m = l[0]
    for n in l[1:]:
        m = greater_number(m, n)
    return m


------------------------------------------

18. min(lst) (အနည်းဆုံးတန်ဖိုး ရှာခြင်း။)


def min(l):
    m = l[0]
    for n in l[1:]:
        m = less_number(m, n)
    return m


------------------------------------------

19. find_max_min(lst) အများဆုံးနဲ့ အနည်းဆုံးတန်ဖိုး ရှာခြင်း။


def find_max_min(l):
    return max(l), min(l)


------------------------------------------

Test


def find_max_min(l):
    max = l[0]
    for n in l[1:]:
        if max > n:
            pass
        else:
            max = n

    min = l[0]
    for n in l[1:]:
        if min < n:
            pass
        else:
            min = n

    return max, min


------------------------------------------

Test


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


def max(l):
    m = l[0]
    for n in l[1:]:
        m = greater_number(m, n)
    return m


def min(l):
    m = l[0]
    for n in l[1:]:
        m = less_number(m, n)
    return m


def find_max_min(l):
    return max(l), min(l)


l = [56, 100, 200, 900, 150, 500, 600, 800]
print(find_max_min(l))

------------------------------------------

21. Uppercase and Lowercase


x = "Apple"
c = x.upper()
l = x.lower()
print(c, l)



def is_lower(c):
    return c in "abcdefghijklmnopqrstuvwxyz"


def lower_upper(l):
    return chr(ord(l) - 32)


def upper(s):
    ans = ""
    for c in s:
        if is_lower(c):
            ans += lower_upper(c)
        else:
            ans += c
    return ans


------------------------------------------


def is_upper(c):
    return c in "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


def upper_lower(u):
    return chr(ord(u) + 32)


def lower(s):
    ans = ""
    for c in s:
        if is_upper(c):
            ans += upper_lower(c)
        else:
            ans += c
    return ans


------------------------------------------

20. linear search


def linear_search(l, element):
    for e in l:
        if e == element:
            return True
    return False


------------------------------------------

22. Binary Search


l = [31, 42, 68, 80, 100, 150, 200]

1. m = 80
2. g => l = [100, 150, 200]

1. m = 150
2. g => l = [200]

1. m = 200
2. g => l = []

------------------------------------------

[31, 42, 68, 80, 100, 150, 200]
compare
   - greater => right  => [m+1:]   => [100, 150, 200]
   - less    => left   => [:m]     => [31, 42, 68]

found => stop True
empty => stop False

------------------------------------------


def binary_search(l, element):
    while len(l) > 0:
        t = len(l)
        m = t // 2
        middle_value = l[m]
        if element == middle_value:
            return True
        elif element > middle_value:
            l = l[m+1:]
        elif element < middle_value:
            l = l[:m]
    return False


------------------------------------------------------------------------------------

"""
