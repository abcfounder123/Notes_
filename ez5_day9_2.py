
"""

Arithmetic operators in programming 

f = (c * 9 / 5) + 32
c = (f - 32) * 5 / 9
f = x ** 2 - (2 * x * y) + y ** 2

################################################

floordiv and modulus

          350 sec
      
      5 min    50 sec

350 // 60 = 5 min
350 % 60 = 50 sec
 
################################################

                  90350 sec
                  
            1505 min           50 sec
            
        25 h        5min
     
    1 day   1 h   
        
        
90350 sec = 1day 1h 5min 50sec

s = 90350
m = s // 60     # 1505 min
sec = s % 60    #  50 sec

h = m // 60     # 25 h
min = m % 60    # 5 min

day = h // 24   # 1 day
hour = h % 24   # 1 h

print(f"{day} day, {hour} hour, {min} min {sec} sec")

################################################

s = int(input("Seconds = "))
m = s // 60     # 1505 min
sec = s % 60    #  50 sec

h = m // 60     # 25 h
min = m % 60    # 5 min

day = h // 24   # 1 day
hour = h % 24   # 1 h

print(f"{day} day, {hour} hour, {min} min {sec} sec")

################################################

1day 1h 5min 50sec => 90350 sec

Day => day * 24 * 60 * 60
Hour => h * 60 * 60
Min => m * 60  

total = d + h + m + s

d = int(input("Day = "))
h = int(input("Hour = "))
m = int(input("Minute = "))
s = int(input("Second = "))

sec = (d * 24 * 60 * 60) + (h * 60 * 60) + (m * 60) + s
print(f"{sec} seconds")

################################################################################################

"""

