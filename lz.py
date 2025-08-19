"""

Lazy class ဆိုတာက အိမ်စာမပါပဲ တစ်ခါတည်း အလွတ်နီးပါးရအောင် သင်ပေးတဲ့ အတန်းပါ။

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

1. Sequence(time)
2. Selection
3. Iteration 
4. Function

################################################

1. data types
2. control flow (sequence, selection, iteration)
3. function (procedure)

################################################

1. time (sequence)
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

1. indexing  ( +, - )

   - left  (positive index) (0) 
   - right (negative index) (1)
   
   - f3  (richest_3 = countries[2] )
   - l3  (p3 = countries[-3] )
   
   - range (-t to t-1)
   - hard = total - abs(easy) 
      
   - middle_country
     - total = odd, m = t // 2
     - total = even, rm = t // 2, lm = rm - 1

################################################

middle_country 

1 2 3 4 5 6 7     
a b c d e f  
0 1 2 3 4 5 6   left   +      
7 6 5 4 3 2 1   right  -     

total = odd, middle = 1
m = t // 2

total = even, middle = 2
rm = t // 2
lm = rm - 1 
   
################################################   
   
2. slicing
   - collection (total)
   - positive and negative for each item
   - result, start:stop:step
   - blank ---> [:4], [-4:]
   - dataset
     - first five, last five
     - inverse

################################################

basic

a b c d e f g    x
0 1 2 3 4 5 6   (+)
7 6 5 4 3 2 1   (-)

bcde -> start = b, stop = f
1234 -> x[1:5:1]
6543 -> x[-6:-2:1]

edcb -> e, a, -1
4321 -> x[4:0:-1]
3456 -> x[-3:-7:-1]

################################################

blank

first 4  
  - 0, 1, 2, 3  
  - [0:4:1]
  - [0:4]
  - [:4]
  
last 4
  - -4, -3, -2, -1
  - [-4:0:1]
  - [-4:0]
  - [-4:]
  
inverse
[::-1]

################################################

# reverse engineering of middle 11 inverse

# [t // 2 - 5 : t // 2 + 6][::-1]
# [::-1] inverse
# m = t // 2
# s = m - 5
# stop = m + 6

################################################  
   
countries = list(range(1, 201))
print(countries)

# first 5, last 5 (easy index)
print(countries[:5])   #  0, 1, 2, 3, 4        #   0:5:1
print(countries[-5:])  # -5, -4, -3, -2, -1    #  -5:0:1

################################################ 

# first 5, last 5 (hard index)
# -200, -199, -198, -197, -196  -> -200:-195:1  -> -200:-195  -> :-195
print(countries[:-195]) 

# 195, 196, 197, 198, 199   ->  195:200:1  ->  195:
print(countries[195:])

################################################ 

- poorest five from richest dataset 
  -> -1, -2, -3, -4, -5        ->   -1:-6:-1     ->   :-6:-1     (easy index)
  -> 199, 198, 197, 196, 195   ->   199:194:-1   ->   :194:-1    (hard index)

################################################ 

richest dataset to  poorest dataset
:::   ->   0:200:1     ->   0, 1, 1, 3, ..., 199
::-1  ->  -1:-201:-1   ->   -1, -1, -3, ..., -200

################################################ 

################################################

1. Operand
   >> left operand
   >> right operand
   
     1    +    2
    /     |     \
  left    |     right
       operator
(addinional operation) 

1 + 2 (binary plus)
+1 (unary plus)

add()
pos()

sub()
neg()

################################################

2. Operator                 
   -  unary operator   --->   right operand                     
      1. unary plus    --->   + 1
      2. unary minus   --->   - 1
      3. logical NOT   --->   not True
      4. bitwise NOT   --->   ~ 5
        
   -  binary operator  --->   left operand, right operand
  
   -  Ternary operator --->   middle operand 

################################################

3. Precedence
   >> parenthesis        --->   ( )
   
   >> Arithmetic operator ( e, u, * /, + - )
   1. exponentiation     --->   **  
   2. unary +, -         --->   +1, -1
   3. multiplication     --->   *
      division   
         division           --->   /
         floor division     --->   //  (ceiling)      ( 2.5  ---> 2, 3 )
         modulus            --->   %
   4. addition           --->   +
      substraction       --->   -

      
(1 + 2) * 3   
3 * 3
9

1 + (2 * 3)
1 * 6
7

################################################

4. Associativity
   >> left sided bind
   >> right sided bind ( **, = )
   
2 ** 3 ** 4
8 ** 4
4096

2 ** 3 ** 4
2 ** 81
2417851639229258349412352
   
x = y = 1

################################################

3. Precedence
>> parenthesis        --->   ( )
   
Arithmetic operators (Perform mathematical operations)( e, u, * /, + - )(9)
1. exponentiation     --->   **  
2. unary +, -         --->   +1, -1, ~
3. multiplication     --->   *
   division   
   division           --->   /
   floor division     --->   //
   modulus            --->   %
4. addition           --->   +
   substraction       --->   -
   
Bitwise Operators (Operate on bits)(shift, and, or2, not)(6)
5. Left shift         --->   <<
   Right shift        --->   >>

6. Bitwise AND        --->   &

7. Bitwise XOR        --->   ^

8. Bitwise OR         --->   |

2. Bitwise NOT        --->   ~

9. 
Comparison Operators (Compare values)(6)
   Equal to           --->   ==              
   Not equal to       --->   !=
   Greater than       --->   >
   Less than          --->   <
   Greater than or equal to   --->   >=
   Less than or equal to      --->   <=

Identity Operators (Compare memory locations)
   Identical objects          --->   is
   Not identical objects      --->   is not

Membership Operators (Test for membership in sequences)
   Present in the sequence    --->   in
   Not present in the sequence --->   not in

Logical Operators (Combine conditional statements)
10.Logical NOT        --->   not
11.Logical AND        --->   and
12.Logical OR         --->   or

13. Ternary Operator
14.Assignment Operators (Assign values to variables) (13)
    Simple assignment --->   =
    Add and assign    --->   +=
15. Walrus Operator   --->   :=

################################################

5. Notes

e, 
u,   -, +, ~
* /, 
+ -                         

shift                         bitwise
and       
xor
or

C                           
not                           logical
and
or

t                             
assignment                    =, **=, *=, /=, //=, %=, +=, -=, <<=, >>=, &=, ^=,|=   
walrus                        :=

################################################

6. Built-in Operators ( 7 )

1. Arithmetic Operators        (9)
2. Bitwise Operators           (6)
3. Comparison Operators        (6)
4. Identity Operators          (2)
5. Membership Operators        (2)
6. Logical Operators           (3)
7. Assignment Operators       (13)
   Walrus                      (1)
                            
   ternary                      1  
   
                               43
                              
################################################
################################################

1. Arithmetic operators in programming

Seconds to Seconds, Minutes, Hours and days ( 90350 )

1hour = 3600 seconds
1day = 24 hours 
1min = 60 seconds

90350 sec // 3600 = 25      h
90350 sec % 3600 = 350      sec

25 h // 24 = 1   day
25 h %  24 = 1   h

350 sec // 60 = 5    min
350 sec % 60 = 50    sec

             90350       = 1 day 1:5:50
          /        |
        25h       350sec
      /   |      /   |
     1d   1h    5min 50sec
     
################################################

2. basic input, output

input 
- receive string value
- prompt letter

print
- print string value
- commma

################################################

3. Three components of programming

noise cancelling (zoom)
input   --->  mic (35db to 250db)
process --->  70db to 100db
output  --->  speaker

day hour minute
input   --->  keyboard (str value of seconds)
process --->  str to int, day, hour, minute
output  --->  standard output file

################################################

sec = int(input("Enter seconds:"))  # 90350

h = sec // 3600                     # 25
sm = sec % 3600                     # 350

day = h // 24                       # 1 d
hour = h % 24                       # 1 h

min = sm // 60                      # 5 min
sec = sm % 60                       # 50 sec

print(day, "day", hour, "hour", min, "minute", sec, "second")

################################################

4. Normal statements

fail statement
pass statement

################################################

5. Conditional statements
  
fail condition:  fail statement
pass condition:  pass statement

################################################

6. program flow
- ability to check the flow of programs

################################################

7. control flow 
- ability to control the flow of programs

################################################

8. program quality (13, 7, 6)

mark = int(input("Enter marks:"))  
exam_pass = mark >= 50  
fail = mark < 50    
if exam_pass:print("pass")
if fail:print("fail")

mark = int(input("Enter marks:")) 
print("Exam result")
if mark >= 50:print("pass")
if mark < 50:print("fail")

mark = int(input("Enter marks:"))
print("Exam result")
if mark >= 50:print("pass")
else:print("fail")

################################################

9. Selection(if, else)

fail or pass 
sleep or walk

################################################





"""