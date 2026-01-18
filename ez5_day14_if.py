
"""

Day.14

if mark is greater than 40, exam pass.
if mark is less than 40, exam fail.

mark = int(input("Marks = "))

p = mark >= 40
f = mark < 40

if p: print("exam pass.")

if f: print("exam fail.")


1. ge()
2. assign()
3. lt()
4. assign()
5. if1
6. if2
7. fail

################################################

if mark is greater than 40, exam pass.
if not mark is greater than 40, exam fail.

mark = int(input("Marks = "))

p = mark >= 40

if p: print("exam pass.")

if not p: print("exam fail.")


1. ge()
2. assign()
3. if1
4. if2
5. fail

################################################

if mark is greater than 40, exam pass.
Else, exam fail.


mark = int(input("Marks = "))

exam_pass = mark >= 40

if exam_pass: print("exam pass.")

else: print("exam fail.")


1. ge()
2. assign()
3. if
4. fail

################################################

mark = int(input("Marks = "))

if mark >= 40: print("exam pass.")

else: print("exam fail.")


1. if
2. ge()
3. fail

################################################

if int(input("Marks = ")) >= 40: print("exam pass.")

else: print("exam fail.")

################################################################################################

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

- 110 => a c h

################################################

Step.2 (output => condition?) (control)

- acg => 111
- ach => 110
- bfg => 001
- be  => 01-  ( 011, 010 )

################################################

Step.3 (condition => new code)
- 1100 => print("new")
- 1111 => print("new2")
- 0001 => print("new3")
- 0000 => print("new4")
- 1010 => print("new5")

c4 = False

if c4:
    pass
else:
    print("new")
        
if not c4:
    print("new")
        
################################################

c1 = True
c2 = False
c3 = True
c4 = False

if c1:
    print("a")
    if c1:
        print("c")
    else:
        print("d")
else:
    print("b")


if c1:
    print("a")
    if c2:
        print("c")
        if c3:
            print("g")
            if c4:
                print("new2")

        else:
            print("h")
            if c4:
                pass
            else:
                print("new")

    else:
        print("d")
        if c3:
            print("g")
            if not c4:
                print("new5")

        else:
            print("h")


else:
    print("b")
    if c2:
        print("e")

    else:
        print("f")
        if c3:
            print("g")

        else:
            print("h")
            if c4:
                print("new3")
            else:
                print("new4")
                
################################################################################################

day. 15

Step.4 ( idea => code )
- motor on

################################################

1. low_level

if low_level:
    print("motor on")
    
################################################

2. electric

if low_level:
    if electric:
        print("motor on")
    else:
        print("generator on")
        print("motor on")

################################################

3. short_circuit

low_level = True
electric = False
short_circuit = True

if low_level:
    if electric:
        if short_circuit:
            print("call mechanic")
            print("motor.2 on")
        else:
            print("motor on")
    else:
        print("generator on")
        if short_circuit:
            print("call mechanic")
            print("motor.2 on")
        else:
            print("motor on")

################################################
       
4. m2  

low_level = True
electric = False
short_circuit = True
short_circuit2 = True

if low_level:
    if electric:
        if short_circuit:
            print("call mechanic (m1) ")
            if short_circuit2:
                print("call mechanic (m2) ")
            else:
                print("motor.2 on")
        else:
            print("motor on")
    else:
        print("generator on")
        if short_circuit:
            print("call mechanic (m1) ")
            if short_circuit2:
                print("call mechanic (m2) ")
                print("generator off")
            else:
                print("motor.2 on")
        else:
            print("motor on")

        
################################################

5. m3

11110
10110

11111
10111

low_level = True
electric = False
short_circuit = True
short_circuit2 = True
short_circuit3 = True

if low_level:
    if electric:
        if short_circuit:
            print("call mechanic (m1) ")
            if short_circuit2:
                print("call mechanic (m2) ")
                if short_circuit3:
                    print("call mechanic (m3) ")
                else:
                    print("motor.3 on")
            else:
                print("motor.2 on")
        else:
            print("motor on")
    else:
        print("generator on")
        if short_circuit:
            print("call mechanic (m1) ")
            if short_circuit2:
                print("call mechanic (m2) ")
                if short_circuit3:
                    print("call mechanic (m3) ")
                    print("generator off")
                else:
                    print("motor.3 on")
            else:
                print("motor.2 on")
        else:
            print("motor on")

################################################

6. m4

111110
101110

111111
101111

################################################################################################

13. Normally open Vs Normally close

short circuit sensor
- Normal condition (close)      =>  no signal
- short circuit (open)          =>  signal

sensor error
- Normal condition       =>  no signal
- short circuit          =>  no signal    (sensor error)

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

14. Opposite condition ( not )
    
# normally close
if c3: # human
    print("Saw machine OFF")
else:
    print("Saw machine ON")
    
    
# open
if not c3: 
    print("Saw machine OFF")
else:
    print("Saw machine ON")

################################################ 

16. one from one ( if ), all from all

greater or equal 500, doctor    
greater or equal 400, engineer   
greater or equal 300, distance  

520  ->  1 2 3
420  ->  2 3
320  ->  3

mark = int(input("Marks = "))

c1 = mark >= 500
c2 = mark >= 400
c3 = mark >= 300

if c1:
    print("doctor")

if c2:
    print("engineer")

if c3:
    print("distance")

################################################ 

15. one from all (if + elif + else)

Doctor -> engineer -> distance  

mark = int(input("Marks = "))

c1 = mark >= 500
c2 = mark >= 400
c3 = mark >= 300

if c1:
    print("doctor")

if not c1 and c2:
    print("engineer")

if not c1 and not c2 and c3:
    print("distance")

################################################ 

> else + if

mark = int(input("Marks = "))

c1 = mark >= 500
c2 = mark >= 400
c3 = mark >= 300

if c1:
    print("doctor")

elif c2:
    print("engineer")

elif c3:
    print("distance")

################################################ 

mark = int(input("Marks = "))

if mark >= 500:
    print("doctor")

elif mark >= 400:
    print("engineer")

elif mark >= 300:
    print("distance")
    
################################################ 

> not c1 + not c2 + not c3 => online shop

mark = int(input("Marks = "))

if mark >= 500:
    print("doctor")

elif mark >= 400:
    print("engineer")

elif mark >= 300:
    print("distance")

else:
    print("online shop")

################################################ 

7. Boolean value  (empty, anything)

c1 = 1

if bool(c1):
    print("m1 on.")


if 1:
    print("m1 on.")

################################################ 

fruits = ["apple", "banana"]

if fruits:
    print("you can buy.")
    
else:
    print("you can not buy.")
    
################################################ 

if sensor value is something / anything, do it.   

sensor = "1V"

if sensor:
    print("m1 on.")

################################################################################################ 
 
"""

