
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

Day.15
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
11. pass (keyword name for pass)
12. nested if (step.4)
13. Normally open Vs Normally close
14. Opposite condition ( not )
15. one from all (if + elif + else)
16. all from all, one from one ( if ), one from two ( if + else )

################################################

Step.1 (condition => output?) (flow)

- 110 => a c j

################################################

Step.2 (output => condition?) (control)

- acj => 110
- beh => 010
- beg => 011
- g   => 0110,0111 => 011

################################################

Step.3 (condition => new code)
- 1100 => print("new")
- 1111 => print("new2")
- 0001 => print("new3")
- 0000 => print("new4")
- 1010 => print("new5")

c4 = 0
if c4:
    pass
else:
    print("new")
    
    
if c3:
    pass
else:
    if c4:
        print("new3")
        
################################################

c1 = 1
c2 = 0
c3 = 1
c4 = 0


if c1:
    print("a")
    if c2:
        print("c")
        if c3:
            print("i")
            if c4:
                print("new2")
        else:
            print("j")
            if c4:
                pass
            else:
                print("new")

    else:
        print("d")
        if c3:
            if c4:
                pass
            else:
                print("new5")

else:
    print("b")
    if c2:
        print("e")
        if c3:
            print("g")
        else:
            print("h")
    else:
        print("f")
        if c3:
            pass
        else:
            if c4:
                print("new3")
            else:
                print("new4")

################################################

Step.4 ( idea => code )
- motor on

################################################

idea => If motor has short circuit, call mechanic. Else, Motor ON. 

if c3:
    print("call mechanic")
else:
    print("Motor ON.")

################################################
      
idea => If motor is good, Motor ON. Else, call mechanic.     
    
if not c3:
    print("Motor ON.")   
else:
    print("call mechanic")
    
################################################  

short circuit(not good) => c3
good                    => not c3 

################################################

idea =>  add a new motor

low + electric + short + not short
1 1 1 0  print("new motor ON")

low + not electric + short + not short
1 0 1 0  print("new motor ON")


################################################

print("call mechanic")

111

low + electric + m1 short

################################################

c1 = 1
c2 = 1
c3 = 1
c4 = 1

if c1:
    if c2:
        if c3:
            print("call mechanic")
            if c4:
                pass
            else:
                print("new motor ON")
        else:
            print("Motor ON.")

    else:
        print("Generator ON.")
        if not c3:
            print("Motor ON.")

        else:
            print("call mechanic")
            if not c4:
                print("new motor ON")

################################################

c1 = input("low_level sensor = ")
c2 = input("electric sensor = ")
c3 = input("M1 short_circuit sensor = ")
c4 = input("M2 short_circuit sensor = ")

if c1:
    if c2:
        if c3:
            print("call mechanic")
            if c4:
                pass
            else:
                print("new motor ON")
        else:
            print("Motor ON.")

    else:
        print("Generator ON.")
        if not c3:
            print("Motor ON.")

        else:
            print("call mechanic")
            if not c4:
                print("new motor ON")
            else:
                print("Generator OFF.")

################################################  

Normally open Vs Normally close

short circuit sensor
- Normally close       =>  no signal
- short circuit open   =>  signal

short circuit sensor (error)
- good => no signal
- not good => no signal

################################################  

Normally open for safety purpose
- Normally open        =>  signal
- short circuit open   =>  not signal  (human, sensor)
          
if c3:
    print("Saw machine ON")
else:
    print("Saw machine OFF")
    
    
# close
if c3: # human
    print("Saw machine OFF")
else:
    print("Saw machine ON")
    
################################################ 

Opposite condition ( not )
    
# close
if c3: # human
    print("Saw machine OFF")
else:
    print("Saw machine ON")
    
    
# open
if not c3: # human
    print("Saw machine OFF")
else:
    print("Saw machine ON")

################################################################################################ 

one from many

greater or equal 500, doctor     1
greater or equal 400, engineer   1 + 2
greater or equal 300, distance   1 + 2 + 3

one from three
precedence  =>  doctor -> engineer -> distance
    
c1 = greater or equal 500
c2 = greater or equal 400
c3 = greater or equal 300

c1 => doctor
not c1 and c2 => engineer
not c1 and not c2 and c3 => distance

################################################

marks = int(input("Marks = "))

c1 = marks >= 500
c2 = marks >= 400
c3 = marks >= 300

if c1: print("Doctor")
if not c1 and c2: print("Engineer")
if not c1 and not c2 and c3: print("Distance")

################################################

marks = int(input("Marks = "))

c1 = marks >= 500
c2 = marks >= 400
c3 = marks >= 300

if c1: print("Doctor")
elif c2: print("Engineer") # not c1 and c2
elif c3: print("Distance") # not c1 and not c2 and c3

################################################

marks >= 90    A+
marks >= 80    A
marks >= 70    B
marks >= 50    C
marks < 50     Fail

one from 5

################################################

c1 = marks >= 90    A+
c2 = marks >= 80    A
c3 = marks >= 70    B
c4 = marks >= 50    C

c1
not c1 and c2
not c1 and not c2 and c3
not c1 and not c2 and not c3 and c4

################################################

marks = int(input("marks = "))

c1 = marks >= 90
c2 = marks >= 80
c3 = marks >= 70
c4 = marks >= 50

if c1:
    print("A+")
elif c2:
    print("A")
elif c3:
    print("B")
elif c4:
    print("C")

################################################

95 marks  -> 13

################################################

marks = int(input("marks = "))

if marks >= 90:
    print("A+")
elif marks >= 80:
    print("A")
elif marks >= 70:
    print("B")
elif marks >= 50:
    print("C")

################################################

95  -> 6

################################################

marks = int(input("marks = "))

if 100 >= marks >= 90:
    print("A+")
    
if 90 > marks >= 80:
    print("A")
    
if 80 > marks >= 70:
    print("B")
    
if 70 > marks >= 50:
    print("C")

################################################

95  -> 16

################################################

one from all (if + elif + else)

marks = int(input("marks = "))

if marks >= 90:
    print("A+")
elif marks >= 80:
    print("A")
elif marks >= 70:
    print("B")
elif marks >= 50:
    print("C")
else:
    print("F")  # F => not c1 + not c2 + not c3 + not c4
    
################################################

all from all

marks = int(input("Marks = "))

c1 = marks >= 500
c2 = marks >= 400
c3 = marks >= 300

if c1: print("Doctor")
if c2: print("Engineer")
if c3: print("Distance")
    
################################################################################################

"""
