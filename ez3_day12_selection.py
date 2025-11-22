
"""

Day.12 (selection)

1. conditional if, if
2. code block
3. conditional code block
4. conditional if code block, if code block, if block
5. conditional else code block, else code block, else block 
6. condition
7. boolean value
8. program flow
9. control flow
10. : (code block)
11. pass (keyword name for pass)
12. nested if

################################################

1. Imperative Paradigm
                                 less 
Procedural programing      10     1      (new procedure)
1. Sequence
2. Selection
3. looping
4. Function
                                  4 KB = 4000
                                  8 GB = 8_000_000_000 = 80 million
                                  100
                                  
                                memory
OOP                        10     10    


2. Declarative Paradigm
   - FP

################################################

1. Normal statement
   - moter on
   - motor off

2. Conditional statement, selection
   - If water level is low, moter on.  (if condition1: p1)
   - if water level is high, motor off. (if condition2: p2)
   
3. Conditional if statement
   - boolean data type
   - True
   
4. Conditional else statement
   - boolean data type
   - False

################################################

1. code block
2. conditional code block
3. conditional if code block, if code block, if block ( 4 spaces )
4. conditional else code block, else code block, else block 
5. condition of if / else
6. : (code block)
7. pass (keyword name for pass)
8. nested if

################################################

step.1

marks = int(input("marks = "))

exam_pass = marks >= 50
exam_fail = marks < 50

if exam_pass:
    print("Exam pass")
    print("Kg out")
    print("G1 in")
    
if exam_fail:
    print("Exam fail")
    print("parent")
    
1. input()    -> str
2. int()      -> type casting
3. assign()
4. ge()       -> bool
5. assign()
6. lt()       -> bool
7. assign()
8. if         ->  True
9. if block
10. if         -> False

################################################

step.2
    
marks = int(input("marks = "))

if marks >= 50:
    print("Exam pass")
    print("Kg out")
    print("G1 in")

if marks < 50:
    print("Exam fail")
    print("parent")
    
    
1. input()   
2. int()      
3. assign()
4. if        
5. ge()
6. if block
7. if 
8. lt

################################################

step.3

marks = int(input("marks = "))

if marks >= 50:
    print("Exam pass")
    print("Kg out")
    print("G1 in")

else:
    print("Exam fail")
    print("parent")

1. input()   
2. int()      
3. assign()
4. if        
5. ge()
6. if block

1. input()   
2. int()      
3. assign()
4. if        
5. ge()
6. else block

################################################

1. program -> control condition   (1100)
2. condition -> new program

################################################

1. low                                      ->   print("water motor ON")
2. full                                     ->   print("water motor OFF")
3. low + not short_circuit                  ->   print("water motor ON")
4. low + electric + not short_circuit       ->   print("water motor ON")                           110      
5. low + not electric                       ->   print("Generator ON")
6. low + not electric + not short_circuit   ->   Generator ON -> print("water motor ON")           100       
7. low + electric + short_circuit_1 +  not short_circuit_2         ->   print("water motor.2 ON")  1110
8. low + not electric + short_circuit_1 +  not short_circuit_2     ->   print("water motor.2 ON")  1010
9. 1111     ->   print("call mechanic")
10. 1011    ->   print("call mechanic")  
11. 11110   ->   print("water motor.3 ON")
12. 10110   ->   print("water motor.3 ON") 
13. 11111        print("call mechanic")
14. 10111        print("call mechanic")
15. call mechanic for all short_circuit

16. 111110  ->   print("water motor.4 ON")
17. 101110  ->   print("water motor.4 ON")
18. 111111       print("call mechanic")
19. 101111       print("call mechanic")


c1    low
c2    electric
c3    m1 short
c4    m2 short
c5    m5 short
c6    m6 short

111110  m4
101110  m4

111111  Mechanic
101111  Mechanic

################################################

c1 = 1
c2 = 0
c3 = 1
c4 = 1
c5 = 1
c6 = 1

if c1:
    if c2:
        if c3:
            if c4:
                if c5:
                    print("call mechanic")
                else:
                    print("water motor.3 ON")
            else:
                print("water motor.2 ON, e")
        else:
            print("water motor.1 ON")

    else:
        print("Generator ON")
        if c3:
            if c4:
                if c5:
                    print("call mechanic")
                else:
                    print("water motor.3 ON")
            else:
                print("water motor.2 ON")
        else:
            print("water motor.1 ON")

################################################################################################

"""

