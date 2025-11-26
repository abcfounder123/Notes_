
"""

OOP

1. Attributes
   - Oxygen, nurse
   - data, function

2. Relations
   - tightly cople, "is a", inheritance
   - loosely couple, "has a", composition

3. Inheritance ( parents, head )
   - water
   - code reuse

4. MRO
   - self, nearest ...

5. Composition ( friends, clothes )
   -

6. "is a"  Relation

7. "has a" Relation

8. Inheritance Vs Composition

9. object and label

################################################

Tightly cople, "is a", inheritance, MRO

                  A           color = "red", + 80

             B         C      ( MRO -> C, A )

                  D           ( MRO -> D, B, C, A )


                  E           ( MRO -> E, D, B, C, A )

################################################

Inheritance (code reuse)

 love  red     2000
 love  green   2000  or  1


        A     color = "red", + 2000

        B     color = "green" ( 1999 from A )

################################################

Inheritance (code reuse)

p1    100
p2    100

p3    50 from p1 + 50 from p2


    p1         p2

        p3

################################################

Integer obj and attributes

int obj  = number + 74

['__abs__', '__add__', '__and__', '__bool__', '__ceil__', '__class__', '__delattr__', '__dir__', '__divmod__', '__doc__', '__eq__', '__float__', '__floor__', '__floordiv__', '__format__', '__ge__', '__getattribute__', '__getnewargs__', '__getstate__', '__gt__', '__hash__', '__index__', '__init__', '__init_subclass__', '__int__', '__invert__', '__le__', '__lshift__', '__lt__', '__mod__', '__mul__', '__ne__', '__neg__', '__new__', '__or__', '__pos__', '__pow__', '__radd__', '__rand__', '__rdivmod__', '__reduce__', '__reduce_ex__', '__repr__', '__rfloordiv__', '__rlshift__', '__rmod__', '__rmul__', '__ror__', '__round__', '__rpow__', '__rrshift__', '__rshift__', '__rsub__', '__rtruediv__', '__rxor__', '__setattr__', '__sizeof__', '__str__', '__sub__', '__subclasshook__', '__truediv__', '__trunc__', '__xor__', 'as_integer_ratio', 'bit_count', 'bit_length', 'conjugate', 'denominator', 'from_bytes', 'imag', 'is_integer', 'numerator', 'real', 'to_bytes']

################################################

Inheritance (code reuse)

      A     n + 74  (n=1, repr="1")

      B     repr = "one"

################################################

int
- n = 1
- repr = "1"

Myint
- n = 1
- repr = "ha ha"

################################################

class Myint(int):
    def __repr__(self):
        return "ha ha"


x = Myint(1)
print(x)

################################################

Inheritance Vs Composition

Diesel engine car is a car.   ( "is a" relation  -> tightly cople -> inheritance )
Car has a brake.              ( "has a" relation -> loosely cople -> composition )
Car has an engine.            ( "has a" relation -> loosely cople -> composition )

################################################

object and label

1, int(1)  ->   command for creating int obj
obj        ->   RAM
x          ->   label

x = 1  # Mandalay
x = 2  # Yangon

################################################################################################

"""


