"""

Precedence(15)

1. e           exponent                                           (right)
2. u           unary plus, unary minus, bitwise not (~)
3. * / // %    multiplication, division, floor division, modulus  (left)
4. + -         addition, subtraction                              (left)

1   =
7   +=, 
5   <<=, >>=, &=

5. shift       left shift, right shift  ( <<, >> )
6. AND         Bitwise AND ( & )
7. XOR         Bitwise exclusive OR  ( ^ )
8. OR          Bitwise OR ( | )

9. C           Comparison operators(6), Membership operators(2), Identity operators(2) 
10. NOT        Logical NOT
11. AND        Logical AND
12. OR         Logical OR
13. t          Ternary operator
14. assignment
15. walrul

################################################

Built-in operators (43)

1. Arithmetics operators -   9
2. Bitwise Operators     -   6     0, 1
3. Comparison operators  -   6
4. Identity operators    -   2
5. Membership operators  -   2
6. Logical operators     -   3     T, F
7. Assignment operator   -  13

8. Ternary operator      -   1
9. Walrus                -   1

Total                    -  43

################################################

Identity Operators(is, is not)(id/ memory address) (same object)

x = []   # new list  4345609472
y = []               4345609856

x == y       --->  True
x is y       --->  False
x is not y   --->  True

################################################

Membership Operators(in, not in)

fruits = ["apple", "banana", "orange"]

x = "mangoes"

x in fruits       --->  False
x not in fruits   --->  True

################################################

Logical operators (not, and, or) (logic value => True, False)

not True        --->  False
True and True   --->  True
True or True    --->  True

################################################

13. t            --->   trnary operator, conditional operator, if-else operator
14. assignment   --->   assignment operator
15. walrus       --->   walrus operator

#####################

13. trnary operator, conditional operator, if-else operator

mark = 30

"pass" if mark >= 40 else "fail"   ---> "fail"

################################################

14. Assignment operator (13)(right-sided bind)

x = 1   --->   x is assigned memory address of int object

#####################

1. simple assignment

x = 1

#####################

2. add and assign

x = x + 1     +, = (add and assign)(same as x = 2)

x = 1
x += 1        +, = (add and assign)(same as x = 2)

#####################

simple assignment - 1

Arithmetics       - 7

Bitwise           - 5

Total             - 13

################################################

15. walrus operator ( := ) 

- assign and use

################################################################################################

Labels

C programming

x = 1

left operand  -> x, variable(value)(box, cup), 
right operand -> 1, value

################################################

1. variable(value)(box, cup)

int32 x;        bottle   (fixed data)(limited amount, size)  # 4345609472 (32)

x = 1           water
x = 5           juice

x = "apple"     (fixed data(water, juice))
x = 2 billions  (limited amount, size)

################################################

2. label, pointer, identifier

x = int()           # 4345609472 (28)  

x = 5  

x = 2 billions      

x = "sun"           # 00001111

################################################

3. objects, memory address and labels

x = []   # Mandalay
y = []   # Yangon

z = x
a = x

house -  2
label -  4

Mandalay  --->  x, z, a
Yangon    --->  y

################################################

4. Building a house

x = int()

design        -->  int
int()         -->  command to built
house object  -->  RAM (address)
label         -->  x

################################################

5. right-sided bind

z = y = x = 0   

house -  1
label -  3

################################################

6. Methods of built-in data types

str          81
int          74
float        59
complex      43
list         48
tuple        35
set          57
frozen       44
bytearray    90
bytes        78
range        35
dict         46
bool         74
memoryview   52
None         25

################################################

7. uppercase and lowercase

"a"      # 97
"A"      # 65

u = l - 32
l = u + 32

################################################

8. "a" to 'က'

"a"    97
'က'   4096

code_a + 3999 

################################################################################################

"""


