"""
1. Sequence
2. Usages of data types
3. Names of data types   
4. Symbols of data types     1, True, None   
5. Boolean values of empty and anything
6. Mutable, Immutable, Ordered, Unordered
7. Indexing
8. Slicing
9. range
10. Operation, Operator, Operand 
11. Unary operator, Binary operator, Ternary operator
12. Precedence (15)(43)           
13. Associativity (2)(**, u, =)
14. Operator groups( 7 )
15. naming rules
16. Type casting (2)
17. Explicit type casting(21)(14 + c o 2 8 16 r e) 
18. Implicit type casting(2)(float, bool) ( 1+ 1.2, not 1 ) 
19. formatting string (fatr)       
20. Three parts of programmimg 
21. Basic input/output
22. program flow   
23. control flow
24. Arithmetic operators in programming 
25. CLI
26. character code
27. single line string, preformatted string, multiline string, documentation string
28. square root ( exponent 1/2 ), cube root ( exponent 1/3 ) 
29. unicode, uppercase to lowercase  ( A to a )
30. Algorithms, pseudo code

################################################

CLI ( Command Line Interface )

1900 * 1200

x
      .             .
        .         .
           .   .
             .
          .    .
        .        .
      .            .

                                                                     A
################################################

1. Basic input & output (str)
   - input -> prompt letter
   - print -> comma

################################################

x = int(input())

x           label
=           assignment operator 14
int()       integer
input()     receive input string

################################################

2. format(f)

f"Name = {name:fatr}."

################################################

3. character code
   - select the new line = n
   - select the tab = t  (4 space)

y = "\nAge = 20\n\tName = Mg Mg\n\t\tMarks = 100\n\t\t\tRoll No = 1"
print(y)


################################################

'''
Age = 20
    Name = Mg Mg
        Marks = 100
            Roll No = 1
'''

################################################

4. single line string 
   - single quotes, double quotes
   - 'appple', "apple"

################################################

5. preformatted string
6. multiline string  
7. documentation string
   - triple quotes (can encode new lines & tabs)

################################################

8. square root ( exponent 1/2 )       2/1 --> 1/2

4 ** 2 
4 * 4 
16


16 ** (1/2)
4

square root of 16 = 4

################################################

9. cube root ( exponent 1/3 ) 3/1  --> 1/3

4 ** 3
4 * 4 * 4
64

64 ** (1/3)
4

################################################

10. Sequence

Ohm’s Law (Voltage, Current, Resistance)( V = IR )

V = I * R
I = V / R
R = V / I

r = float(input("Resistance = "))
i = float(input("Current = "))
v = i * r

print(f"Voltage = {v}")

print(f"Voltage = {float(input("Current = ")) * float(input("Resistance = "))}")

################################################

1. input("Current = ")
2. float()
3. input("Resistance = ") 
4. float()
5. mul()
6. str()  -> "Voltage = 1.0"
7. print() 

################################################

1. input
2. float
3. assign
4. input
5. float
6. assign
7. mul
8. assign
9. format
10. print

################################################

11. unicode

65       A
97       a
4096     က

################################################

12. character to unicode number (ord(က) -> 4096)
    - ordinal unicode number of a character (ord)

13. unicode number to character (chr(4096) -> က)
    - unicode character (chr) 

################################################

14. uppercase to lowercase  ( A to a )

- unicode of A          65
- unicode of A + 32     97
- unicode number of 'a' to character

"A"  ->  65  + 32  -> 97  ->  "a"

################################################

15. Algorithms 

Algorithm for uppercase to lowercase 
- add 32

Algorithm for lowercase to uppercase
- minus 32

################################################

16. pseudo code

1. unicode of uppercase   
2. unicode of uppercase + 32    
3. unicode number of lowercase to character

################################################

uppercase = ord(input("uppercase = ")) # A   ->  65
lowercase = chr(uppercase + 32)        # 97  ->  a
print("lowercase =", lowercase)

################################################

Algorithm for lowercase to uppercase ( -32 )

- unicode of lowercase   
- unicode of lowercase - 32    
- unicode number of uppercase to character

lowercase = ord(input("lowercase = ")) # a   ->  97
uppercase = chr(lowercase - 32)        # 65  ->  A
print("uppercase =", uppercase)

################################################

Algorithm for A to  က ( + 4031 )

65 to 4096  

################################################################################################

"""
