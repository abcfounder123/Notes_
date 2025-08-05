
"""

################################################

Step.1 ( Write ) 

Car မှာ ကားနံပါတ် တာယာနဲ့ အင်ဂျင်ပါတယ်။ (VIN, engine, tires)

Tires ( ကားတာယာ ) တွင် size နှင့် pressure ပါသည်။  
pressure ၏ မူလတန်ဖိုးသည် 0 ( psi ) ဖြစ်သည်။
လေထိုးသောလုပ်ဆောင်ချက်ပါသည်။ သတ်မှတ်ပေးလိုက်သော ဖိအားအတိုင်း လေထိုးပေးမည်။

Engine တွင် fuel_type ပါသည်။
စက်နှိုး/မနှိုး ဟူသော အခြေအနေ  state ပါသည်။
မူလအခြေအနေမှာ စက်မနှိုးထားသဖြင့် off ဖြစ်နေမည်။
ပေးထားသော fuel_type ဖြင့် စက်နှိုး ၊ စက်ရပ် မည့်လုပ်‌ဆောင်ချက်ပါသည်။ ( on(), off() )

ဖန်တီးခဲ့သော တာယာနှင့် အင်ဂျင်ကို ယူသုံးပြီး city_car တစ်စီးဖန်တီးပါ။
ကားနံပါတ်မှာ 001A ၊ တာယာမှာ 15 လက်မ၊ ဆီအမျိုးအစားမှာ petrol ဓါတ်ဆီ ဖြစ်သည်။
ထိုကားကို လေဖိအား 3 psi ထိလေထိုးပြီး စက်နှိုးပါ။

################################################

Step.2 ( Divide )

paper name - Car
data -  VIN, engine, tires, 50000
method - 

paper name - Tires
data - size, pressure=0 ( psi )
method - pump(p)

paper name - Engine
data -  fuel_type , state="off" 
method - on(), off()

################################################

Step.3 ( Draw )


class Tires:
    def __init__(self, size):
        self.size = size
        self.pressure = 0

    def pump(self, pressure):
        print("pump")


class Engine:
    def __init__(self, fuel_type):
        self.fuel_type = fuel_type
        self.state="off"

    def on(self):
        print("On")

    def off(self):
        print("Off")


class Car:
    def __init__(self, VIN, engine, tires):
        self.VIN = VIN
        self.engine = engine
        self.tires = tires


################################################

Step.4 ( Color.1 ) (control pressure)

pump(pressure)   --->  self.pressure = pressure


class Tires:
    def __init__(self, size):
        self.size = size
        self.pressure = 0

    def pump(self, pressure):
        self.pressure = pressure
        print("pumped to " + self.pressure)


################################################

Step.4 ( Color.2 ) limit ON and OFF

if off: on
if on: off


class Engine:
    def __init__(self, fuel_type):
        self.fuel_type = fuel_type
        self.state="off"

    def on(self):
        if self.state == "off":
            self.state = "on"
            print("On")
        else:
            print("already on.")

    def off(self):
        if self.state == "on":
            self.state = "off"
            print("Off")
        else:
            print("already off.")


################################################

Step.4 ( Color.3 ) (auto create serial number)

c = 0
Car.c += 1
self.VIN = f"BMW-{Car.c:0>4}A"


class Car:
    c = 0
    def __init__(self, engine, tires):
        Car.c += 1
        self.VIN = f"BMW-{Car.c:0>4}A"
        self.engine = engine
        self.tires = tires


################################################

Step.4 ( Color.4 ) (representation string)

def __repr__(self):
        return f"{self.VIN}"

        

class Car:
    c = 0
    def __init__(self, engine, tires):
        Car.c += 1
        self.VIN = f"BMW-{Car.c:0>4}A"
        self.engine = engine
        self.tires = tires

    def __repr__(self):
        return f"{self.VIN}"


################################################

Step.4 ( Color.5 ) (creating many obj)

cars = []
for _ in range(1000):
    cars.append(Car(Engine("petrol"), Tires("15 inches")))
    
################################################

Step.4 ( Color.6 ) (controlling many obj)

# car 1, 3, 5, ... on
for i in range(0, 100,2):
    cars[i].engine.on()

# last 10 on
for car in cars[-10:]:
    car.engine.on()

################################################

Step.5 ( Test )


class Tires:
    def __init__(self, size):
        self.size = size
        self.pressure = 0

    def pump(self, pressure):
        self.pressure = pressure
        print("pumped to " + self.pressure)


class Engine:
    def __init__(self, fuel_type):
        self.fuel_type = fuel_type
        self.state="off"

    def on(self):
        if self.state == "off":
            self.state = "on"
            print("On")
        else:
            print("already on.")

    def off(self):
        if self.state == "on":
            self.state = "off"
            print("Off")
        else:
            print("already off.")


class Car:
    c = 0
    def __init__(self, engine, tires):
        Car.c += 1
        self.VIN = f"BMW-{Car.c:0>4}A"
        self.engine = engine
        self.tires = tires

    def __repr__(self):
        return f"{self.VIN} {self.engine.state}"


cars = []
for _ in range(100):
    cars.append(Car(Engine("petrol"), Tires("15 inches")))

print(cars)

for car in cars[-10:]:
    car.engine.on()

print(cars)

################################################


"""

