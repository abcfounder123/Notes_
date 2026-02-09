
"""

OOP

Attributes

Inheritance
- parent and child 
- code reuse
        
Type of inheritance
1. Single inheritance 
2. Multiple inheritance
3. Mutilevel inheritance 
4. Hierarchical inheritance
5. Hybrid inheritance

#################################################

1. Single inheritance

       Animal  

         |
         
        Dog
        
 
        
class Animal:
    def eat(self):
        print("Animal eat.")


class Dog:
    def eat(self):
        print("Animal eat.")
        
    def bark(self):
        print("Dog bark.")


#################################################


class Animal:
    def eat(self):
        print("Animal eat.")


class Dog(Animal):
    def bark(self):
        print("Dog bark.")


x = Dog()
x.eat()
x.bark()

#################################################

2. Multiple inheritance  

          Father   Mother
             \\     /
               Child


      old.1  old.2  old.3  old.4  old.5  old.6  old.7    =>  700
          \\           |             /             /
       
                     New                                 => old 400 + 300    = 700


class New(old.1, old.3, old.5, old.7):
    + 300
    pass

#################################################

class Phone:
    def call(self, number):
        print("Calling to ", number)
        
        
class Camera:
    def take_photo(self):
        print("Taking aa photo.")
        
        
class SmartPhone:
    def call(self, number):
        print("Calling to ", number)
        
    def take_photo(self):
        print("Taking aa photo.")

#################################################


class Phone:
    def call(self, number):
        print("Calling to ", number)


class Camera:
    def take_photo(self):
        print("Taking aa photo.")


class SmartPhone(Phone, Camera):
    pass


y = Phone()
y.call("09123456")

z = Camera()
z.take_photo()

x = SmartPhone()
x.call("09123456")
x.take_photo()

#################################################

3. Mutilevel inheritance

          Grand X  x
            |
         Parent Y  y     Single inheritance
            |
          Child Z  z     Mutilevel inheritance
         

class X:
    def x(self):
        print("x")


class Y(X):
    def y(self):
        print("y")


class Z(Y):
    def z(self):
        print("z")


a = Z()
a.x()
a.y()
a.x()

#################################################

4. Hierarchical inheritance

            X          eat .1
         
         /     \\
         
      Y           Z
     bark        meow
      
         

class Animal:
    def eat(self):
        print("Animal eat.")


class Dog:
    def eat(self):
        print("Animal eat.")
        
    def bark(self):
        print("Dog bark.")


class Cat:
    def eat(self):
        print("Animal eat.")
        
    def meow(self):
        print("Cat meow.")
        
        
#################################################

class Animal:
    def eat(self):
        print("Animal eat.")


class Dog(Animal):
    def bark(self):
        print("Dog bark.")


class Cat(Animal):
    def meow(self):
        print("Cat meow.")

x = Dog()
x.eat()
x.bark()

#################################################

            X  
         
         /     \\
         
      Y           Z
    


class X:
    pass


class Y(X):
    pass


class Z(X):
    pass


#################################################

5. Hybrid inheritance

              A       Hierarchical inheritance
              
           /     \\
           
          B        C      single
          
           \\     /
           
               D      Hybrid


D(B, C)            (multiple)
D <- B <- A        (multilevel)
D <- C <- A        (multilevel)


################################################################################################## 

inheritance exercise

11. Jet လေယာဉ်တွင် တိုက်ခိုက်မှုအမျိုးအစား ၊ အမည်နှင့် ထုတ်လုပ်သောနိုင်ငံဟူသော အချက်အလက်ပါရှိသည်။

( role, name, country )

F35 နှင့် F22 သည် Jet လေယာဉ်ဖြစ်သည်။ ( is , has ) ( is a relation ) (tightly coupled) (inheritance) 

       Jet
     /     \
   F35     f22

#################################################

Jet လေယာဉ်တွင် တိုက်ခိုက်မှုအမျိုးအစား ၊ အမည်နှင့် ထုတ်လုပ်သောနိုင်ငံဟူသော အချက်အလက်ပါရှိသည်။

name --> Jet
data -->  role, name, country
method -->

class Jet:
    def __init__(self, role, name, country):
        self.role = role
        self.name = name
        self.country = country
        
        

# F35 သည် Jet လေယာဉ်ဖြစ်သည်။
class F35(Jet):
    pass

# F22 သည် Jet လေယာဉ်ဖြစ်သည်။
class F22(Jet):
    pass

#################################################
                 
                  car
                  

             engine    battry


                      A
                      |
                      B
                      |
                      C

parent class, super class, base class
child class, sub class, derived class

#################################################

12.
I, J, K သည် A ၏ sub class ဖြစ်သည်။
X သည် I ၏ sub class ဖြစ်သည်။
Y သည် J ၏ sub class ဖြစ်သည်။
Z သည် K ၏ sub class ဖြစ်သည်။
ပုံဆွဲပါ။
class တည်ဆောက်ပါ။

               A
               
           /   |   \\

        I      J      K
        
      /        |       \\
       
    X          Y         Z
        


class A:
    pass


class I(A):
    pass
    
    
class J(A):
    pass


class K(A):
    pass


class X(I):
    pass


class Y(J):
    pass


class Z(K):
    pass


#################################################

13.  အောက်ပါပုံအတိုင်း class တည်ဆောက်ပါ။
                      

                      Fruit            x
                      
              /         |        \\
                    
         Apple        Mango       Banana  
         
                  /     |     \\
                  
             မချစ်စု   စိန်တလုံး   တောသရက်
          
          
class Fruit:
    pass


class Apple(Fruit):
    pass


class Mango(Fruit):
    pass


class Banana(Fruit):
    pass


class မချစ်စု(Mango):
    pass


class စိန်တလုံး(Mango):
    pass


class တောသရက်(Mango):
    pass


#################################################

multiple inheritance exercises

14. ပန်းသီးနှင့် သစ်တော်သီးသည် သစ်သီးများဖြစ်ကြသည်။

ပန်းသစ်တော်သီးသည် ပန်းသီးနှင့် သစ်တော်သီးနှစ်မျိုးလုံးမှ မျိုးဗီဇများ အမွေဆက်ခံထားသည်။
 
ထို့ကြောင့် ပန်းသစ်တော်သီးသည် ပန်းသီးလည်း ဖြစ်သလို သစ်တော်သီးလည်းဖြစ်သည်။

ပုံဆွဲပြီး class တည်ဆောက်ပါ။


                       သစ်သီး

                     /        \\
                    
                ပန်းသီး           သစ်တော်သီး
                
                    \\          /
                 
                     ပန်းသစ်တော်သီး    


class သစ်သီး:
    pass


class ပန်းသီး(သစ်သီး):
    color = "white"
    pass


class သစ်တော်သီး(သစ်သီး):
    taste = "sweet"
    pass


class ပန်းသစ်တော်သီး(ပန်းသီး, သစ်တော်သီး):
    pass



x = ပန်းသစ်တော်သီး()
print(x.color)
print(x.taste)

#################################################

15.
A, B သည် Y ဖြစ်သည်။
C, D, E သည် Z ဖြစ်သည်။
X သည် A, B, C, D, E, F ဖြစ်သည်။
ပုံဆွဲပြီး class တည်ဆောက်ပါ။

#################################################

A, B သည် Y ဖြစ်သည်။

                    Y
                   
                 /     \\

               A           B
               
               
C, D, E သည် Z ဖြစ်သည်။               
               

                    Z
                   
                 /   |  \\

               C     D     E
               
                              
X သည် A, B, C, D, E, F ဖြစ်သည်။

               
               A    B   C   D   E   F
               
                \\   \\ |  /  /  /
                
                        X

#################################################


               Y          Z             
                   
             /  \\     /  |  \\    

             A    B    C   D   E   F

               \\   \\ |  /  /  /
               
                  \\ \\| / / /
            
                       X
                        
#################################################

class Y:
    pass
class Z:
    pass
class F:
    pass

class A(Y):
    pass
class B(Y):
    pass

class C(Z):
    pass
class D(Z):
    pass
class E(Z):
    pass

class X(A, B, C, D, E, F):
    pass

print(X.__mro__)  # X  ABY CDEZ F

#################################################

16. X ၏ attributes ကို ရှာဖွေပါက မည့်သည့်အစီအစဉ်အတိုင်း ရှာဖွေမည်နည်း။

               Y         Z
                   
             /  \\    /  |  \\

             A   B   C   D   E    F

               \\   \\ |  /  /  /
               
                  \\ \\| / / /
            
                       X      
                       
Method Resolution Order = X ->  A -> B -> Y  -> C -> D -> E -> Z  -> F


class Y:
    a = "Y"
    pass
class Z:
    a = "Z"
    pass

class A(Y):
    a = "A"
    pass
class B(Y):
    a = "B"
    pass

class C(Z):
    a = "C"
    pass
class D(Z):
    a = "D"
    pass
class E(Z):
    a = "E"
    pass

class F:
    a = "F"
    pass

class X(A, B, C, D, E, F):
    a = "X"
    pass


print(X.a) # X

#################################################

17. Method Resolution Order Exercise.1  => X BAY CDEZ F

               Y          Z             
                   
             /  \\     /  |  \\    

             B    A    C   D   E   F

               \\   \\ |  /  /  /
               
                  \\ \\| / / /
            
                       X


class X(B, A, C, D, E, F):
    pass

#################################################
                  
18. Method Resolution Order Exercise.2  => X CDEZ ABY F   
   
                Z             Y   
                   
             /  |  \\        / \

            C   D     E     A   B   F

             \\   \\   |   /  /  /
               
                  \\ \\| / / /
            
                       X


class X(C, D, E, A, B, F):
    pass


#################################################

19. Method Resolution Order Exercise.3  => X F CDEZ ABY

                 Z             Y   
                   
              /  |  \\        / \

       F    C    D     E     A   B  

         \\    \\   \\   |   /  /  
               
              \\   \\ \\| / / 
            
                       X

class Y:
    pass
class Z:
    pass
class F:
    pass

class A(Y):
    pass
class B(Y):
    pass

class C(Z):
    pass
class D(Z):
    pass
class E(Z):
    pass

class X(F, C, D, E, A, B):
    pass

print(X.__mro__)              
            
#################################################

20. Method Resolution Order Exercise.4  

=> Cross diamond example
=> X  A C BY DEZ F 

       
               Y        Z
                
              /    X    |  \\

             A   C   B  D   E    F

               \\   \\  |  /  /  /
               
                  \\ \\ | / / /
            
                        X       
 
 
class X(A, C, B, D, E, F):
    pass


#################################################

"""


# A consistent method resolution order (MRO)

#                 Y

#            A   /\   B
#                \/

#                 X

# A, B သည် Y ဖြစ်သည်။
# X သည် A, B ဖြစ်သည်။  (A, B, Y)

#################################################

# Not a consistent method resolution order (MRO)

#                 Y
#              /

#          /    /   \
#             A      B
#          \    \   /
#            \
#              \
#                 X


# X သည် Y, A, B ဖြစ်သည်။ (Diamond problem ) (Y, A, B, Y)
# TypeError: Cannot create a consistent method resolution order (MRO)

#################################################

"""

class Y:
    pass
class Z:
    pass
class F:
    pass

class A(Y):
    pass
class B(Y):
    pass

class C(Z):
    pass
class D(Z):
    pass
class E(Z):
    pass

class X(Y, A, B, C, D, E, F):
    pass


print(X.__mro__)                
         
#################################################

21. Method Resolution Order Exercise.5  

=> G is Y.
=> X is G.
=> X AGBY CDEZ F

Y
|
G      <---
|
X

               Y         Z
                   
             / | \\    /  |  \\

             A G  B   C   D   E    F

               \\   \\ |  /  /  /
               
                  \\ \\| / / /
            
                       X       

MRO -> XAGBYCDEZF

class X(A, G, B, C, D, E, F):

#################################################

22. Method Resolution Order Exercise.6  

=> H is Z.
=> X is H.
=> X AGBY CHDEZ F

Z
|
H    <---
|
X  

"""
#              Y              Z
                   
#             / | \       / / | \

#             A G  B    C H  D   E  F

#               \ \ \   | | /  /  /
               
#                  \ \\ | |/ / /
            
#                        X

"""


class X(A, G, B, C, H, D, E, F):
    pass


#################################################

23. Method Resolution Order Exercise.7  
  
=> X is I.
=> X AGBY CHDEZ F I

  I
  |
  X
  

"""
#              Y              Z

#             / | \       / / | \

#             A G  B    C H  D  E   F  I

#               \ \ \   | | /  /  / /

#                  \ \\ | |/ /  / /

#                        X


"""


class X(A, G, B, C, H, D, H, E, F, I):
    pass


#################################################

24. Method Resolution Order Exercise.8  
  
=> X is J.
=> X J AGBY CHDEZ F I

  J
  |
  X
  

"""
#              Y              Z

#             / | \       / / | \

#         J  A G  B     C H  D  E   F  I

#           \   \ \ \   | | /  /  / /

#               \  \ \\ | |/ /  / /

#                        X


"""


class X(X, J, A, G, B, C, H, D, E, Z, F, I):
    pass


#################################################

25. Method Resolution Order Exercise.9 
  
=> All is K.

                     K
                     

                /      \\     \\
                
               Y         Z
                   
             /  \\    /  |  \\  \\

             A   B   C   D   E    F

               \\   \\ |  /  /  /
               
                  \\ \\| / / /
            
                       X   
                       

#################################################

class K:
    a = "K"
    pass
    
class Y(K):
    pass
class Z(K):
    pass
class F(K):
    pass

class A(Y):
    pass
class B(Y):
    pass

class C(Z):
    pass
class D(Z):
    pass
class E(Z):
    pass

class X(A, B, C, D, E, F):  
    pass

print(D.a) 

#################################################

26. What should be Class level data?

50 millions people

1. Name       -  obj    =>   500 millions   =>  500 MB
2. ID         -  obj    =>   500 millions   =>  500 MB
3. age        -  obj    =>   500 millions   =>  500 MB 
4. "Myanmar"  -  obj    =>   500 millions   =>  500 MB 
                                            +   2000 MB
                                             

1. Name       -  obj    =>   500 millions   =>  500 MB
2. ID         -  obj    =>   500 millions   =>  500 MB
3. age        -  obj    =>   500 millions   =>  500 MB 
4. "Myanmar"  -  cls           1            =>  100 bytes 

                                            +   1500 MB + 100 bytes 

#################################################


class X:
    def __init__(self, name, id, age, country):
        self.name = name
        self.id = id
        self.age = age 
        self.country = country


p1 = X(name="p1", id="000000001", age=20, country="Myanmar")
p2 = X(name="p2", id="000000002", age=20, country="Myanmar")

print(p1.__dict__)
print(p2.__dict__)

print(p1.country)
print(p2.country)

p1.country = "Burma"
p2.country = "Burma"

print(p1.country)
print(p2.country)

#################################################

{'name': 'p1', 'id': '000000001', 'age': 20, 'country': 'Myanmar'}        400 bytes
{'name': 'p2', 'id': '000000002', 'age': 20, 'country': 'Myanmar'}        400 bytes


p1 = X(name="p1", id="000000001", age=20, country="Myanmar")              create for every obj
p2 = X(name="p2", id="000000002", age=20, country="Myanmar")              create for every obj

"Myanmar"  -  obj    =>   500 millions   =>  500 MB                       much memory usage

p1.country = "Burma"                                                      update for every obj
p2.country = "Burma"                                                      update for every obj

#################################################


class X:
    country = "Myanmar"  # class level data

    def __init__(self, name, id, age):
        self.name = name
        self.id = id
        self.age = age 


p1 = X(name="p1", id="000000001", age=20)
p2 = X(name="p2", id="000000002", age=20)

print(p1.__dict__)
print(p2.__dict__)

print(p1.country)
print(p2.country)

X.country = "Burma"

print(p1.country)
print(p2.country)

#################################################

{'name': 'p1', 'id': '000000001', 'age': 20}         300 bytes
{'name': 'p2', 'id': '000000002', 'age': 20}         300 bytes

country = "Myanmar"  =>  100 bytes                   create once, less memory usage

X.country = "Burma"                                  update once

#################################################

27. Use inheritance for the following code.


class Male:
    gender = "male"
    country = "Myanmar"
    percedence = "U Ba"
    system = "Democracy"

    def __init__(self, id, name, age):
        self.id = id
        self.name = name
        self.age = age


class Female:
    gender = "female"
    country = "Myanmar"
    percedence = "U Ba"
    system = "Democracy"

    def __init__(self, id, name, age):
        self.id = id
        self.name = name
        self.age = age


#################################################


class X:
    country = "Myanmar"
    percedence = "U Ba"
    system = "Democracy"

    def __init__(self, id, name, age):
        self.id = id
        self.name = name
        self.age = age


class Male(X):
    gender = "male"


class Female(X):
    gender = "female"


#################################################

p1 = Male(id="123456789", name="Mg Mg", age=20)
print(p1.gender)
print(p1.country)

#################################################

28. Create relations for the following classes.

Myanmar Human
Yangon Human
Mandalay Human
America Human
Newyork Human
Human

                              Human (head=1)
                                
                            /                  \\

            Myanmar Human                        America Human

           /        \\                                \\
           
   Yangon Human   Mandalay Human                      Newyork Human


800 billions , 600 bytes, 100 bytes

#################################################

29. Create relations for the following classes.

Car
Engine Car
Electric Car
Diesel Car
Petrol Car
                       
                       Car
                       
                    /       \\
                   
           Engine Car         Electric Car
           
           /    \\

   Diesel Car     Petrol Car

#################################################

30. Draw MRO for the following relations.

A is a F.    (ပန်းသီး is a Fruit.)
T is a F.    (သစ်တော်သီး is a Fruit.)
O is a F.    (Orange is a Fruit.)

AT is a A.   (ပန်းသစ်တော်သီးသည် ပန်းသီးဖြစ်သည်။)
AT is a T.   (ပန်းသစ်တော်သီးသည် သစ်တော်သီးဖြစ်သည်။)
(ပန်းသစ်တော်သီးသည် ပန်းသီးလည်း ဖြစ်သလို သစ်တော်သီးလည်းဖြစ်သည်။)

O1 is a O.
O2 is a O.
O3 is a O.
                             F
                             
                         /   |   \\
                                
                        A    T       O
                        
                        \   /     /  |  \\
                        
                          AT    O1  O2   O3
                          
#################################################

Knowledges

1. comma + space
2. operator => s + operator +  s
3. fun, class  => line 2
4. while, if, for  =>  line 1
5. normal program  =>  no line, line 1

6. Diamond problam (YAB => YABY)
7. MRO

##################################################################################################

"""



