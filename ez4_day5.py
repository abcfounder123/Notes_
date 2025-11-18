
"""

Operators (43)

1. Operation, Operator, Operand

Additional Operation   =>   1 + 2
Additional Operator    =>     +
Left Operand           =>   1
Right Operand          =>   2

2. Unary Operator, Binary Operator, Ternary Operator

3. Precedence (15)

1  +  2  *  3 

Addition
1  +  2  *  3 
3  *  3 
9

Multiplication
1  +  2  *  3
1  +  6
7

################################################

4. Unary plus, Binary plus, Unary minus, Binary minus
   
+ 1     -> positive       (pos)
- 1     -> negative       (neg)

1 + 2   -> Addition       (add)
1 - 2   -> Subtraction    (sub)

################################################

5. Associativity (left, right(e, u))

2 ** 3 ** 4

left-sided bind
2 ** 3 ** 4
8 ** 4
4096

right-sided bind
2 ** 3 ** 4
2 ** 81
2417851639229258349412352

################################################

1.  e    
2.  u    
3.  * / 
4.  + -

1 + 2 // 3 - 4 * 5 / 6 ** 1

6
1. **
2. 
3. // * /
4. + -

1 + 2 // 3 - 4 * 5 / 6 ** 1

1 + 0 - 4 * 5 / 6 

1 + 0 - 20 / 6 

1 + 0 - 3.333 

1 - 3.333 

- 2.333 

################################################

6. Arithmetic Operators (9)

1. Exponentation
2. Unary plus
3. Unary minus
4. Multiplication
5. Division
6. Floor Division
7. Modulus
8. Addition
9. Subtraction 


################################################

7. Bitwise operator (6)

5. Shift (left, right) ( <<, >> )

4 bits

1111 right shift 1  => 1111 >> 1

 0000
 1111
 01111

 0111


1111 left shift 1  => 1111 << 1

 0000
 1111
11110
 
 1110
 
################################################
 
8 bits

01011100 right shift 2 
=> 01011100 >> 2 
=> 00010111

 00000000
 01011100
   01011100
   
 00010111
 
 
01011100 left shift 2 
=> 01011100 << 2
=> 01110000

  00000000
  01011100
01011100   
  01110000  

################################################

I want apple and banana.
I want apple or banana.
I want apple xor banana.

################################################

6. AND ( & )

1    electric 
0    not 

1.....
        AND   ---- 1
1.....     


1011.....
           AND   ---- 0001
0101.....     

1011 & 0101   =>   0001

################################################

7. XOR ( ^ )

1.....
        XOR   ---- 1
0..... 

0.....
        XOR   ---- 1
1..... 

1.....
        XOR   ---- 0
1.....     

0.....
        XOR   ---- 0
0..... 

1011.....
           XOR   ----    1110
0101.....     

1011 ^ 0101   =>   1110

################################################

8. OR  ( | )

1.....
        OR   ---- 1
0..... 

0.....
        OR   ---- 1
1..... 

1.....
        OR   ---- 1
1.....     

0.....
        OR   ---- 0
0..... 

1011.....
           OR   ---- 1111
0101.....     

1011 | 0101   =>   1111

################################################

2. NOT ( ~ )

0101 ----   NOT  ----  1010

~ 0101   =>  1010

################################################

Bitwise operator (6)
1. Left shift
2. Right shift
3. Bitwise AND
4. Bitwise Exclusive OR
5. Bitwise OR
6. Bitwise not             precedence 2

################################################

Summary

1.  e    exponent(**)
2.  u    Unary plus, Unary minus, bitwise not
3.  * / 
4.  + -
5. shift 
6. and
7. xor
8. or

################################################################################################

day.6

9. Comparision operators (6) ( value ) (True, False)
   - equal
   - not equal
   - greater than
   - less than
   - greater than or equal 
   - less than or equal 

x == y
x != y
x > y
x < y

x is greater than or equal to y.
x >= y

################################################

Identity operators (ID)
- is
- is not 

################################################

Membership operator
- in
- not in

################################################

Logical operators (logic value -> True, False)

10. Logical not

11. Logical and

12. Logical or

~ 1 => 0
not True => False

1 & 1 => 1
True and True => True
True or False => True

################################################

13. ternary operator, conditional operator, if else operator

value  if  condition  else    value

greater = n1 if n1 > n2 else n2
smaller = n1 if n1 < n2 else n2
permit = "sell" if age > 18 else "not sell"
exam_result = "pass" if marks >= 40 else "fail"

################################################

14. assignmemt opeators (13)

1. assign ( = )

x = 1
x = 2
x = "apple"
x = True
x = []
fruits = ["apple", "banana", "orange"]

2. exponent and assign  ( **= )

x = 10
x **= 3   => x = 1000

7. add and assign  ( += )

x = 10
x += 2    => x = 12
x += 2    => x = 14
x += 1    => x = 15

################################################

assignmemt opeators (13)

1. =
2. **=
3. *=
4. /=
5. //=
6. %=
7. +=
8. -=
9. <<=
10. >>=
11. &=
12. ^=
13. |=

################################################

15. walrus operator ( := )(assign and use)
    - assign in operation 
    
################################################    
    
group(7)

1. Arithmetic Operators (9)

1. Exponentation
2. Unary plus
3. Unary minus
4. Multiplication
5. Division
6. Floor Division
7. Modulus
8. Addition
9. Subtraction 

################################################

2. Bitwise operator (6)

1. Left shift
2. Right shift
3. Bitwise AND
4. Bitwise Exclusive OR
5. Bitwise OR
6. Bitwise not            

################################################

3. Comparision operators (6) 
   - equal
   - not equal
   - greater than
   - less than
   - greater than or equal 
   - less than or equal 

4. Identity operators (ID)
- is
- is not 

5. Membership operator
- in
- not in

################################################

6. Logical operators 

1. Logical not
2. Logical and
3. Logical or

################################################

7. assignmemt opeators (13)

1. =
2. **=
3. *=
4. /=
5. //=
6. %=
7. +=
8. -=
9. <<=
10. >>=
11. &=
12. ^=
13. |=

################################################

Precedence 15

1.  e   
2.  u    Unary plus, Unary minus, bitwise not
3.  * / 
4.  + -
5. shift 
6. and
7. xor    exclusive
8. or
9. c
10. not
11. and 
12. or
13. t
14. assignmemt
15. walrus


group(7)

1.
2.

3.
4.
5.

6.
7.

################################################################################################

"""

