
"""

Day.4

Indexing
- positive index
- negative index
- hard = total - abs of easy
- f1, f5, f10
- l1, l5, l10
- index range = -t to t-1
- middle
  - odd, m = t // 2
  - even, r = t // 2, l = r - 1 
  
################################################

a b c d e f g        7
0 1 2 3 4 5 6        positive index
7 6 5 4 3 2 1        negative index

################################################

Day.5

Slicing
- value ("cdef")
- index of value 
  - "cdef"   ->   2, 3, 4, 5 and -5, -4, -3, -2
  - "fedc"   ->   5, 4, 3, 2 and -2, -3, -4, -5
- range 
  - "cdef"   ->   [2:6:1] and [-5:-1:1]
  - "fedc"   ->   [5:1:-1] and [-2:-6:-1]
- f5, f10 => [:5] # 0 1 2 3 4
- l5, l10 => [-5:] # -5, -4, -3, -2, -1
- step
  - left to right = 1 2 3 4 = positive
  - right to left = 4 3 2 1 = negative
- reverse => [::-1] 
  - richest country 10 to poorest country list
  - poorest 10 from richest country list => l10 reverse => [-10:][::-1]
- half => [:m], [m:]
- 3 parts  => [:p1], [p1:p2], [p2:]
- 4 parts  => [:p1], [p1:p2], [p2:p3], [p3:]

################################################  

"abcdefg"

f5 -> "abcde" -> 0, 1, 2, 3, 4 -> [0:5:1] -> [:5:1] -> [:5]

f5
from starting point, stop at index of 6
[:5]

f10
from starting point, stop at index of 11
[:10]

f3
from starting point, stop at index of 4
[:3]

f17
from starting point, stop at index of 18
[:17]

################################################

l5

[-5:]
from -5 to the end

################################################

richest country list

richest_10 
1. value = f10
2. index = 0 to 9
3. stop = 10
4. [:10]

poorest_10 
1. value = l10
2. index = -10 to -1
3. start = -10
4. [-10:]

richest_5
1. value = f5
2. index = 0 1 2 3 4
3. stop = 5
4. [:5]

poorest_5 
1. value = l5
2. index = -5, -4, -3, -2, -1
3. start = -5
4. [-5:]

################################################

poorest country list

richest_10 
1. value = l10
2. index = 
3. stop = 
4. [-10:]

poorest_10 
1. value = f10
2. index = 
3. stop = 
4. [:10]

################################################

"abcdefg"

step
left to right = 1 2 3 4 = positive
right to left = 4 3 2 1 = negative


[::1]   => "abcdefg"
[left:right:1]

[::-1]  => "gfedcba"
[right:left:-1]

1 (left to right)
-1 (right to left) 

reverse => richest country list to poorest country list

f5 => [:5]   => [0:5:1] # 0 1 2 3 4
l5 => [-5:]  => [-5::1] # -5 -4 -3 -2 -1
n  => [::1]  => if t = 7, 0123456 or -7-6-5-4-3-2-1
r  => [::-1] => if t = 7, 6543210 or -1-2-3-4-5-6-7 

################################################

poorest_10 from richest country list

poorest_10 
- l10
- l10 = [-10:]  # -10, -9, -8, to -1
- reverse
  - poorest_10 = l10[::-1] # -1, -2, -3 to -10

################################################

richest_10 from poorest country list

richest_10 = [-10:][::-1]

[-10:]   [::-1]

last 10  reverse
 
[-10:] => [l10:right_end:1] => -10 to -1 => last 10
[::-1] => -1 to -10 => reverse

################################################

Half

"abcdefgh"    8

half_1 = "abcd" => [start:e] => [:4] => 0 1 2 3
half_2 = "efgh" => [e:end] => [4:] => 4 5 6 7

half_1 = [:mid]
half_2 = [mid:]

"abcdefgh"    8 // 2 = rm
"abcdefg"     7 // 2 = m
"abc" + "defg"

 11
 5 + 6
 
 13
 6 + 7
 
################################################

Three parts(1/3)
 
"abcdefghi"

"abc" + "def" + "ghi"

12

....p1...p2...
............

....p1 = ....
p1...p2 = ....
p2...   = ....

f1 = start to p1 = [:p1]
f2 = p1 to p2    = [p1:p2]
f3 = p2 to end   = [p2:]

p1 = ?
p2 = ?

################################################

         p1       p2
. . . .  . . . .  . . . .
1 2 3 4  5 6 7 8  9 101112
0 1 2 3  4 5 6 7  8 9 10 11

p1 = 12 // 3 = 4
p2 = 12 // 3 * 2 = 8

################################################

Four parts(1/4)

         p1       p2         p3       
. . . .  . . . .  . . . .    . . . . 
1 2 3 4  5 6 7 8  9 101112  13
0 1 2 3  4 5 6 7  8 9 10 11 12

f1 = start to p1 = [:p1]
f2 = p1 to p2    = [p1:p2]
f3 = p2 to p3    = [p2:p3]
f4 = p3 to end   = [p3:]

p1 = 16 // 4 = 4
p2 = 16 // 4 * 2 = 8
p3 = 16 // 4 * 3 = 12

p1 = t // 4
p2 = p1 * 2
p3 = p1 * 3

x[len(x) // 4 * 3:]

################################################

Half

9, 10

[:m] = 4  , 5
[m:] = 5  , 5

5 + 4
[:m+1] [m+1:]

################################################

Exercise => Five parts (1/5)

################################################################################################

"""


