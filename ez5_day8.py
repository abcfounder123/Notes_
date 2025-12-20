
"""

Day.8

Python has five rules for naming identifiers(labels).

(one, alpha, number, o, r)

1. An identifier must contain at least one character.
2. The first character of an identifier must be an alphabet or the underscore.
3. The remaining characters may be alphabets, underscores, numbers.
4. Other characters are not permitted.
5. A reserved keyword cannot be used as an identifier.
6. meaningful

################################################

one, alpha, number, o, r

1. one  (at least one character)
2. alpha (alphabet or underscroll)
3. number 
4. o     (other character)
5. r     (reserved keyword name) 35

################################################

import keyword

print(keyword.kwlist)
print(len(keyword.kwlist))

################################################

kwlist = ['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']

35

SyntaxError: invalid syntax

################################################

Type casting (21) (14 + c o 2 8 16 r e)

1. str()

2. int()
3. float()
4. complex()

5. list()
6. tuple()
7. set()
8. frozenst()
9. bytearray()
10. bytes()
11. range()
12. dict()

13. bool()

14. memoryview()

15. chr -> str   eg. chr(65)    =>   'A'
16. ord -> int   eg. ord('A')   =>    65
17. bin -> str  "0b0011"
18. oct -> str  "0o75"
19. hex -> str  "0xa"
20. repr -> str
21. eval -> program output(15 +)

################################################

c o 2 8 16 r e

ordinal number ( first, second )

Unicode

A  =>  65
B  =>  66
a  =>  97
b  =>  98
က =>  4096
ခ  =>  4097
   
################################################

decimal number to str
binary number         ->  bin()
octal number          ->  oct()
hexadecimal number    ->  hex()

################################################

r  (Representation string )   ->   repr()

################################################

e  (Evaluation)              ->   eval()

################################################################################################

"""


