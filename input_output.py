"""
19. formatting string (fatr)
20. Three parts of programmimg 
21. Basic input/output
22. program flow   
23. control flow
24. Arithmetic operators in programming 

################################################

19. formatting string (fatr)
   - filled chr (space)
   - alignment(<, >, ^)(left)
   - total chr count
   - round(.2f)
   
-----------------------------------------------------------
|  No  |    Date    |  Temperature(C)  |  Temperature(F)  |
-----------------------------------------------------------
|  1.  |  1.1.2025  |       27         |       Na         |
-----------------------------------------------------------
|  2.  |  2.1.2025  |       28         |       Na         |
-----------------------------------------------------------
|  1.  |  3.1.2025  |       26         |       Na         |
-----------------------------------------------------------
 

t = ["No", "Date", "Temperature(C)", "Temperature(F)"]
x = [('1.', '1.1.2025', 27, 'Na' ), ('2.', '2.1.2025', 28, 'Na' ), ('3.', '3.1.2025', 26, 'Na' )]

l = "-" * 59
f1 = f"|{t[0]:^6}|{t[1]:^12}|{t[2]:^18}|{t[3]:^18}|"
f2 = f"|{x[0][0]:^6}|{x[0][1]:^12}|{x[0][2]:^18}|{x[0][3]:^18}|"
f3 = f"|{x[1][0]:^6}|{x[1][1]:^12}|{x[1][2]:^18}|{x[1][3]:^18}|"
f4 = f"|{x[2][0]:^6}|{x[2][1]:^12}|{x[2][2]:^18}|{x[2][3]:^18}|"

print(l)
print(f1)
print(l)
print(f2)
print(l)
print(f3)
print(l)
print(f4)
print(l)

################################################################################################

20. Three parts of programmimg 

1. input (various, everywhere) (str)
2. processing       <---
3. output (various, everywhere) (str)

################################################

21. Basic input/output

- input()   -->  prompt letter
- print()   -->  ,

################################################

22. program flow    

1. input()       <-  data input
2. int()         <-  processing 
3. assign()
4. floordiv() 
5. assign()
6. modulus()
7. assign()
8. floordiv()  
9. assign()
10. modulus()
11. assign()
12. print()     <-  data output 

################################################

23. control flow

p2  p4(p6)
p1(p5)
p3

program flow -> 264513

control flow -> 246153

p2  p6(p4)
p5(p1)
p3

################################################

24. Arithmetic operators in programming 

          90350 seconds
        
    25 h            350 sec 
          
               5 min      50 sec
               
90350 seconds =  25 h   5 min   50 sec  

################################################

360 sec = 5 minutes 60 seconds
25 h = 1 day 1 hour
366 d = 1 year 1 day

################################################

s = int(input("Total seconds = ")) # int("90350") -> 90350

h = s // 3600 # 25 h
ms = s % 3600 # 350 sec

m = ms // 60 # 5 min
mms = ms % 60 # 50 sec

d = h // 24 # 1 day
mh = h % 24 # 1 hour

y = d // 365
md = d % 365

print(f"{y} Years, {md} Days, {mh} Hours, {m} Minutes and {mms} Seconds")

################################################

25 h, 5 min, 50 sec
>> 25 * 3600 + 5 * 60 +  50 
>> 90000 + 300 + 50 
>> 90350 sec

################################################

input data ->  days, hours, minutes, seconds  

1. input
2. int
3. input
4. int
5. input
6. int
7. input
8. int
9. precedence, associativity
10. print


d = int(input("Day = "))
h = int(input("Hour = "))
m = int(input("Minute = "))
s = int(input("Seconds = "))

sec = (d * 24 * 3600) + (h * 3600) + (m * 60) + s

print(f"{d} Days, {h} Hours, {m} Minutes and {s} Seconds is {sec} seconds.")

################################################

import calendar

calendar.prcal(2025, m=4)

                                              2025

      January                   February                   March                     April
Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su
       1  2  3  4  5                      1  2                      1  2          1  2  3  4  5  6
 6  7  8  9 10 11 12       3  4  5  6  7  8  9       3  4  5  6  7  8  9       7  8  9 10 11 12 13
13 14 15 16 17 18 19      10 11 12 13 14 15 16      10 11 12 13 14 15 16      14 15 16 17 18 19 20
20 21 22 23 24 25 26      17 18 19 20 21 22 23      17 18 19 20 21 22 23      21 22 23 24 25 26 27
27 28 29 30 31            24 25 26 27 28            24 25 26 27 28 29 30      28 29 30
                                                    31

        May                       June                      July                     August
Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su
          1  2  3  4                         1          1  2  3  4  5  6                   1  2  3
 5  6  7  8  9 10 11       2  3  4  5  6  7  8       7  8  9 10 11 12 13       4  5  6  7  8  9 10
12 13 14 15 16 17 18       9 10 11 12 13 14 15      14 15 16 17 18 19 20      11 12 13 14 15 16 17
19 20 21 22 23 24 25      16 17 18 19 20 21 22      21 22 23 24 25 26 27      18 19 20 21 22 23 24
26 27 28 29 30 31         23 24 25 26 27 28 29      28 29 30 31               25 26 27 28 29 30 31
                          30

     September                  October                   November                  December
Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su
 1  2  3  4  5  6  7             1  2  3  4  5                      1  2       1  2  3  4  5  6  7
 8  9 10 11 12 13 14       6  7  8  9 10 11 12       3  4  5  6  7  8  9       8  9 10 11 12 13 14
15 16 17 18 19 20 21      13 14 15 16 17 18 19      10 11 12 13 14 15 16      15 16 17 18 19 20 21
22 23 24 25 26 27 28      20 21 22 23 24 25 26      17 18 19 20 21 22 23      22 23 24 25 26 27 28
29 30                     27 28 29 30 31            24 25 26 27 28 29 30      29 30 31


################################################################################################

"""

