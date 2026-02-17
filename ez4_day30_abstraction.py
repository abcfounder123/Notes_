
"""

Abstraction


from abc import ABC, abstractmethod


class CarRule(ABC):
    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def stop(self):
        pass

    @abstractmethod
    def brake(self):
        pass


class AICarRule(ABC):
    @abstractmethod
    def gps(self):
        pass

    @abstractmethod
    def sensor(self):
        pass

    @abstractmethod
    def ai_control(self):
        pass


class CityCar(CarRule):
    def __init__(self):
        self.engine = "city engine"
        self.tire = "city tire"

    def start(self):
        print(f"{self.engine} start.")

    def stop(self):
        print(f"{self.engine} stop.")
        
    def brake(self):
        print("brake")


class AICar(CarRule, AICarRule):
    def __init__(self):
        self.engine = "city engine"
        self.tire = "city tire"

    def start(self):
        print(f"{self.engine} start.")

    def stop(self):
        print(f"{self.engine} stop.")

    def brake(self):
        print("brake")

    def gps(self):
        print("GPS .... ")

    def sensor(self):
        print("Sensor .... ")

    def ai_control(self):
        print("Control .... ")
        
        
##################################################################################################      
 
"""

