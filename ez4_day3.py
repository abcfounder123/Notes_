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

Day.4

################################################

range of collection

"abcdefg" (-t to t-1) 

t = 7, range = -7 -6 -5 -4 -3 -2 -1 0 1 2 3 4 5 6
t = 10, range = -10 to 9
t = 100, range of range = -100 to 99

################################################

out of range error

IndexError: string index out of range
IndexError: list index out of range
IndexError: tuple index out of range

#################################################

indexing (1D, 2D, 3D)

x = [("apple", "banana"), ("apple", "orange")]


print(x) # [("apple", "banana"), ("apple", "orange")]
print(x[0]) # ("apple", "banana")
print(x[0][1]) # "banana"
print(x[0][1][::-1]) # "ananab"

################################################

richest dataset
richest 10 = x[:10]
poorest 10 = x[-10:][::-1]
poorest 10 = x[:-11:-1]

4 => Start, 1/4, 2/4, 3/4, END

richest dataset
1 2 3 ... 191 192 ... 200

################################################

richest_countries = ['Country.1', 'Country.2', 'Country.3', 'Country.4', 'Country.5', 'Country.6', 'Country.7', 'Country.8', 'Country.9', 'Country.10', 'Country.11', 'Country.12', 'Country.13', 'Country.14', 'Country.15', 'Country.16', 'Country.17', 'Country.18', 'Country.19', 'Country.20', 'Country.21', 'Country.22', 'Country.23', 'Country.24', 'Country.25', 'Country.26', 'Country.27', 'Country.28', 'Country.29', 'Country.30', 'Country.31', 'Country.32', 'Country.33', 'Country.34', 'Country.35', 'Country.36', 'Country.37', 'Country.38', 'Country.39', 'Country.40', 'Country.41', 'Country.42', 'Country.43', 'Country.44', 'Country.45', 'Country.46', 'Country.47', 'Country.48', 'Country.49', 'Country.50', 'Country.51', 'Country.52', 'Country.53', 'Country.54', 'Country.55', 'Country.56', 'Country.57', 'Country.58', 'Country.59', 'Country.60', 'Country.61', 'Country.62', 'Country.63', 'Country.64', 'Country.65', 'Country.66', 'Country.67', 'Country.68', 'Country.69', 'Country.70', 'Country.71', 'Country.72', 'Country.73', 'Country.74', 'Country.75', 'Country.76', 'Country.77', 'Country.78', 'Country.79', 'Country.80', 'Country.81', 'Country.82', 'Country.83', 'Country.84', 'Country.85', 'Country.86', 'Country.87', 'Country.88', 'Country.89', 'Country.90', 'Country.91', 'Country.92', 'Country.93', 'Country.94', 'Country.95', 'Country.96', 'Country.97', 'Country.98', 'Country.99', 'Country.100', 'Country.101', 'Country.102', 'Country.103', 'Country.104', 'Country.105', 'Country.106', 'Country.107', 'Country.108', 'Country.109', 'Country.110', 'Country.111', 'Country.112', 'Country.113', 'Country.114', 'Country.115', 'Country.116', 'Country.117', 'Country.118', 'Country.119', 'Country.120', 'Country.121', 'Country.122', 'Country.123', 'Country.124', 'Country.125', 'Country.126', 'Country.127', 'Country.128', 'Country.129', 'Country.130', 'Country.131', 'Country.132', 'Country.133', 'Country.134', 'Country.135', 'Country.136', 'Country.137', 'Country.138', 'Country.139', 'Country.140', 'Country.141', 'Country.142', 'Country.143', 'Country.144', 'Country.145', 'Country.146', 'Country.147', 'Country.148', 'Country.149', 'Country.150', 'Country.151', 'Country.152', 'Country.153', 'Country.154', 'Country.155', 'Country.156', 'Country.157', 'Country.158', 'Country.159', 'Country.160', 'Country.161', 'Country.162', 'Country.163', 'Country.164', 'Country.165', 'Country.166', 'Country.167', 'Country.168', 'Country.169', 'Country.170', 'Country.171', 'Country.172', 'Country.173', 'Country.174', 'Country.175', 'Country.176', 'Country.177', 'Country.178', 'Country.179', 'Country.180', 'Country.181', 'Country.182', 'Country.183', 'Country.184', 'Country.185', 'Country.186', 'Country.187', 'Country.188', 'Country.189', 'Country.190', 'Country.191', 'Country.192', 'Country.193', 'Country.194', 'Country.195', 'Country.196', 'Country.197', 'Country.198', 'Country.199', 'Country.200']

richest_10 = richest_countries[:10]
poorest_10 = richest_countries[-10:][::-1]

# 4 => Start, 1/4, 2/4, 3/4, END

t = len(richest_countries) # 200
p1 = t // 4  # int
p2 = p1 * 2
p3 = p1 * 3

q1 = richest_countries[:p1]
q2 = richest_countries[p1:p2]
q3 = richest_countries[p2:p3]
q4 = richest_countries[p3:]

poorest_countries = richest_countries[::-1]

################################################################################################

11. collections and indexing ( base + size * n ) (n = i + 1)

door = 20 km
house1_size  = 20 m
address = 20km to  20km 


Town..........||||.||||.||||.
     20km      20m
     
################################################     

ordered collection of elements

x = ["house.1", "house.2"]
1000000
1000028
1000056

################################################

unordered collection of elements
base = 1000000
h1 = 10
h2 = 200000

################################################

12. Characteristics of data types
    - ordered, unordered, mutable, immutable

list =>   mutable ordered
tuple =>  immutable ordered
set  =>   mutable unordered unique

################################################

collections
1. str
2. list
3. tuple
4. set
5. frozenset
6. bytearray
7. bytes
8. dict

unordered collections
1. set
2. frozenset
3. dict

ordered collections
1. str
2. list
3. tuple
4. bytearray
5. bytes

################################################

mutable data types (4+1)
1. list
2. set
3. bytearray, memoryview() of bytearray()
4. dict

immutable data types (10+1)
1. str()
2. int()
3. float()
4. complex()
5. tuple()
6. frozenst()
7. bytes(), memoryview() of bytes()
8. range()
9. bool()
10. NoneType

################################################

Low level programming language
High level programming language 

################################################################################################

1. Procedure              4
2. Sequence               3
3. Data types            15
4. Creating by names     14
5. Creating by symbols   11
6. range                  3
7. length   -> len()
8. delete   -> del
9. Indexing(+, -, hard, middle)
10. Slicing (start:stop:step, half)
11. collections and indexing ( base + size * n ) (n = i + 1)
12. Characteristics of data types
    - ordered, unordered, mutable, immutable

################################################################################################

Knowledge
1. collection   -> "abcdefg"
2. element      -> a
3. absolute value -> abs of -5  -> 5
4. print()
5. standard output file
6. division, floating-point division     7 / 2 = 3.5
7. floor division, integer division      7 // 2 = 3
8. modulus                               7 % 2 = 1
9. range of collection, out of range error
10. 1/2, 1/3, 1/4
11. Low level programming language
12. High level programming language 

################################################################################################


"""

