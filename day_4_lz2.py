"""

day.4

################################################

1. Range

"abcdefg"

range of index
-> -7, -6, -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6 
-> -7 to 6
-> -t to t-1

t = 100
-> -100 to 99

IndexError: string index out of range
IndexError: list index out of range

################################################################################################

2. Dimensions of data

1D, 2D, 3D, 4D

.           .
.
.   .   .   .

3 + 2j

3, 2, 3

No   Name     Age   Marks

1    Mg Mg    20    (70, 74, 80)
2    Ma Ma    21    ([70, 68, 75], [74, 75, 76], [80, 75, 90])
3    Hla Hla  19

column = X
row    = Y

Hla Hla (1, 2)
74      (3, 0, 1) 
Ma Ma' Myanmar marks' final marks  (X 3, Y 1, Z 0, I -1)


x = (["apple", "banana"], "orange")  # (list, str), [str, str]
print(x[0][1][:3])
print(x[1][1:4])

################################################################################################ 

3. Reverse engineering of middle 11 reverse

middle 11 inverse
=> [t // 2 - 5 : t // 2 + 6][::-1]
=> [t // 2 - 5 : t // 2 + 6 : 1][start:end:-1]
=> [start:stop]reverse
=> middle 11 inverse

1. m = t // 2
2. start = m - 5
3. stop = m + 6 
4. [::-1] <-- reverse

################################################

middle 21 inverse
=> [t // 2 - 10 : t // 2 + 11][::-1]

middle n inverse
=> n = 11
=> h = n // 2
=> [t // 2 - h : t // 2 + (h+1)][::-1]

middle n inverse
=> n = 11
=> h = n // 2
=> [m - h : m + h][::-1]

################################################

d = "whfihwvhkjvnakjnvkvdwiviovwvjhvbdjhfjehfhehfijheffhvjh"

n = int(input("Enter n: "))
h = n // 2
m = len(d) // 2
ans = d[m - h:m + h+1][::-1]
print(ans)

################################################

if total is even,

middle 11 -> (5, 6)
middle n  -> (half, half+1)

################################################

if total is odd,

middle 10 -> (5, 5)
middle n  -> (half, half)

1 2 3 4 5 6 7 8 9 10 (11)

################################################################################################

4. ordered collections  ( indexing, slicing )

houses = [1, 2, 3, 4, 5, .., 100] 

house 100

-->  Mandalay
-->  Yangoon

-->  base memory address = 23551298600
-->  base + (i + 1) * 10 =  ?

################################################

positive index 
=> houses[9]                 
=> base + (i + 1) * 10 = 23551298700     <= first 10


negative index
=> houses[-91]
=> total - easy = 100 - 91 = 9
=> houses[9]
=> base + (i + 1) * 10 = 23551298700      <= first 10

################################################

i = 9
n = i + 1 = 10
size = 28
base = 23551298600
h10  = base + (n * size) = 23551298880

################################################################################################

5. unordered collections

10000
{1, 2, 3, 4, 5, ..,  100}

f1 = 100
f2 = 10001
f3 = 2000
f100 = 1

################################################################################################

1. Operand
   >> left operand
   >> right operand
   
     1    +    2
    /     |     \
  left    |     right
       operator
(addinional operation) 

binary minus (subtraction)(addition)
unary minus  (negative)(positive)
+1, -1, 
1 + 2, 1 - 2
   
################################################

2. Operator  

   -  one (unary)
   -  two (binary)
   -  three (ternary)
               
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
   
   >> Arithmetic operators ( e, u, * /, + - )
   1. exponentiation     --->   **  
   2. unary +, -         --->   +1, -1
   3. multiplication     --->   *
      division   
         division           --->   /
         floor division     --->   //  (ceiling)      ( 3.5  ---> 3, 4 )
         modulus            --->   %
   4. addition           --->   +
      substraction       --->   -

      

+, *
1 + 2 * 3
3 * 3
9

*, +
1 + 2 * 3 
1 + 6
7

################################################

4. Associativity
   >> left sided bind
   >> right sided bind ( **, = )
   
left-sided bind
2 ** 3 ** 4
8 ** 4
4096
  
right-sided bind
2 ** 3 ** 4
2 ** 81
2417851639229258349412352

x = y = 1

################################################################################################




"""