
"""

Operator (43)

1. Operation, Operator, Operand

1 + 2

Operation = Additional operation
Operator  =  + additional operator
Operand   
- lelt operand = 1
- right operand = 2

#################################################

2. Types of operators (3)
   - unary operator   (right)
   - binary operator  (left, right)
   - ternary operator (left, middle, right)
   
#################################################

3. Positive, Negative, Addition, Substraction

+ 1         <---   pos, unary plus
- 1         <---   neg, unary minus
1 + 2       <---   add, binary plus
2 - 1       <---   sub, binary minus
   
1 - 2 + - 1

#################################################

4. Precedence (15)


1 + 2 * 3

add
1 + 2 * 3
    3 * 3
        9

mul
1 + 2 * 3
1 + 6
7

#################################################

1. e   exponent           **
2. u   unary operators    +1, -1
3. */  ...                *, /, //, %
4. +-                     +, -

#################################################

Arithmetic Operators 9

1. Exponent
2. Unary plus, 
3. Unary minus
4. Multiplication
5. Division
6. Floor division 
7. Modulus
8. Addition
9. Substraction

#################################################

5. shift
6. and
7. xor 
8. or

9. c
10. not
11. and 
12. or

#################################################

Bitwise operators (6)

1. Left shift
2. Right shift
3. Bitwise AND 
4. Bitwise Exclusive 
5. Bitwise OR
6. Bitwise NOT 

#################################################

Bitwise 
Bit => binary digit => 0011

#################################################

1. Left shift

1111 << 1       --->  1110 
1111 << 2       --->  1100

   0000
   1111
  1111
   1110

#################################################
   
2. Right shift

1111 >> 1       --->  0111
1111 >> 2       --->  0011

   0000
   1111
    1111
   0111

#################################################

I want apple and banana.
I want apple or banana.
I want apple exclusive or banana.

#################################################

3. Bitwise AND (&) (two wires)

1 ----
        AND ---- 1
1 ----

0 ----
        AND ---- 0
1 ----

1 ----
        AND ---- 0
0 ----

0 ----
        AND ---- 0
0 ----

0101 ----
          AND ----  0001
0011 ----

0101 & 0011  => 0001

#################################################

5. Bitwise OR (|) (one wire)

1 ----
        OR ---- 1
1 ----

0 ----
        OR ---- 1
1 ----

1 ----
        OR ---- 1
0 ----

0 ----
        OR ---- 0
0 ----

0101 ----
          OR ----  0111
0011 ----

0101 | 0011  => 0111

#################################################

4. Bitwise Exclusive (^) (only one wire)

1 ----
        XOR ---- 0
1 ----

0 ----
        XOR ---- 1
1 ----

1 ----
        XOR ---- 1
0 ----

0 ----
        XOR ---- 0
0 ----

0101 ----
          XOR ----  0110
0011 ----

0101 ^ 0011  => 0110

#################################################

6. Bitwise NOT (~)

1 ---- NOT  ---- 0
0 ---- NOT  ---- 1
0011 ---- NOT  ---- 1100

~ 0011  => 1100

#################################################

1. e
2. u       +1, -1, ~
3. */
4. +-


5. shift
6. and         bitwise
7. xor 
8. or

9. C
10. not
11. and
12. or

#################################################

Comparison operators.6 (equal, greater)(boolean value)

1. Equal                    ==
2. Not equal                !=
3. Greater than             >
4. Less than                <
5. Greater than or equal    >=
6. less than or equal       <=

#################################################

Identity operator(2)(same object)
- is
- is not

#################################################

Membership operator (2)
- in
- not in

#################################################

Logical operator (2) (logical value)(boolean value)(True, False)
- not
- and
- or

#################################################

Ternary operator, if else operator, conditional operator
- left operand, right operand, middle operand

mark = 50

exam_result_1 = "pass" if mark >= 40 else "fail"
exam_result_2 = "fail" if mark < 40 else "pass"

#################################################

Assignment operator ( 13 )

1. Normal assign ( = )

2. exponent and assign ( **= )
3. multiply and assign ( *= )
4. division and assign ( /= )
5. floor division and assign ( //= )
6. modulus and assign ( %= )
7. add and assign ( += )
8. substract and assign ( -= )

9. left shift and assign ( <<= )
10. right shift and assign ( >>= )
11. bitwise AND and assign ( &= )
12. bitwise XOR and assign ( ^= )
13. bitwise OR and assign ( |= )

#################################################

Walrul operator  ( := )
 - assign in operation (operation and assign)

#################################################

1. e                                    
2. u       +1, -1, ~                       
3. */ 
4. +-

5. shift
6. and         bitwise
7. xor 
8. or                       

9. C           C, I, M
10. not        logical                 
11. and
12. or

13. t
14. assignment                           
15. walrul         :=                    

#################################################

1. Arithmetic Operators(9)
2. Bitwise operators (6)
3. Comparison operators (6)
4. Identity operator (2)
5. Membership operator (2)
6. Logical operator (2)
7. conditional operator(1)
8. assignment operator (14)
      
#################################################

Unary operator (4)
Binary operator (38)
Ternary operator (1)

#################################################

5. Associativity
   - Left-sided bind  ( - )
   - Right-sided bind (e, u, assign)

Left-sided bind
2 ** 2 ** 3
     4 ** 3
         64

Right-sided bind
2 ** 2 ** 3
2 ** 8
256

#################################################

Precedence(15)
Associativity(e, u, assign)

##################################################################################################

"""
