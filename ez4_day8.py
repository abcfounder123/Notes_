
"""
1. Formatting string (fatr)
2. Arithmetic operators in programming 
3. Three parts of programming
4. Basic input/output ( str )
5. Program flow 
6. Control flow

1. Formatting string (fatr)
   - filled chr (space)
   - alignment(<, >, ^)(left)
   - total chr count
   - round(.2f)
   
BMW-0001
BMW-0002
BMW-0100
BMW-1000

f = 0
a = >
t = 4

n = 8
x = f"BMW-{n:0>4}"
print(x)

################################################
   
-----------------------------------------------------------
|  No  |    Date    |  Temperature(C)  |  Temperature(F)  |
-----------------------------------------------------------
|  1   |  1.1.2025  |       27         |       Na         |
-----------------------------------------------------------
|  2   |  2.1.2025  |       28         |       Na         |
-----------------------------------------------------------
|  3   |  3.1.2025  |       26         |       Na         |
-----------------------------------------------------------


c1 = "No"
c2 = "Date"
c3 = "Temperature(C)"
c4 = "Temperature(F)"

d = [
    [1, "1.1.2025", 27, "Na"],
    [2, "2.1.2025", 28, "Na"],
    [3, "3.1.2025", 26.5082101, "Na"]
]

l = "-" * 59
t = f"|{c1:^6}|{c2:^12}|{c3:^18}|{c4:^18}|"
r1 = f"|{d[0][0]:^6}|{d[0][1]:^12}|{d[0][2]:^18}|{d[0][3]:^18}|"
r2 = f"|{d[1][0]:^6}|{d[1][1]:^12}|{d[1][2]:^18}|{d[1][3]:^18}|"
r3 = f"|{d[2][0]:^6}|{d[2][1]:^12}|{d[2][2]:^18.0f}|{d[2][3]:^18}|"

print(l)

print(t)
print(l)

print(r1)
print(l)

print(r2)
print(l)

print(r3)
print(l)

################################################

2. Arithmetic operators in programming 


formula = x ** 2 + y ** 2

celsius to fahrenheit
f = (c * 9 / 5) + 32
c = (f - 32) * 5 / 9

################################################

floordiv and modulus

        350 seconds
   
 // 5 min      % 50 seconds
   
s = 350
m = s // 60   # 5 min
ms = s % 60   # 50 seconds
ans = f"{m} minutes {ms} seconds"
print(ans)

################################################

             90350  seconds

      h               sec

     25               350
  
   1day  1h       5 min   50 sec

s = 90350
h = s // 3600   # 25 h
ms = s % 3600   # 350 sec

min = ms // 60  # 5 min
ms2 = ms % 60   # 50 sec

d = h // 24     # 1 day
h2 = h % 24     # 1 hour

ans = f"{d} days, {h2} hours, {min} minutes, {ms2} seconds"
print(ans)

################################################

3. Three parts of programming 
- input           (mic) (30 35 60 70)
- processing      (30 to 70)
- output          (speaker)

################################################

4. Basic input/output ( str )
- input (prompt)
- print ( , )

################################################

5. Program flow  

1. input()
2. int()           float()
3. assign()

4. floordiv()
5. assign()
6. mod()
7. assign()

8. floordiv()
9. assign()
10. mod()
11. assign()

12. floordiv()
13. assign()
14. mod()
15. assign()

16. format()
17. assign()

18. print()

################################################

6. Control flow

s = float(input("Seconds = "))
h = s // 3600   # 25 h
ms = s % 3600   # 350 sec

min = ms // 60  # 5 min
ms2 = ms % 60   # 50 sec

d = h // 24     # 1 day
h2 = h % 24     # 1 hour

ans = f"{d} days, {h2} hours, {min} minutes, {ms2} seconds"
print(ans)

################################################################################################

"""

