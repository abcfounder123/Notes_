
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

"""

