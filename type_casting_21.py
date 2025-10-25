"""
16. Type casting (2)
   
1. explicit
float(1) + 1.5 + float(2) + float(3) -> 7.5

2. implicit
1 + 1.5 + 2 + 3  -> float(1) + 1.5 + float(2) + float(3) -> 7.5

################################################

1. float(1) + 1.5 + float(2) + float(3)  ->  7.5     explicit  (float)
2. 1 + 1.5 + 2 + 3                       ->  7.5     implicit  (float)
3. 1 + int(1.5) + 2 + 3                  ->  7       explicit  (truncate)
4. 1 + round(1.5) + 2 + 3                ->  8       explicit  (round)

################################################

17. Explicit type casting (21) (14 + c o 2 8 16 r e)

1. str
2. int
3. float
4. complex
5. list
6. tuple
7. range
8. dict
9. set
10. frozenset
11. bool
12. bytes
13. bytearray
14. memoryview

15. chr -> str 
16. ord -> int
17. bin -> str  "0b0011"
18. oct -> str  "0o75"
19. hex -> str  "0xa"
20. repr -> str
21. eval -> program output(15 +)

c o 2 8 16 r e

1. character
2. ordinal number
3. binary number
4. octal number
5. hexadecimal number
6. representation string
7. evaluation

################################################

1. Explicit type casting (list to set)

x = ["apple", "orange", "apple", "banana", "orange", "apple"]
ans = set(x)
print(ans)

################################################

2. Explicit type casting (range to list)

x = range(1000)
ans = list(x)
print(ans)

################################################

3. Explicit type casting (dict to list)

x = {"name": "Mg Mg",
     "age": 20,
     "grade": "A",
     "pn No": "09123456"
     }

k = list(x.keys()) # ['name', 'age', 'grade', 'pn No']
print(k)

kk = list(x) # list(x.keys())
print(kk)

v = list(x.values()) # ['Mg Mg', 20, 'A', '09123456']
print(v)

i = list(x.items()) # [('name', 'Mg Mg'), ('age', 20), ('grade', 'A'), ('pn No', '09123456')]
print(i)

################################################

4. Explicit type casting (list to dict)

d = dict(i) # {'name': 'Mg Mg', 'age': 20, 'grade': 'A', 'pn No': '09123456'}
print(d)

################################################################################################

ordinal number, unicode number, character

65.   A
66.   B
4096. က

################################################

ord & chr

chr(65)  --> A     <- str
ord("A") --> 65    <- int

################################################

5. Explicit type casting (chr to ord)

x = "A"
ans = ord(x)
print(ans)

################################################

6. Explicit type casting (ord to chr)

chr(4096) --> က
x = 4096
ans = chr(x)
print(ans)

################################################

7. Explicit type casting (int to str value of binary number)
x = 2
ans = bin(x) # "0b10"
print(ans)

################################################

8. Explicit type casting (int to str value of octal number)

x = 8
ans = oct(x) # "0o10"
print(ans)

################################################

9. Explicit type casting (int to str value of hexadecimal number)

x = 16
ans = hex(x) # "0x10"
print(ans)

################################################

10. Explicit type casting (int to repr value)

x = 1 # int
ans = repr(x) # repr value -> "1"
print(ans, type(ans))

################################################

1 -> int() -> integer object (acts like a house) (n + 74)

################################################

10. Explicit type casting (str to program value)

x = "1 + 1.5"
ans = eval(x) # float
print(ans)

x = "1 + 1"
ans = eval(x) # int
print(ans)

################################################

11. Explicit type casting (str to program value) (Dynamic formla)

x = 1
y = 2
ans = 2 * x + y
print("ans =", ans)

>> ans = 4

x = 1
y = 2
ans = 2 * x + 2 * y
print("ans =", ans)

>> ans = 6

x = 1
y = 2
f = input("f = ") # "2 * x + y", "2 * x + 2 * y", "x + y"
ans = eval(f)
print("ans =", ans)

################################################################################################

"""

