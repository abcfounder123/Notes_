
"""

1. e           exponent                                           (right)
2. u           unary plus, unary minus, bitwise not (~)
3. * / // %    multiplication, division, floor division, modulus  (left)
4. + -         addition, subtraction                              (left)

5. shift       left shift, right shift  ( <<, >> )
6. AND         Bitwise AND ( & )
7. XOR         Bitwise exclusive OR  ( ^ )
8. OR          Bitwise OR ( | )

9. C           Comparison operators (6)
10. NOT        Logical NOT
11. AND        Logical AND
12. OR         Logical OR

################################################

1. Arithmetics operators - 9
2. Bitwise Operators     - 6
3. Comparison operators  - 6

################################################

Introduction of Bitwise operators.

Bits 

Bits act like a switch.  
Amount of data in computer system.
bit -> bytes -> kilo bytes -> mega bytes

4 bits data => 0100 
-> low     0, 1
-> full    0, 1
-> on      0, 1
-> short circuit 0, 1

bit => bi nary digi t  (0, 1)

################################################

Bitwise Operators (6)

1. Left shift ( << )
2. Right shift ( >> )
3. Bitwise AND
4. Bitwise OR
5. Bitwise XOR
6. Bitwise NOT

################################################

1. Left shift ( << )

 1234 5678
 1111 1111
1111 11110       left   --> 1111 1111 < 1
 111 11110
 
    12345678
    11111111       <<   3
 11111111
    11111000
    
left shift 2 of 4 bits in Python
0100 << 2
    
################################################
 
2. Right shift ( >> )
 
 12345678
 11111111
 011111111      right
 01111111
 
 12345678
 11111111          >>   3
    11111111
 00011111
     

right shift 2 of 4 bits in Python
0100 >> 3
 
################################################

AND, OR, XOR
I want apple and banana. (2)
I want apple or banana.  (1, 2) (boy)
I want apple Xor banana. (1)    (angry bird)

################################################

3. Bitwise AND

---  
      AND  ----  (out)
---

0010
         AND     0010
0011

################################################

4. Bitwise OR

---  
      OR  ----  (out)


 
      OR  ----  (out)
---


---  
      OR  ----  (out)
---

0010
         OR      0011
0011

################################################

5. Bitwise XOR

---  
      XOR  ----  (out)


 
      XOR  ----  (out)
---

0010
         XOR     0001
0011

################################################

6. Bitwise NOT

      NOT  ----  (out)
      
################################################      

left shift
0010 << 1     --->  0100

right shift
0010 >> 1     --->  0001

AND
0010 & 0011   --->  0010

XOR
0010 ^ 0011   --->  0001

OR
0010 | 0011   --->  0011

NOT
~ 1011   ---->   0100

################################################

Comparison operators (6) ( values -> boolean value )
1. equal  ( == )
2. not equal ( != )
3. greater than ( > )
4. less than ( < )
5. greater than or equal ( >= )
6. less than or equal ( <= )

################################################

1 == 1   --->  True
1 != 2   --->  True
2 > 1    --->  True
1 < 2    --->  True

x = 2
y = 2
x >= y   --->  True
x <= y   --->  True

################################################################################################

"""


