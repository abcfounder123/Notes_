
"""
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

step.1 (condition -> output)(flow)
- 1101  acjm

################################################

step.2 (output -> condition)(control)
- acjn  1100
- behk
- beg   011
- ad    10
- behl  0100

################################################

step.3 (condition -> new code)
- 1100   - print("new")
- 1111   - if c4:print("new")
- 11111  - c5 = 1; if c5:print("new")
- 0001  
 
if c3:
    pass
else:
    if c4:
        print("new")
          
################################################
        
step.4 (idea -> code) 
- motor ON         

################################################

c1 = 0
c2 = 0
c3 = 0
c4 = 1
c5 = 1

if c1:
    print("a")
    if c2:
        print("c")
        if c3:
            print("i")
            if c4:
                if c5:
                    print("new")


        else:
            print("j")
            if c4:
                print("m")

            else:
                print("n")

    else:
        print("d")

else:
    print("b")
    if c2:
        print("e")
        if c3:
            print("g")

        else:
            print("h")
            if c4:
                print("k")

            else:
                print("l")

    else:
        print("f")
        if c3:
            pass
        else:
            if c4:
                print("new")
                
################################################

1. low   ->   print("water motor ON")
2. full  ->   print("water motor OFF")
                
                
if low_level:
    print("water motor ON")

if full:
    print("water motor OFF")
                
################################################
            
3. low + not short_circuit -> print("water motor ON")                

if low_level:
    if short_circuit:
        pass
    else:
        print("water motor ON")

################################################
                
4. low + electric + short_circuit   -> print("water motor ON")

if low_level:
    if electric:
        if short_circuit:
            pass
        else:
            print("water motor ON")                

################################################

5. low + not electric  -> print("Generator ON")

if low_level:
    if electric:
        if short_circuit:
            pass
        else:
            print("water motor ON")
    else:
        print("Generator ON")

################################################

6. low + not electric + not short_circuit   ->   Generator ON ->   print("water motor ON")

if low_level:
    if electric:
        pass
    else:
        print("Generator ON")
        if short_circuit:
            pass
        else:
            print("water motor.1 ON")

################################################

7. low + electric + short_circuit_1 +  not short_circuit_2     ->   print("water motor.2 ON")
     1      1            1                0

if low_level:
    if electric:
        if short_circuit_1:
            if short_circuit_2:
                pass
            else:
                print("water motor.2 ON")
        else:
            print("water motor.1 ON")
            
################################################

8. low + not electric + short_circuit_1 +  not short_circuit_2     ->   print("water motor.2 ON")

################################################

sensor(2)
- low level       (somthing) (True)
- full            (somthing) (True)
- short circuit   (somthing) (True)

Actuactors
- water motor ON
- water motor OFF

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

"0"  is somthing value.

################################################

low_level = input("low_level = ")
electric = input("electric = ")
short_circuit_1 = input("short_circuit_1 = ")
short_circuit_2 = input("short_circuit_2 = ")
short_circuit_3 = input("short_circuit_3 = ")

print()

if low_level:
    if electric:
        if short_circuit_1:
            print("call mechanic")
            if short_circuit_2:
                print("call mechanic")
                if short_circuit_3:
                    print("call mechanic")
                else:
                    print("water motor.3 ON")
            else:
                print("water motor.2 ON")
        else:
            print("water motor.1 ON")
    else:
        print("Generator ON")
        if short_circuit_1:
            print("call mechanic")
            if short_circuit_2:
                print("call mechanic")
                if short_circuit_3:
                    print("call mechanic")
                else:
                    print("water motor.3 ON")
            else:
                print("water motor.2 ON")
        else:
            print("water motor.1 ON")

################################################################################################

one from many (elif -> else + if)

greater or equal 500, doctor
greater  or equal 400, engineer
greater  or equal 300, distance 

c1 = greater or equal 500
c2 = greater or equal 400
c3 = greater or equal 300

c1, doctor
not c1 and c2, engineer
not c1 and not c2 and c3, distance 
not c1 and not c2 and not c3, online shop

################################################

mark = int(input("Mark = "))

c1 = mark >= 500
c2 = mark >= 400
c3 = mark >= 300


if c1:print("doctor")
if not c1 and c2:print("engineer")
if not c1 and not c2 and c3:print("distance")
if not c1 and not c2 and not c3:print("online shop")

################################################

4      <--

1      <--
2
3      <--

################################################

mark = int(input("Mark = "))

c1 = mark >= 500
c2 = mark >= 400
c3 = mark >= 300


if c1:print("doctor")
elif c2:print("engineer")
elif c3:print("distance")
else:print("online shop")

################################################

mark >= 90    A+
mark >= 80    A
mark >= 70    B
mark >= 50    C
mark < 50     fail


c1 = mark >= 90    
c2 = mark >= 80    
c3 = mark >= 70   
c4 = mark >= 50    
c5 = mark < 50     

c1                              A+
not c1, c2                      A
not c1, notc2, c3               B
not c1, notc2, not c3, c4       C

mark < 50     fail

################################################

# Error sample

if c1:print("A+")       <---    c1                                       A+
elif c3:print("B")      <---    not c1 and c3                            B
elif c2:print("A")      <---    not c1 and not c3 and c2                 A
elif c4:print("D")      <---    not c1 and not c3 and not c2 and c4      C
    
mark = int(input("Mark = "))

c1 = mark >= 90
c2 = mark >= 80
c3 = mark >= 70
c4 = mark >= 50

if c1:print("A+")
elif c3:print("B")
elif c2:print("A")
elif c4:print("C")

################################################

correct sample

c1                              A+
not c1, c2                      A
not c1, notc2, c3               B
not c1, notc2, not c3, c4       C
not c1, notc2, not c3, not c4   fail


mark = int(input("Mark = "))

c1 = mark >= 90
c2 = mark >= 80
c3 = mark >= 70
c4 = mark >= 50
c5 = mark < 50

if c1:print("A+")
elif c2:print("A")
elif c3:print("B")
elif c4:print("C")
else :print("fail")

# elif c5:print("fail")

################################################





"""
