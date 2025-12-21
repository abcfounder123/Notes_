
"""

Day.8

Python has five rules for naming identifiers(labels).

(one, alpha, number, o, r)

1. An identifier must contain at least one character.
2. The first character of an identifier must be an alphabet or the underscore.
3. The remaining characters may be alphabets, underscores, numbers.
4. Other characters are not permitted.
5. A reserved keyword cannot be used as an identifier.
6. meaningful

################################################

one, alpha, number, o, r

1. one  (at least one character)
2. alpha (alphabet or underscroll)
3. number 
4. o     (other character)
5. r     (reserved keyword name) 35

################################################

import keyword

print(keyword.kwlist)
print(len(keyword.kwlist))

################################################

kwlist = ['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']

35

SyntaxError: invalid syntax

################################################

Type casting (21) (14 + c o 2 8 16 r e)

1. str()

2. int()
3. float()
4. complex()

5. list()
6. tuple()
7. set()
8. frozenst()
9. bytearray()
10. bytes()
11. range()
12. dict()

13. bool()

14. memoryview()

15. chr -> str   eg. chr(65)    =>   'A'
16. ord -> int   eg. ord('A')   =>    65
17. bin -> str  "0b0011"
18. oct -> str  "0o75"
19. hex -> str  "0xa"
20. repr -> str
21. eval -> program output(15 +)

################################################

c o 2 8 16 r e

ordinal number ( first, second )

Unicode

A  =>  65
B  =>  66
a  =>  97
b  =>  98
က =>  4096
ခ  =>  4097
   
################################################

decimal number to str
binary number         ->  bin()
octal number          ->  oct()
hexadecimal number    ->  hex()

################################################

r  (Representation string )   ->   repr()

################################################

e  (Evaluation)              ->   eval()

################################################################################################

1. Explicit type casting (list to set)

x = ["apple", "orange", "apple", "banana", "orange", "apple"]
ans = set(x)
print(ans)

################################################

2. Explicit type casting (range to list)

x = range(1000)
ans = list(x)
print(ans)

ans = list(range(1, 1001))
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

Type casting
- Explicit type casting (direct)   (21)
- Implicit type casting (indirect) (2)

################################################

Explicit type casting

int(truncate)
1 + int(1.5)
1 + 1              ->   2 

int(round)
1 + round(1.5) 
1 + 2              ->   3

float
float(1) + 1.5
1.0 + 1.5          ->   2.5

################################################

Implicit(float, bool)

1
float  ->  1.0
bool   ->  True

################################################

bool (empty, any)

Empty    ->   False
0
0.0
0j
""
[]
()
{}
set()

Any      ->   True
1
10
1000000
1.0
0.000001
"apple"
" "
["apple", "banana"]
(1, 2)
{"name": "Mg Mg"}
set(1, 2, 3)       

################################################################################################

"""


