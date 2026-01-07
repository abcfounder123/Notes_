
"""

Inheritance exercise

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


                 Y       Z
                   
             /  \\    /  |  \\

             A   B   C   D   E    F

               \\   \\ |  /  /  /
               
                  \\ \\| / / /
            
                       X
                        
#################################################

                 Y
              
            A   /\\   B
                \\/
             
                 X
                 
                 
             
               Y         Z
                   
             /  \\    /  |  \\

             A   B   C   D   E    F

               \\   \\ |  /  /  /
               
                  \\ \\| / / /
            
                       X       a


MRO (method resolution order)
<class '__main__.X'>, 
<class '__main__.A'>, <class '__main__.B'>, <class '__main__.Y'>, 
<class '__main__.C'>, <class '__main__.D'>, <class '__main__.E'>, <class '__main__.Z'>, 
<class '__main__.F'>, 

<class 'object'>

class X(A, B, C, D, E, F):

class X(A, B, Y, C, D, E, Z, F):

Diamond Problem -> Cannot create a consistent MRO
class X(Y, A, B, Y, C, D, E, Z, F)

#################################################

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

16. X ၏ attributes ကို ရှာဖွေပါက မည့်သည့်အစီအစဉ်အတိုင်းရှာဖွေမည်နည်း။

               Y         Z
                   
             /  \\    /  |  \\

             A   B   C   D   E    F

               \\   \\ |  /  /  /
               
                  \\ \\| / / /
            
                       X       a
                       
နမူနာ အဖြေ
Method Resolution Order = X ->  A -> B -> Y  -> C -> D -> E -> Z  -> F

#################################################

               Y         Z
                   
             /  \\    /  |  \\

             A G  B   C   D   E    F

               \\   \\ |  /  /  /
               
                  \\ \\| / / /
            
                       X       a


Y
|
G
|
X

MRO -> XAGBYCDEZF

class X(A, G, B, C, D, E, F):

#################################################

              Y         Z
                   
             /  \\    /  |  \\

             A G  B   C H  D   E    F   

               \\   \\ |  /  /  /
               
                  \\ \\| / / /
            
                       X   
Z
|
H
|
X                          
MRO -> XAGBYCHDEZF

#################################################

              Y         Z
                   
             /  \\    /  |  \\

            A G  B   C H  D   E    F   I

               \\   \\ |  /  /  /
               
                  \\ \\| / / /
            
                       X   

I

MRO -> XAGBYCHDEZFI

#################################################

J
MRO -> XJAGBYCHDEZFI


              Y         Z
                   
             /  \\    /  |  \\

       J     A G  B   C H  D   E    F   I

               \\   \\ |  /  /  /
               
                  \\ \\| / / /
            
                       X   

#################################################

class J:
    pass
class Y:
    a = "Y"
    pass
class Z:
    a = "Z"
    pass
class F:
    a = "F"
    pass

class A(Y):
    a = "A"
    pass
class G(Y):
    a = "G"
    pass
class B(Y):
    a = "B"
    pass

class C(Z):
    a = "C"
    pass
class H(Z):
    pass
class D(Z):
    a = "D"
    pass
class E(Z):
    a = "E"
    pass
    
class I:
    pass

class X(J, A, G, B, C, H, D, E, F, I):
    a = "X"
    pass


print(X.a) # X

#################################################

Class level data


class Male:
    head = 1
    hand = 2
    leg = 2
    gender = "male"
    country = "Myanmar"

    def __init__(self, id, name, age):
        self.id = id
        self.name = name
        self.age = age


#################################################

Inheritance

                        Human
                        
                        /   \
                        
                   Male     Female
                   
                   
class Human:
    head = 1
    hand = 2
    leg = 2
    country = "Myanmar"

    def __init__(self, id, name, age):
        self.id = id
        self.name = name
        self.age = age


class Male(Human):
    gender = "male"


class Female(Human):
    gender = "female"


x1 = Male("9/WTN(N)123456", "Mg Mg", 30)
x2 = Male("9/WTN(N)123457", "Mg Ba", 29)
x3 = Male("9/WTN(N)123458", "Mg Mya", 28)

print(x1.country)

##################################################################################################

"""
