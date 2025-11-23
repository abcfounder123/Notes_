
"""
Day.15 (question)

Celsius to Fahrenheit

################################################

Input Data

test_2024.xlsx
No   Date             Temperature(C)  
1    1.1.2024(6:00)       27              
2    1.1.2024(12:00)      30              
3    1.1.2024(22:00)      29
4.       ...              ...           
5.       ...              ...            
6.       ...              ...             

################################################

Output Data

test_2024_f.xlsx
No   Date             Temperature(C)  Temperature(F)
1    1.1.2024(6:00)       27              80.6
2    1.1.2024(12:00)      30              86.0
3    1.1.2024(22:00)      29              ...
4.       ...              ...             ...
5.       ...              ...             ...
6.       ...              ...             ...

################################################

1. Reading data from excel file

read_excel(file_name)

################################################

2. Checking column data

print(t["Temperature(C)"])

################################################

3. Creating list by column data 
   
list(t["Temperature(C)"])

################################################

4. Creating new column 
 
t["Temperature(F)"] = f

################################################

4. Creating new excel

t.to_excel("test_2024_f.xlsx")

################################################

import pandas

t = pandas.read_excel("test_2024.xlsx")

c = list(t["Temperature(C)"])  # [27, 30, 29]
f = [] 

for celsius in c:
    f.append((celsius * 9 / 5) + 32)

t["Temperature(F)"] = f  # [80.6, 86.0, 84.2]

t.to_excel("test_2024.xlsx")

################################################################################################

"""


