"""

################################################

Knowledge

a. collection   -> "abcdefg"
b. element      -> a
c. absolute value -> abs of -5  -> 5
d. print()
e. standard output file
f. division, floating-point division     7 / 2 = 3.5
g. floor division, integer division      7 // 2 = 3
h. modulus                               7 % 2 = 1

################################################

7. length   -> len()

################################################

8. delete   -> del 

################################################

9. Indexing
    - positive index
    - negative index
    - hard = total - abs of easy
    - f1, f5, f10
    - l1, l5, l10
    - middle
      - odd, m = t // 2
      - even, r = t // 2, l = r - 1 
      
################################################

Exercise.1

if total is 35,
f1 = 0, -35
f5 = 4, -31
f10 = 9, -26 

l1 = -1, 34
l5 = -5, 30
l10 = -10, 25


Exercise.2

if t = 35, m = 17
if t = 36, lm = 17, rm = 18

################################################

10. Slicing 
    - value ("cdefg", "gfedc") (start:stop:step)
    - index of value 
      - "cdefg" => 2 3 4 5 6, -8 -7 -6 -5 -4    , c, h
      - "gfedc" => 6 5 4 3 2, -4 -5 -6 -7 -8    , g, b, -
    - f5, f10 => stop  => [:5]  # 0 1 2 3 4
    - l5, l10 => start => [-5:] # -5 -4 -3 -2 -1
    - reverse => step => [::-1]
    - left to right => step = positive
    - right to left => step = negative
    - richest to poorest 
    - half => [:m], [m:]
    - 3    => [:p1], [p1:p2], [p2:]
    - 4    => [:p1], [p1:p2], [p2:p3], [p3:]
    - 5    =>

################################################

Half

abcdefghij   10

if total is even,
rm = t // 2 = 5
     10
  5     5
abcde  fghij    
   

abcdefghijk   11
if total is odd,
m = t // 2 = 5

     11
  5      6
abcde  fghijk 


################################################

3 => 1/3, 2/3


x = "abcdefghhdydulwfoufhqohfoqhghohfqeoihfoehf1udhfdhgd"

t = len(x) # 51
p1 = t // 3  # 17
p2 = p1 * 2  # 34

print(t, p1, p2)

h1 = x[:p1]    # [:17] => 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16
h2 = x[p1:p2]  # [17:34] => 17 to 33
h3 = x[p2:]    # [34:]   => 34 to 50(end)

print(h1, h2, h3)

################################################

4  => 1/4, 2/4, 3/4

     12
 3  3  3  3

     abcdefghijkl
abc   def   ghi   jkl


x = "abcdefghijkl"
t = len(x)
p1 = t // 4  # 1/4
p2 = p1 * 2  # 2/4
p3 = p1 * 3  # 3/4

c1 = x[:p1]
c2 = x[p1:p2]
c3 = x[p2:p3]
c4 = x[p3:]

print(c1, c2, c3, c4)

################################################

start, stop, step

a b c d e f g    7
0 1 2 3 4 5 6 
7 6 5 4 3 2 1

b c d e
start = b (1, -6)
stop = f (5, -2)
step = +

x = "abcdefg"

print(x[1:5])    # pos
print(x[-6:-2])  # neg
print(x[-6:5])   # neg pos
print(x[1:-2])   # pos neg

################################################

real world

x = "abcdefgffugdddtyfuyffuyduf"

print(x[4:-4]) # f5 to l5  , start = f5, stop = l4
print(x[4:-4][::-1]) # l5 to f5
print(x[-5:3:-1]) # l5 to f5

################################################################################################

"""

