"""
Indexing 

Left (+) 

1. zero
2. 1st = 0, last = t - 1
3. 5th ?, last 5 ?
   -> n - 1
   -> t - n  
4. middle index (odd, even)
5. left index from middle ( - ), right index from middle ( + )

################################################

Right (-)

1. one
2. 1st = t, last = 1
3. last 5 ? first 5 ?
   -> n
   -> t - (n-1)  
4. middle index (odd, even)
   - if odd
      - m = floor + 1
   if even,
      - rm = floor 
      - lf = floor + 1   
5. left index from middle ( + ), right index from middle ( - )
     
################################################

last and first 

positive index of last value = t - 1
negative index of last value = 1

positive index of first value = 0
negative index of first value = t

################################################

middle index 

total = odd, middle = 1
m = t // 2

total = even, middle = 2
rm = t // 2
lm = rm - 1 

################################################

Indexing for programming

1. positive index, negative index
2. if t = 100, 
   - f1 -> 0, -100
   - l1 -> -1, 99
   - f5 -> 4, -96
   - l5 -> -5, 95
   hard = total - absolute of easy index
   
################################################################################################   
   
Slicing

1. result, start:stop:step
2. positive and negative for each item
3. blank ---> [:4], [-4:]
4. dataset
  - first five, last five, middle 10, poorest five
  - inverse

################################################

1. result, start:stop:step

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

2. positive and negative for each item

"abcdefghijklmnopqrstuvwxyz"

'zyxwvutsrq'

start = z
stop = p

1. negative index = (-1, -11, -1)

(t = 26)
2. positive index = (25, 15, -1)

3. negative + positive = (-1, 15, -1) 

3. inverse last 10 = [-10:][::-1]

################################################

3. blank

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

4. dataset
  - first five, last five
  - inverse 
   
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

"middle 10"

rm = len(rich_countries) // 2

start = rm - 10
stop = rm + 10

print(rich_countries[start:stop])

################################################

# reverse engineering of middle 11 inverse

middle 11 inverse
=> [t // 2 - 5 : t // 2 + 6][::-1]
=> [s:stop][::-1]

1. m = t // 2
2. s = m - 5
3. stop = m + 6 
4. [::-1] <-- inverse

################################################ 

- poorest five from richest dataset 
  -> -1, -2, -3, -4, -5        ->   -1:-6:-1     ->   :-6:-1     (easy index)
  -> 199, 198, 197, 196, 195   ->   199:194:-1   ->   :194:-1    (hard index)

################################################ 

richest dataset to  poorest dataset
:::   ->   0:200:1     ->   0, 1, 1, 3, ..., 199
::-1  ->  -1:-201:-1   ->   -1, -1, -3, ..., -200

################################################################################################  


"""