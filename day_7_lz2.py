
"""

CLI ( Command Line Interface )

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

f"Name = {name}."

################################################

3. character code
   - select the new line = n
   - select the tab = t

y = "\nAge = 20\n\tName = Mg Mg\n\t\tMarks = 100\n"
print(y)

################################################

'''
Age = 20
    Name = Mg Mg
        Marks = 100
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

8. square root ( exponent 1/2 )

4 ** 2 
4 * 4 
16


16 ** (1/2)
4

square root of 16 = 4

################################################

9. cube root ( exponent 1/3 )

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

initial_amount = float(input("Enter initial amount(g): "))
half_life = float(input("Enter half-life (years): "))  # 4.468e9 ( e9 = 1_000_000_000 )
time = float(input("Enter elapsed time (years): "))  # 4_000_000_000
ans = initial_amount * 0.5 ** (time / half_life)
print("Remaining amount:", ans)

################################################

Sequence

1. input("Enter initial amount(g): ")
2. float()
3. assign
4. input("Enter half-life (years): ")
5. float()
6. assign
7. input("Enter elapsed time (years): ")
8. float()
9. assign
10. div -> (time / half_life) 
11. exp -> 0.5 ** div
12. mul -> initial_amount * exp
13. assign
14. print()

################################################

print(f"Remaining amount: {float(input("Enter initial amount(g): ")) * 0.5 ** (float(input("Enter elapsed time (years): ")) / float(input("Enter half-life (years): ")))}" )

################################################

Sequence

1. input("Enter initial amount(g): ")
2. float()
3. input("Enter half-life (years): ")
4. float()
5. input("Enter elapsed time (years): ")
6. float()
7. div -> (time / half_life) 
8. exp -> 0.5 ** div
9. mul -> initial_amount * exp
10. print()

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

################################################

15. Algorithms 

Algorithm for uppercase to lowercase 
- to add 32

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


