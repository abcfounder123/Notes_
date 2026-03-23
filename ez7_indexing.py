
"""

Indexing
- positive index
- negative index
- hard = total - abs value of easy
- f1, f5, f10
- l1, l5, l10    
- middle index
  - odd, m = total // 2
  - even, rm = total // 2, lm = rm - 1
- range
- out of range

#################################################

 Slicing
 - value
 - index
 - start, stop, step
 
 - f5 (start to 4)
   - stop = 5
   - x[:5]
   
 - l5 (l5 to end)
   - start = -5
   - x[-5:]
   
- reverse = [::-1]
  - left to right => step = +
  - right to left => step = -
  - richest to poorest = reverse

#################################################

Extra
1. half => [:m], [m:]                                 1/2
2. 3    => [:p1], [p1:p2], [p2:]                      1/3, 2/3
3. 4    => [:p1], [p1:p2], [p2:p3], [p3:]             1/4, 2/4, 3/4
4. 5    => [:p1], [p1:p2], [p2:p3], [p3:p4], [p4:]    1/5, 2/5, 3/5, 4/5
6. 80%, 20% => 4/5, 
   20%, 80% => 1/5
7. 90%, 10% => 9/10, 
   10%, 90% => 1/10
8. 75%, 25% => 3/4, 
   25%, 75% => 1/4
9. 85%, 15% => 85/100
10. 17%     => start to 17/100

#################################################

1. Reverse Engineering

richest[-10:][::-1]

last 10   =>    [-10:]    
reverse   =>    [::-1]
poorest 10

#################################################

2. Real world

f10 = richest[:10]
l10 = richest[-10:]
reverse = richest[::-1]

print(richest[-1:-11:-1])      <= complex
print(richest[-10:][::-1])     <= simple

#################################################

3. Range of collection

total = 10
range = -10 to 9

#################################################

out of range

#################################################

4. 1D, 2D, 3D

1D

x = [1, 2, 3, 4, 5]

element 3  =>  x[2]

#################################################

2D

x = [1, 2, "apple", 4, 5]

"apple"  =>  x[2]
"a"      =>  x[2][0]

#################################################

3D

x = [1, 2, ["apple", "banana"], 4, 5]

["apple", "banana"]  =>  x[2]
"banana"             =>  x[2][1]
"b"                  =>  x[2][1][0]


#################################################

x = [1, 2, ["apple", "banana", ["XYZ", "def"]], 4, 5]

print(x[2])
print(x[2][-1])
print(x[2][-1][0])
print(x[2][-1][0][0])

#################################################

  _______
 |       |
 |       |
 |_______|

   ________
  /       /|
 /_______/ |
 |       | |
 |       | /
 |_______|/


length, width, thick, 
length, width, thick, time

photo = length, width
video = length, width, time

#################################################

7 houses

base = 100 km
h1 = 100 km + 50 m
h2 = 100 km + 100 m
h7 = 100 km + 50 * 7 m
h10 = 100 km + 500 m

x = "abcdefg"     
base = 1_000_000
"a"  = 1_000_060
"b"  = 1_000_120

#################################################

"""
