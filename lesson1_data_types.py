
"""
1. Mindset
2. Limit
3. Behaviour
4. Ethics
5. Imaginary
6. Step
7. Simple
8. Imperative paradigm(procedure, object), Declarative paradigm (functional)
9. Procedural programming (procedure)

################################################

1. time
2. select
3. loop
4. function

################################################

1. data types
2. control flow
3. function

################################################

1. time
   - top to b
   - left to right
   - parenthesis 

################################################

p0  computer open
p1  song open
p2  song close
p3  computer close

################################################

012123

p0 p1
p2 p1
p2 p3

p3(p2(p1(p2(p1(p0)))))

################################################

p3(p0) p1(p0)
p2 p1
p2 p3

03012123

################################################

abc  ( data types 15 )

apple ( type casting, ... )

practice 

grammer ( syntax )

################################################

1. Data types
  - str
    - character (chr)
    - character string ( str )
    - documentation string ( doc )

  - number
    - int       --->   integer 
    - float     --->   decimal/floating-point number
    - complex   --->   complex number

  - 8
    - normal list  2   (list, tuple)
    - unique list  2   (set, frozenset)
    - binary list  2   (bytearray, bytes)
    - number list  1   (range)(generator object)
    - item list    1   (dict)

  - condition           bool
    
  - memoryview

  - None Type           None

################################################

range

1, 2, 3, 4, ..., 100
start = 1
stop = 101
step = 1

################################################

odd 50  = 1, 3, 5, to 99
start = 1
stop = 100
step = 2

even 50 = 2, 4, 6, to 100
start = 2
stop = 101
step = 2

reversed odd 50 = 99, 97, 95 to 1
start = 99
stop = 0
step = -2

reversed even 50 = 100, 98, 96, 94 to 2
start = 100
stop = 1
step = -2

################################################

1. Data type 

################################################

1.1. built-in data types ( 15)

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
15. NoneType(None)

################################################

1. mutable, immutable
   - list, set, bytearray, dict
   
2. unordered, ordered (indexing)
   - set, frozen set, dict
   
################################################

1.2.Creating built-in data types with notations

notations
1. quotes
2. .
3. j
4. []
5. (), (comma)
6. {}  (set)
7. b
8. {} (dict)

Notation is value.
1. 1
2. True, False
3. None

No notation 
1. frozenset()
2. bytearray()
3. range()
4. memoryview()

################################################

1.3.Creating built-in data types with name ( type casting )

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

################################################

15. NoneType      <---   only notation value None

################################################

1.4.Python has five rules for naming identifiers(labels).

(one, alpha, number, o, r)

1. An identifier must contain at least one character.
2. The first character of an identifier must be an alphabet or the underscore.
3. The remaining characters may be alphabets, underscores, numbers.
4. Qther characters are not permitted.
5. A reserved keyword cannot be used as an identifier.
6. meaningful

################################################

"""

# 1.5.Checking data type

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
1e6
1e-6
0.000001


["apple", "banana", "orange"]
[]
list()

()
tuple()
("Mg Mg", 20, 5.5)

range(0, 10)
range(2, 101, 2)

{"name": "Mg Mg", "age": 20, "height": 5.5}

{
    "name": "Mg Mg",
    "age": 20,
    "height": 5.5
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
{1, }

(1 + 2) * 3
(1)
("apple")

(1,)
("apple",)
1, 2, 3
1,

"1000"
str(1000)

1000
int("1000")

1000.0
float(1000)
float("1000")
2.6
1 + 1.6

float(1) + 1.6
1.0 + 1.6

################################################

# 1.6.boolean value exercise

0
0.0
0j

1
1000
12.5
0.1
0.000001
1e6

{}  # empty dict
set()  # empty set
[]  # empty list
()  # empty tuple
frozenset()  # empty frozenset
""  # empty str
''
""""""
''''''
b""
bytearray(b"")

################################################


"""






























