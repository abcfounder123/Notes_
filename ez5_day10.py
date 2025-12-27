
"""

Day.10

1. Three parts of programmimg 
2. Basic input/output
3. program flow   
4. control flow

################################################

1. Three parts of programmimg
   - input     (mic)(30 35 60 70 90 120) 
   - processing   ( 60 70 )
   - output    (speaker)                 

################################################

2. Basic input/output (str)
   - input(prompt letter)
   - print(,)

################################################

3. program flow 

1. input()       '90350'
2. int()          90350
3. asssign()

4. floor div()
5. asssign()
6. mod()
7. asssign()

8. floor div()
9. asssign()
10. mod()
11. asssign()

12. floor div()
13. asssign()
14. mod()
16. asssign()

17. format()
18. print()

Day
Hour
Min
Sec

################################################

4. control flow 
Sec
Min

################################################

Associativity
- left-sided bind
- right-sided bind (1, 2, 10, 14, 15)(e, u, assignment)

left
2 ** 2 ** 3
4 ** 3
64

right
2 ** 2 ** 3
2 ** 8
256

left
2 / 2 * 3
1.0 * 3
3

right
2 / 2 * 3
2 / 6
3.333

################################################

e, u, assignment

Exponent      -  1
+, -, ~, not  -  4
13 + 1        - 14

                19

################################################

1 ** 2 + 3 * 4 / 5 - 6 ** 1 

1. r **, l **

>> 1 ** 2 + 3 * 4 / 5 - 6
>> 1 + 3 * 4 / 5 - 6

2. l*, r/

>> 1 + 12 / 5 - 6
>> 1 + 2.4 - 6

3. l+, r-

>> 3.4 - 6
>> - 2.6

################################################

1. CLI
2. character code
3. single line string, preformatted string, multiline string, documentation string
4. square root ( exponent 1/2 ), cube root ( exponent 1/3 ) 
5. unicode, uppercase to lowercase  ( A to a )
6. Algorithms, pseudo code
7. CLI 35

################################################

CLI ( Command Line Interface )

GUI


800 * 600 = 480_000

2000 * 1000 = 2_000_000

500 50
. . . . .       X
. . . . .
. . . . .
. . . . .
. . . . .  5, 5

Y

500

x
      .             .
        .         .
           .   .
             .
          .    .
        .        .
      .            .
                                     
                                                    
################################################

1. Basic input & output (str)
   - input -> prompt letter
   - print -> comma

################################################

x = int(input())

x           identifier, label
=           assignment operator 14
int()       integer
input()     receive input string


x = 5

5  -> int house -> (n=5,str='5' + 74) => Mandalay, 4333981320

x  -> house address 

print(x)


################################################

2. format(f)

f"Name = {name:fatr}."

################################################

3. character code (u0041, u000a, u0009)
   - 'select the new line' character = 10, u000a, n
   - select the tab = t  (4 space)   =  9, u0009, t
   
65 66 -> AB
0x41 0x42 -> AB

\u0041\u000a\u0009\u0042\u000a\u0009\u0009\u0043
A\u000a\u0009B\u000a\u0009\u0009C
A\u000a\u0009B\u000a\u0009\u0009C
A\n\tB\n\t\tC
41 a 9 42 a 9 9 43

A
	B
		C

print("A\u000a\u0009B\u000a\u0009\u0009C")
print("A\n\tB\n\t\tC")

################################################################################################

"""
