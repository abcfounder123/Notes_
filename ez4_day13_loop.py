"""

Procedural programming
1. Sequence (top, left, p)
2. Selection (if, else, elif)
3. Loop      (for, while)
4. Function

################################################

Looping
1. Iteration, Looping
2. Nested loop
3. for and range
4. for and indexing, indexing by length
5. for and break
6. for and count
7. for, count, break

################################################

1. Iteration, Looping

x = "Temperature 100°C." # 18

for c in x:
    print(c)
    
    
fruits = ["apple", "banana", "orange"]

for fruit in fruits:
    print(fruit)


numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

for number in numbers:
    print(number)

################################################

Looping
       
for _ in range(10):
    print("ha ha")    
    
################################################

2. Nested loop


fruits = ["apple", "banana", "orange"]

for fruit in fruits: # "apple"
    print(fruit)
    for c in fruit:
        print(c)
        

yearly_marks = [[75, 78, 80], [76, 80, 85], [70, 73, 85]]

for monthly_marks in yearly_marks:
    print(monthly_marks)
    for mark in monthly_marks:
        print(mark)

################################################

3. for and range

numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for number in numbers:
    print(number)

for number in range(0, 11, 1):
    print(number)

for number in range(11):
    print(number)


int  -> 11
list ->  1

range(11) -> 1
int  -> 1 

for n in range(100):
    pass

for _ in range(100):
    pass

################################################

4. for and indexing, indexing by length

x = "Temperature 100°C."  # 18 => positive index => 0 to 17

for i in range(18):
    print(x[i])
    
for i in range(len(x)):
    print(x[i])

################################################

5. for and break

x = "Temperature 100°C.I want Fahrenheit."

for i in range(len(x)):
    print(i, x[i])
    if x[i] == "°" and x[i+1] == "C":
        print("We found °C at", i)
        break

################################################

6. for and count

n = 0
n += 1


x = "100°C 100°C Temperature 100°C.I want 100°C Fahrenheit.100°C 100°C"
n = 0

for i in range(len(x)):
    print(i, x[i])
    if x[i] == "°" and x[i+1] == "C":
        print("We found °C at", i)
        n += 1

print("total count =", n)
   
################################################

7. for, count, break

x = "100°C 100°C Temperature 100°C.I want 100°C Fahrenheit.100°C 100°C"
n = 0

for i in range(len(x)):
    print(i, x[i])

    if x[i] == "°" and x[i+1] == "C":
        print("We found °C at", i)
        n += 1
        if n == 3: # >=
            break

print("total count =", n)

################################################

s = "I go to school by bycicle."
n = 0

for c in s:
    if c in "aeiouAEIOU":
        n += 1

print(n)

################################################################################################

"""


