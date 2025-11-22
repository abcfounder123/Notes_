
"""

Day.13 (elif) (Logical operators in programming)

Logical operators in programming

1. Logical NOT  --> opposite     ( NO, NC) (UA, OA)
2. Logical AND  --> ALL True
3. Logical OR   --> ANY True      (kpay, wave, COD)

1. beer
2. age > 18
3. payment      -> bank account, COD

money -> bank account or COD

order received => 1 and 2 and 3
order received => (beer) and (age > 18) and (bank account or COD)

################################################

list = ["Beer", "Wine", "Alcohol"]
age = 19

item = input("Item name : ")
account = input("Cash from account : ")
cod = input("COD = ")

isbeer = "Beer" in list
is_age = age > 18
payment = account or cod

order_received = isbeer and is_age and payment

if order_received:
    print("Order-receiced. Delivery is on the way.")

else:
    print(f"You can not buy {item}.")
    
################################################ 

order_received = ("Beer" in list) and (age > 18) and (account or cod)

################################################   

list = ["Beer", "Wine", "Alcohol"]
age = 19

item = input("Item name : ")
account = input("Cash from account : ")
cod = input("COD = ")

order_received = ("Beer" in list) and (age > 18) and (account or cod)
# order_received = "Beer" in list and age > 18 and (account or cod)

if order_received:
    print("Order-receiced. Delivery is on the way.")

else:
    print(f"You can not buy {item}.")

################################################

account = kpay or wave or bank1 or b2

################################################

list = ["Beer", "Wine", "Alcohol"]
age = 19

item = input("Item name : ")

kpay = input("Kpay Scan : ")
wave = input("wave Scan : ")
cod = input("COD = ")

if "Beer" in list and age > 18 and (kpay or wave or cod):  # 1 and 2 and 3, payment = kpay or wave or cod
    print("Order-receiced. Delivery is on the way.")

else:
    print(f"You can not buy {item}.")

################################################

under_age Vs over_age

################################################

list = ["Beer", "Wine", "Alcohol"]
under_age = False
over_age = True

item = input("Item name : ")

kpay = input("Kpay Scan : ")
wave = input("wave Scan : ")
cod = input("COD = ")

if "Beer" in list and over_age and (kpay or wave or cod):  # 1 and 2 and 3, payment = kpay or wave or cod
    print("Order-receiced. Delivery is on the way.")

else:
    print(f"You can not buy {item}.")

################################################

Right sided bind = exponent, unary, assignment  (**, =)

################################################

low + electric + not short_circuit       ->   print("water motor ON") 

low = input("Water level sensor (low) : ")
electric = input("Electric : ")
short_circuit = input("Short-circuit : ")

c1 = low
c2 = electric
c3 = not short_circuit

m1 = c1 and c2 and c3

if m1:
    print("water motor ON")

if low and electric and not short_circuit:
    print("water motor ON")
    
################################################    
    
low = input("Water level sensor (low) : ")
electric = input("Electric : ")
short_circuit = input("Short-circuit : ")

if low and electric and not short_circuit:
    print("water motor ON")

if low and not electric and not short_circuit:
    print("Generator ON.")
    print("water motor ON")
    
################################################ 
    
normally closed and normally opened  

normally closed             
Human open  -->  accident

normally opened                      
Human closed --> not accident

################################################ 

# low = input("Water level sensor (low) : ") # normally closed 
low = not input("Water level sensor (low) : ") # normally opened 
electric = input("Electric : ")
short_circuit = input("Short-circuit : ")

if low and electric and not short_circuit:
    print("water motor ON")

################################################################################################  

one from many (elif -> else + if)

greater or equal 500, doctor
greater or equal 400, engineer
greater or equal 300, distance 

c1 = greater or equal 500
c2 = greater or equal 400
c3 = greater or equal 300

c1                              doctor
not c1 and c2                   engineer
not c1 and not c2 and c3        distance 
not c1 and not c2 and not c3    online shop

################################################ 

marks = int(input("Marks : "))

c1 = marks >= 500
c2 = marks >= 400
c3 = marks >= 300

if c1:
    print("Doctor")

if not c1 and c2:
    print("Engineer")

if not c1 and not c2 and c3:
    print("Distance")
    
################################################ 
   
501
1. if 
2. print("Doctor")
3. if2
4. if3

################################################ 

marks = int(input("Marks : "))

c1 = marks >= 500
c2 = marks >= 400
c3 = marks >= 300

if c1:
    print("Doctor")

elif c2:
    print("Engineer")

elif c3:
    print("Distance")


elif => else + if

################################################ 

501
1. if
2. print("Doctor") 

450
1. if
2. elif
3. print("Engineer")

350
1. if
2. elif
3. elif
4. print("Distance")

################################################ 

marks >= 90, A+    ( c1 )
marks >= 80, A     ( not c1, c2 )
marks >= 60, B     ( not c1, not c2, c3 )
marks >= 50, C     ( not c1, not c2, not c3, c4 )


marks >= 60, B     ( not c1, not c2, c3 )
marks >= 90, A+    ( c1 )
marks >= 50, C     ( not c1, not c2, not c3, c4 )
marks >= 80, A     ( not c1, c2 )


marks >= 90, A+    ( c1 )
marks >= 80, A     ( not c1, c2 )
marks >= 60, B     ( not c1, not c2, c3 )
marks >= 50, C     ( not c1, not c2, not c3, c4 )
marks <= 50, F     ( not c1, not c2, not c3, not c4 )

marks = int(input("Marks : "))

if marks >= 90:
    print("A+")

elif marks >= 80:
    print("A")

elif marks >= 60:
    print("B")

elif marks >= 50:
    print("C")

else:
    print("F")
    
################################################################################################

"""

