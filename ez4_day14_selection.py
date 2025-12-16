
"""

Day.14

Selection

1. Normal Statement ( ; end of line)
   - motor on
   - motor off
   - pass
   - fail

2. Conditional Statement
   - If water level is low, motor on.  
   - If water level is high, motor off. 
   - if exam pass, show "pass".
   - if exam fail, show "fail".

3. Conditional if Statement
   - boolean data type
   - True

3. Conditional else Statement
   - boolean data type
   - False

################################################

# 10

mark = int(input("Marks : "))
c1 = mark >= 40
c2 = mark < 40

if c1:
    print("Exam pass.")
    print("Kg out")
    print("G1 in.")

if c2:
    print("Exam fail.")
    print("parent")

################################################

# 8
mark = int(input("Marks : "))

if mark >= 40:
    print("Exam pass.")
    print("Kg out")
    print("G1 in.")

if mark < 40:
    print("Exam fail.")
    print("parent")


1. input()
2. int()
3. assign
4. ge()        
5. if1        True
6. if1 block
7. lt()       
8. if2        False

1. input()
2. int()
3. assign
4. ge()  
5. if1        False     
6. lt()
7. if2        True
8. if2 block

################################################

# 6
mark = int(input("Marks : "))

if mark >= 40:
    print("Exam pass.")
    print("Kg out")
    print("G1 in.")

else:
    print("Exam fail.")
    print("parent")


1. input()
2. int()
3. assign
4. ge()  
5. if        False
6. else block

1. input()
2. int()
3. assign
4. ge()  
5. if        True
6. if block

################################################

one from two
- if else

mark = int(input("Marks : "))

if mark >= 40:
    print("Exam pass.")
    print("Kg out")
    print("G1 in.")

else:
    print("Exam fail.")
    print("parent")

################################################################################################

1. Conditional if, if
2. Code block
3. Conditional code block
4. Conditional if code block, if code block, if block 
5. Conditional else code block, else code block, else block  
6. Condition
7. Boolean value
8. program flow
9. control flow
10. : (code block)

mark = int(input("Marks : "))

if mark >= 50:
    print("Exam pass.")

else:
    print("Exam fail.")
  
################################################
  
if something fruit,You can buy fruits.

if fruits:
    print("You can buy fruits.")  
    
################################################
    
if empty fruit,You can not buy fruits.

1. if True 
2. not False
3. empty fruit

fruits = ["apple", "banana", "orange"]

if not fruits:
    print("You can not buy fruits.")

################################################

c1    low
c2    electric
c3    short circuit , not

################################################

1. low                                  ->  print("water motor ON.")
2. low + not short circuit              ->  print("water motor ON.")

################################################

1. low                                  ->  print("water motor ON.")

if c1:print("water motor ON.")

################################################

2. low + not short circuit              ->  print("water motor ON.")

if c1:
    if not c3:
        print("water motor ON.")
        
################################################

3. low + electric + not short circuit              ->  print("water motor ON.") 

1 1 0

if c1:
    if c2:
        if not c3: print("water motor ON.")
    
################################################

4. low + not electric                              ->  print("Generator ON.") 

################################################

5. low + not electric + not short circuit              ->  print("Generator ON."), print("water motor ON.") 

1 0 0

################################################

6. low + not electric + short circuit                  ->  print("Generator Off.")

1 0 1

################################################

7.
                                               print("call mechanic")
1 1 1
1 0 1

################################################

8. motor 2

1 1 1 0
1 0 1 0

print("water motor.2 ON.")


################################################

9. print("call mechanic")

1 1 1 1
1 0 1 1

################################################

Exercise 

10. motor 3

1 1 1 1 0
1 0 1 1 0

################################################

11. 
print("call mechanic")
print("Generator Off.")

1 1 1 1 1
1 0 1 1 1

################################################################################################


"""
