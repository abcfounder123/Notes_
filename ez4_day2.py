
"""

1. Procedure              4
2. Sequence               3
3. Data types            15
4. Creating by names     14
5. Creating by symbols   11
6. range                  3

################################################

Procedural programming
1. sequence
2. selection
3. looping
4. function (Procedure)

################################################

1. sequence
   - top
   - left
   - parenthesis first

p1
p2 p3(p4)
p5(p6(p7))
p8(p11) p9 p10(p12)

1 243 765 11 8 9 12 10

p1
p2 p4(p3)
p7(p6(p5))
p9(p8) p10 p12(p11)

################################################

data types 15

1. Character (chr)
2. Character string (str)
3. Documentation string (doc)

1. integer (int)
2. floating-point number (float)
3. complex number  (complex)

1. normal list (list, tuple)
2. unique list (set, frozenset)
3. binary list (bytearray, bytes)
7. number list (range)
8. item list   (dict) dictionary

1. Boolean data type (bool)

################################################

Data types 15

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
15. NoneType

################################################

Creating by names (14)

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

################################################

Creating by symbols (11)

1. quotes
2. .
3. j
4. []
5. ()
6. {}
7. b
8. {}

Value is symbol.
1. integer
2. boolean
3. NoneType


Name only
1. frozenset()
2. bytearray()
3. range()
4. memoryview()

################################################################################################

"""

# Checking data type

b''
b'apple'

bytearray(b'')
bytearray(b'apple')

memoryview(b"apple")
# <memory at 0x1005f2080>

''
' '
'1000'
"1000"
'''1000'''
"""1000"""

0j
3 + 2j
1j

0
-1
+1
1_000
1_000_000
1_000_000_000
1000000000

0.0
-1.0
+1.0
1.0
1000.0
.01
100.
0.
1_000_000.0
1e6                    # e6 = 1000000
1e-6                   # e-6 = 1/1000000 = 0.000001
0.000001
1.234e-9                   # 0.000000001234
1e9
1e12
1000000000000.0

["apple", "banana", "orange"]
[]
list()

()
tuple()
("Mg Mg", 20, 5.5)


range(0, 10, 1)
range(0, 10)
range(10)
range(2, 101, 2)

{"name": "Mg Mg", "age": 20, "height": 5.5}

{
    "name": "Mg Mg",
    "age": 20,
    "height": 5.5,
    "marks": [60, 70, 80]
}

{}

{"apple", "banana", "orange"}
set()
frozenset()
frozenset({'apple', 'orange', 'banana'})  # frozenset
frozenset(['apple', 'orange', 'banana'])
frozenset(('apple', 'orange', 'banana'))

1000
0
int()

True
False
bool()

None

{}
dict()
set()
{1, }


"1000"
str(1000)

1000
int("1000")

1000.0
float(1000)
float("1000")




