
"""

Day.20

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
    return n % 2 == 0


################################################

2. is_odd (တန်ဖိုးတစ်ခုခုကို 2 နဲ့စားလို့ အကြွင်း 1 ရရင် မကိန်းဖြစ်ပါတယ်။) ( n % 2 == 1 )


def is_odd(n):
    return n % 2 == 1


################################################    
    
3. is_number (0 1 2 3 4 5 6 7 8 9 စတာတွေဟာ နံပါတ်တွေဖြစ်ကြပါတယ်။) ( c in "0123456789" )


def is_number(c):
    return c in "0123456789"
    

################################################

is_alphabet (a to z တွေနဲ့ ကကြီး ခကွေးလိုမျိုးတွေက အက္ခရာဖြစ်ပါတယ်။)

4. English alphabet (A to Z)(a to z)


def is_alphabet(c):
    return c in "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"


################################################

5. English alphabet + Myanmar alphabet by unicode


def is_eng_myn_alphabet(c):
    return ord(c) in list(range(65, 91)) + list(range(97, 123)) + list(range(4096, 4130)) 


################################################

6. Myanmar alphabet


def is_myn_alphabet(c):
    return ord(c) in list(range(4096, 4130)) 
    

################################################

7. palindrome (နောက်ပြန်ဖတ်လျှင်လည်း ထပ်တူညီသော စကား) eg. madam ( str == str[::-1] )


def is_palindrome(s):
    return s == s[::-1]
    

################################################

8. greater number (ပိုကြီးတဲ့ နံပါတ်) ( n1 > n2 ) 


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


################################################

11. summation


def summation(n):
    ans = 0
    for i in range(1, n+1):
        ans += i
    return ans


################################################

12. factorial(n) (မြှောက်ဖော်ကိန်း)
    => factorial of 5 = 1 * 2 * 3 * 4 * 5 = 120


def factorial(n):
    ans = 1
    for i in range(1, n+1):
        ans *= i
    return ans


################################################

13. reverse_string(s) (string ကိုနောက်ကစပြီး ပြောင်းပြန်ရေးခြင်း။) ( [::-1] )


def reverse_string(s):
    return s[::-1]
    

################################################

14. count_vowels(s) (စာလုံးထဲက a, e, i, o, u ရေတွက်ခြင်း။)


def count_vowels(s):
    t = 0
    for c in s:
        if c in "aeiouAEIOU":
            t += 1
    return t


################################################

15. count_vowels(s) (စာလုံးထဲက a, e, i, o, u ဘယ်နှစ်လုံးရှိလဲရေတွက်ခြင်း။)


def count_vowels(s):
    d = {}
    for c in s:
        if c in "aeiouAEIOU": 
            if c not in d.keys():
                d[c] = 1
            else:
                d[c] += 1
    return d

################################################

16. sum_of_list(lst) (စာရင်းထဲက နံပါတ်တွေကို ပေါင်းခြင်း။)


def sum_of_list(lst):
    t = 0
    for n in lst:
        t += n
    return t


################################################

17. max(lst) (အများဆုံးတန်ဖိုး ရှာခြင်း။)


def max(lst):
    m = lst[0]  
    for n in lst[1:]:
        m = greater_number(m, n) 
    return m


################################################    

18. min(lst) (အနည်းဆုံးတန်ဖိုး ရှာခြင်း။)


def min(lst):
    m = lst[0] 
    for n in lst[1:]:
        m = less_number(m, n)
    return m


################################################

19. find_max_min(lst) အများဆုံးနဲ့ အနည်းဆုံးတန်ဖိုး ရှာခြင်း။ 


def find_max_min(lst):
    return max(lst), min(lst)
    
    
################################################

21. Uppercase and Lowercase

Uppercase (a to A)  (97 to 65)


def upper(s):
    ans = ""
    for c in s:   # "g"
        if c in "abcdefghijklmnopqrstuvwxyz":
            ans += chr(ord(c) - 32)
        else:
            ans += c
    return ans
    
    
################################################ 
  
Lowercase (A  to a)  (65 to 97)


def lower(s):
    ans = ""
    for c in s:  
        if c in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
            ans += chr(ord(c) + 32)
        else:
            ans += c
    return ans
    

################################################ 

20. linear search


def linear_search(lst, element):
    for e in lst:
        if e == element:
            return True
    return False


################################################ 

22. Binary Search


def binary_search(collection, element):
    while len(collection) > 0:
        t = len(collection)               
        m = t // 2                        
        middle = collection[m]           

        if element == middle:
            return True
        elif element > middle:
            collection = collection[m+1:]     # r
        elif element < middle:
            collection = collection[:m]       # l     
    return False
    
 
################################################

10. leap year (ရက်ထပ်နှစ်) (and, or)


def leap_year(y):
    return ( y % 400 == 0 ) or ( y % 4 == 0 and y % 100 != 0 )


################################################################################################
################################################################################################

1. is_even (တန်ဖိုးတစ်ခုခုကို 2 နဲ့စားလို့ အကြွင်း 0 ရရင် စုံကိန်းဖြစ်ပါတယ်။)( n % 2 == 0)


def is_even(n):
    if n % 2 == 0:
        print("even number.")
    else:
        print("not an even number.")


def is_even(n):
    if n % 2 == 0:
        return True
    else:
        return False


def is_even(n):
    return n % 2 == 0

################################################

x = [1, 2, 3, 4, 5 , 6, 7, 8, 9, 10]
even = []
odd = []

for n in x:
    if is_even(n):
        print(f"{n} is an even number.")
        even.append(n)
    else:
        print(f"{n} is not an even number.")
        odd.append(n)

print(even)
print(odd)

################################################

2. is_odd (တန်ဖိုးတစ်ခုခုကို 2 နဲ့စားလို့ အကြွင်း 1 ရရင် မကိန်းဖြစ်ပါတယ်။) ( n % 2 == 1 )


def is_odd(n):
    return n % 2 == 1
    

################################################

condition True and return True


def is_even(n):
    if n % 2 == 0:  # condition True 
        return True  # return True
    else:
        return False


def is_even(n):
    return n % 2 == 0  # condition True and return True


################################################

condition True and return False


def is_odd(n):
    if n % 2 == 0:  # condition True 
        return False # return False
    else:
        return True


def is_odd(n):
    return not(n % 2 == 0)  #  condition True and return False
    
    
################################################

3. is_number (0 1 2 3 4 5 6 7 8 9 စတာတွေဟာ နံပါတ်တွေဖြစ်ကြပါတယ်။) ( c in "0123456789" )


def is_number(c):
    return c in "0123456789"
    

################################################

s = "I go to school No.123."

for c in s:
    if is_number(c):
        print(f"{c} is a number letter.")
    else:
        print(f"{c} is not a number letter.")

s = "I go to school No.123."
t = 0

for c in s:
    if is_number(c):
        t += 1

print(f"Total = {t}")

################################################

is_alphabet (a to z တွေနဲ့ ကကြီး ခကွေးလိုမျိုးတွေက အက္ခရာဖြစ်ပါတယ်။)

4. English alphabet (A to Z)(a to z)


def is_alphabet(c):
    return c in "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"


################################################

s = "I go to school No.123."

for c in s:
    if is_alphabet(c):
        print(f"{c} is an alphabet.")

t = 0

for c in s:
    if is_alphabet(c):
        t += 1

print(f"Total = {t}")

################################################

5. English alphabet + Myanmar alphabet by unicode

6. Myanmar alphabet

A => 65
Z => 90
a => 97
z => 122
က => 4096
အ => 4129

################################################ 

[65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122]

list(range(65, 91)) + list(range(97, 123))


[65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 4096, 4097, 4098, 4099, 4100, 4101, 4102, 4103, 4104, 4105, 4106, 4107, 4108, 4109, 4110, 4111, 4112, 4113, 4114, 4115, 4116, 4117, 4118, 4119, 4120, 4121, 4122, 4123, 4124, 4125, 4126, 4127, 4128, 4129]

list(range(65, 91)) + list(range(97, 123)) + list(range(4096, 4130))

################################################ 

def is_upper(c):
    return ord(c) in list(range(65, 91))


def is_lower(c):
    return ord(c) in list(range(97, 123))


def is_english_alphabet(c):
    return ord(c) in list(range(65, 91)) + list(range(97, 123))
    

def is_myn_alphabet(c):
    return ord(c) in list(range(4096, 4130)) 
    

def is_eng_myn_alphabet(c):
    return ord(c) in list(range(65, 91)) + list(range(97, 123)) + list(range(4096, 4130)) 


s = "I go to school က No.123.အ"

for c in s:
    if is_eng_myn_alphabet(c):
        print(f"{c} is an alphabet.")
        
################################################

7. palindrome (နောက်ပြန်ဖတ်လျှင်လည်း ထပ်တူညီသော စကား) eg. madam ( str == str[::-1] )

"abcbA" == "Abcba"
lower case chr => "abcba" == "abcba"
upper case chr => "ABCBA" == "ABCBA"


def is_palindrome(s):
    return s == s[::-1]
    
    
print(is_palindrome("madam"))


def is_palindrome(s):
    l = s.lower()
    return l == l[::-1]
    

print(is_palindrome("Madam"))

################################################

8. greater number (ပိုကြီးတဲ့ နံပါတ်) ( n1 > n2 ) 

n1  n2
2   1   => greater number = n1
1   2   => greater number = n2
2   2   => greater number = n1, n2

################################################


def greater_number(n1, n2):
    if n1 > n2:
        return n1

    if n2 > n1:
        return n2

    if n1 == n2:
        return n2


################################################


def greater_number(n1, n2):
    if n1 > n2:
        return n1
    else:
        return n2
        

print(greater_number(2, 1))
print(greater_number(1, 2))
print(greater_number(2, 2))

################################################

n1  n2
1   2   => greater number = n2
2   1   => greater number = n1
2   2   => greater number = n1


def greater_number(n1, n2):
    if n2 > n1:
        return n2
    else:
        return n1
        

################################################

9. less number ( n1 < n2 )

n1  n2
1   2   => less number = n1
2   1   => less number = n2
1   1   => less number = n1, n2

################################################


def less_number(n1, n2):
    if n1 < n2:
        return n1
    else:
        return n2


print(less_number(1, 2))
print(less_number(2, 1))
print(less_number(1, 1))

################################################

11. summation

summation of 5 = 1 + 2 + 3 + 4 + 5 = 15
summation of 6 = 1 + 2 + 3 + 4 + 5 + 6 = 21
summation of 7 = 1 + 2 + 3 + 4 + 5 + 6 + 7 = 28

################################################ 

summation of 5 = 1 to 5  => stop = 5 + 1
summation of 6 = 1 to 6  => stop = 6 + 1
summation of 7 = 1 to 7  => stop = 7 + 1
summation of n = 1 to n  => stop = n + 1

ans = 0
ans += 1     =>  1
ans += 2     =>  3
ans += 3     =>  6
ans += 4     =>  10
ans += 5     =>  15

################################################ 


def summation(n):
    ans = 0
    for i in range(1, n+1):
        ans += i
    return ans


print(summation(10))

################################################

ans = 1 
ans += 2     =>  3
ans += 3     =>  6
ans += 4     =>  10
ans += 5     =>  15


def summation(n):
    ans = 1
    for i in range(2, n+1):
        ans += i
    return ans

   
################################################

12. factorial(n) (မြှောက်ဖော်ကိန်း)
    => factorial of 5 = 1 * 2 * 3 * 4 * 5 = 120
    
ans = 1
ans *= 1     =>  1
ans *= 2     =>  2
ans *= 3     =>  6
ans *= 4     =>  24
ans *= 5     =>  120

################################################


def factorial(n):
    ans = 1
    for i in range(1, n+1):
        ans *= i
    return ans


print(factorial(5))

################################################

ans = 1    
ans *= 2     =>  2
ans *= 3     =>  6
ans *= 4     =>  24
ans *= 5     =>  120


def factorial(n):
    ans = 1
    for i in range(2, n+1):
        ans *= i
    return ans
    
    
################################################

13. reverse_string(s) (string ကိုနောက်ကစပြီး ပြောင်းပြန်ရေးခြင်း။) ( [::-1] )


def reverse_string(s):
    return s[::-1]


x = "I go to school."
r = reverse_string(x)
print(x)
print(r)

################################################

14. count_vowels(s) (စာလုံးထဲက a, e, i, o, u ရေတွက်ခြင်း။)

x = "I go to school."

t = 0
t += 1   I
t += 1   0
t += 1   0
t += 1   0
t += 1   0

t => 5


def count_vowels(s):
    t = 0
    for c in s:
        if c in "aeiouAEIOU":
            t += 1
    return t


x = "I go to school."
print(count_vowels(x))

################################################

15. count_vowels(s) (စာလုံးထဲက a, e, i, o, u ဘယ်နှစ်လုံးရှိလဲရေတွက်ခြင်း။)

add item to dict   => {'I': 1, 'o': 1}
d["I"] = 1
d["o"] = 1

update dict value  => {'I': 1, 'o': 2}
d["o"] += 1


def count_vowels(s):
    d = {}
    for c in s:
        if c in "aeiouAEIOU": 
            if c not in d.keys():
                d[c] = 1
            else:
                d[c] += 1
    return d


x = "I go to school."
print(count_vowels(x))

################################################

{}
I  =>  d["I"] = 1   =>  {'I': 1}
0  =>  d["o"] = 1   =>  {'I': 1, 'o': 1} 
0  =>  d["o"] += 1   =>  {'I': 1, 'o': 2} 
0  =>  d["o"] += 1   =>  {'I': 1, 'o': 3} 
0  =>  d["o"] += 1   =>  {'I': 1, 'o': 4} 

################################################

x = "I go to school. I like apple."

{
    'I': 2, 
    'o': 4, 
    'i': 1, 
    'e': 2, 
    'a': 1
    
    }
    

{
    'i': 3, 
    'o': 4, 
    'e': 2, 
    'a': 1
    
    }
    
{
    'I': 3, 
    'O': 4, 
    'E': 2, 
    'A': 1
    
    }
    
################################################

{'i': 3, 'o': 4, 'e': 2, 'a': 1}


def count_vowels(s):
    d = {}
    for c in s:  # i
        l = c.lower() # i
        if l in "aeiou": 
            if l not in d.keys():
                d[l] = 1
            else:
                d[l] += 1
    return d


x = "I go to school. I like apple."
print(count_vowels(x))

################################################

{'I': 3, 'O': 4, 'E': 2, 'A': 1}


def count_vowels(s):
    d = {}
    for c in s:  # i
        u = c.upper() # i
        if u in "AEIOU":
            if u not in d.keys():
                d[u] = 1
            else:
                d[u] += 1
    return d


x = "I go to school. I like apple."
print(count_vowels(x))

################################################

16. sum_of_list(lst) (စာရင်းထဲက နံပါတ်တွေကို ပေါင်းခြင်း။)


def sum_of_list(lst):
    t = 0
    for n in lst:
        t += n
    return t


x = [100, 1000, 2000]
print(sum_of_list(x))

################################################

17. max(lst) (အများဆုံးတန်ဖိုး ရှာခြင်း။)

x = [100, 1000, 2000, 1500, 3000]

m = 100

100  1000    m = 1000
1000 2000    m = 2000
2000 1500    m = 2000
2000 3000    m = 3000

m = 3000

################################################


def greater_number(n1, n2):
    if n1 > n2:
        return n1
    else:
        return n2


def max(lst):
    m = lst[0]  
    for n in lst[1:]:
        m = greater_number(m, n) 
    return m


x = [100, 1000, 2000, 1500, 3000]
print(max(x))
        

################################################    

18. min(lst) (အနည်းဆုံးတန်ဖိုး ရှာခြင်း။)


def min(lst):
    m = lst[0] 
    for n in lst[1:]:
        m = less_number(m, n)
    return m


################################################


19. find_max_min(lst) အများဆုံးနဲ့ အနည်းဆုံးတန်ဖိုး ရှာခြင်း။ 

(3000, 100)


def find_max_min(lst):
    return (max(lst), min(lst))


def find_max_min(lst):
    return max(lst), min(lst)
    
    
################################################

[3000, 100]


def find_max_min(lst):
    return [max(lst), min(lst)]
    
    
################################################

{'max': 3000, 'min': 100}


def find_max_min(lst):
    return {"max": max(lst), "min": min(lst)}


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
    m = lst[0]  # 100
    for n in lst[1:]: # [1000, 2000, 1500, 3000]
        m = greater_number(m, n)
    return m


def min(lst):
    m = lst[0]  # 100
    for n in lst[1:]: # [1000, 2000, 1500, 3000]
        m = less_number(m, n)
    return m


def find_max_min(lst):
    return max(lst), min(lst)


x = [100, 1000, 2000, 1500, 3000]
ans = find_max_min(x)
print(ans)

################################################


def find_max_min(lst):
    max = lst[0]  
    for n in lst[1:]:  
        if max > n:
            pass
        else:
            max = n

    min = lst[0]  
    for n in lst[1:]: 
        if min < n:
            pass
        else:
            min = n
    return max, min


################################################

21. Uppercase and Lowercase

Uppercase (a to A)  (97 to 65)

1. ord
2. - 32
3. chr

chr(ord(c) - 32)

################################################ 


def upper(s):
    ans = ""
    for c in s:   # "g"
        if c in "abcdefghijklmnopqrstuvwxyz":
            ans += chr(ord(c) - 32)
        else:
            ans += c
    return ans
    
    
################################################ 
  
Lowercase (A  to a)  (65 to 97)

1. ord
2. + 32
3. chr

chr(ord(c) + 32)

################################################ 


def lower(s):
    ans = ""
    for c in s:  
        if c in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
            ans += chr(ord(c) + 32)
        else:
            ans += c
    return ans


x = "I go to school."
print(lower(x))

################################################ 

20. linear search


def linear_search(lst, element):
    for e in lst:
        if e == element:
            return True
    return False


################################################ 

atoms = ['Aluminium', 'Antimony', 'Argon', 'Arsenic', 'Astatine', 'Barium', 'Barium', 'Beryllium', 'Boron', 'Bromine', 'Cadmium', 'Calcium', 'Carbon', 'Cerium', 'Cesium', 'Chlorine', 'Chromium', 'Cobalt', 'Copper', 'Dysprosium', 'Erbium', 'Europium', 'Fluorine', 'Francium', 'Gadolinium', 'Gallium', 'Germanium', 'Gold', 'Hafnium', 'Helium', 'Holmium', 'Hydrogen', 'Indium', 'Iodine', 'Iron', 'Krypton', 'Lanthanum', 'Lithium', 'Lutetium', 'Magnesium', 'Manganese', 'ManganeseGermanium', 'Mercury', 'Molybdenum', 'Neodymium', 'Neon', 'Nickel', 'Niobium', 'Nitrogen', 'Oxygen', 'Palladium', 'Phosphorus', 'Platinum', 'Potassium', 'Praseodymium', 'Promethium', 'Radium', 'Radon', 'Rhodium', 'Rubidium', 'Ruthenium', 'Samarium', 'Scandium', 'Selenium', 'Silicon', 'Silver', 'Sodium', 'Strontium', 'Strontium', 'Sulfur', 'Tantalum', 'Technetium', 'Tellurium', 'Terbium', 'Thulium', 'Tin', 'Titanium', 'Tungsten', 'Vanadium', 'Xenon', 'Ytterbium', 'Yttrium', 'Zinc', 'Zirconium']

################################################ 

22. Binary Search

Search
1. e == m
2. e > m   =>  right
3. e < m   =>  left

################################################ 

empty => Stop 

any value => Search

################################################ 

x = [10, 40, 50, 70, 90, 110, 120]

total = len(x)          =>  7
m = t // 2              =>  3
middle = x[m]           =>  70

right = [m+1:end]       =>  [90, 110, 120]
left = [start:m]        =>  [10, 40, 50]

################################################   


def binary_search(collection, element):

    while len(collection) > 0:
        t = len(collection)                # 7        3        1
        m = t // 2                         # 3        1        0
        middle = collection[m]             # 70       40       10

        if element == middle:
            return True
        elif element > middle:
            collection = collection[m+1:]     # r
        elif element < middle:
            collection = collection[:m]       # l     [10, 40, 50]   [10]    []

    return False
    
 
################################################

10. leap year (ရက်ထပ်နှစ်) (and, or)
    1. divisible by 400 ( eg. 2000, 1600 )    ( y % 400 == 0 )
    2. divisible by 4 + not divisible by 100   ( y % 4 == 0 and y % 100 != 0 )
    
    - Rule.1 or Rule.2

################################################

1. Julian


def leap_year(y):
    return y % 4 == 0
    
    
################################################

2. Gregorian


def leap_year(y):
    return ( y % 400 == 0 ) or ( y % 4 == 0 and y % 100 != 0 )
    

################################################################################################

"""

