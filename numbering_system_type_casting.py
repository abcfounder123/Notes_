"""
1. Numbering System -> int(value, base)

Base-1: Unary Numbering System

1. Base-2: Binary             4 bits ( 2 ** 4)
2. Base-3: Ternary (or Trinary)
3. Base-4: Quaternary
4. Base-5: Quinary
5. Base-6: Senary (or Hexary)
6. Base-7: Septenary
7. Base-8: Octal
8. Base-9: Nonary
9. Base-10: Decimal (or Denary)
10. Base-11: Undecimal      0 to 9 + a
11. Base-12: Duodecimal
12. Base-13: Tridecimal
13. Base-14: Tetradecimal
14. Base-15: Pentadecimal
15. Base-16: Hexadecimal
16. Base-17: Heptadecimal
17. Base-18: Octodecimal
18. Base-19: Nonadecimal
19. Base-20: Vigesimal
20. Base-21: Unvigesimal
21. Base-22: Duovigesimal
22. Base-23: Trivigesimal
23. Base-24: Tetravigesimal
24. Base-25: Pentavigesimal
25. Base-26: Hexavigesimal
26. Base-27: Heptavigesimal
27. Base-28: Octovigesimal
28. Base-29: Nonavigesimal
29. Base-30: Trigesimal
30. Base-31: Untrigesimal
31. Base-32: Duotrigesimal
32. Base-33: Tritrigesimal
33. Base-34: Tetratrigesimal
34. Base-35: Pentatrigesimal 
35. Base-36: hexatridecimal system ( 0 to z ) 10 + 26 (36) (0 to 35)

################################################

if base is 1(stick),

tttttttttt

################################################

if base is 10,

0 1 2 3 4 5 6 7 8 9

1
10       1  (10)
100      1 1 (10 10)
1000     1 1 1 (10 10 10)

################################################

if base is 8,

0 1 2 3 4 5 6 7

1
10      1 (8)
100     1 1 (8 8)
1000    1 1 1(8 8 8)

################################################

if base is 2,

0 1

1       1
10      1 (2)
100     1 1(2 2)
1000    1 1 1(2 2 2)

################################################

if base is 3, 

0 1 2
a b c

a      0
b      1
c      2
ba     1 (3)
bb     4
bc     5
ca     6

ba     1(3)
baa    1 1 (3 3)
baaa   1 1 1 (3 3 3)

################################################

if base is 100,

a b c . . . 
0 1 2

ba    1 (100)
baa   1 1(100 100)
baaa  1 1 1(100 100 100)

################################################

count by int()

formula = base ** (n-1)

int("1111", 2)
1111     1000 + 100 + 10 + 1 = 2**(n-1) + 2**(n-1) + 2**(n-1) + 2**(n-1) = 8 + 4 + 2 + 1 = 0 to 15  = 16

b = 10
int("1111", 10)
1111     1000 + 100 + 10 + 1 = 10**(n-1) + 2**(n-1) + 2**(n-1) + 2**(n-1) = 1000 + 100 + 10 + 1 = 1111

b = 8
int("1111", 8)
1111     1000 + 100 + 10 + 1 = 8**(n-1) + 8**(n-1) + 8**(n-1) + 8**(n-1) = 512 + 64 + 8 + 1 = 585

10000        1 1 1 1(2 2 2 2) 16
1000 0000    1 1 1 1 1 1 1 (2 2 2 2 2 2 2) = 128
1111 1111    128 + 64 + 32 + 16 + 8 + 4 + 2 + 1 = 255 = 0 to 255 = 256 = 2 ** 8

################################################

Base-1_000_000: Megary numbering system  ( Mega -> one million in Greek )

Base-1_000_000_000: Gigary numbering system ( Giga -> one billion in Greek )

################################################

notations /symbols for numbering system

0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 
31 32 33 34 35 ... 

0 1 2 3 4 5 6 7 8 9 a  b  c  d  e  f  g  h  i  j  k  l  m  n  o  p  q  r  s  t  u  
v  w  x  y  z  ...

################################################

Base-2: Binary   --->   0, 1    (3.0 V, 3.5 V)

0
1
10   <--- 10

1111  (16)

################################################

Base-3: Ternary   --->   0, 1, 2

0
1
2
10      2

################################################

Base-8: Octal   --->   0 1 2 3 4 5 6 7 

0
1
2
3
4
5
6
7
10  8

################################################

Base-10: decimal   --->   0 1 2 3 4 5 6 7 8 9

0
1
2
3
4
5
6
7
8
9
10

################################################

Base-11: Undecimal   --->   0 1 2 3 4 5 6 7 8 9 a 

0
1
2
3
4
5
6
7
8
9
a
10

################################################

Base-16: hexadecimal

--->   0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15

--->   0 1 2 3 4 5 6 7 8 9 a  b  c  d  e  f

0
1
2
3
4
5
6
7
8
9
a
b
c
d
e
f    15
10   1 (16)
100  1 1 (16 16)
1000 1 1 1 (16 16 16) 4096

###############################################################################################

Integer (whole numbers, positive or negative, without decimals) ( -3, -1, 0, 1, 2 )

1. bin                  --->   Binary, 0b       ( -0b11, -0b1, 0b0, 0b1, 0b10 )
2. oct                  --->   Octal, 0o        ( -0o3, -0o1, 0o0, 0o1, 0o2 )
3. hex                  --->   Hexadecimal, 0x  ( -0x3, -0x1, 0x0, 0x1, 0x2 ) (0 to 15)

Creating integer by name and symbol
- int(10), 10     <- decimal
- bin(10), 0b1010
- oct(10), 0o12
- hex(10), 0xa

################################################

0b11   <-- int, 3

bin(3) <-- str value of binary, "0b11"

################################################################################################

2. Type casting

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


chr -> str 
ord -> int
bin -> str  "0b0011"
oct -> str  "0o75"
hex -> str  "0xa"
repr -> str
eval -> program output(15 +)

c o 2 8 16 r e

################################################

x = int(input("enter x : "))
y = int(input("enter y : "))
f = input("enter x, y formula : ") # "x + y" , "2 * x + y"
z = eval(f) # x + y
print("z =", z)

################################################################################################

"""