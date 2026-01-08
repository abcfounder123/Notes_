
"""

Abstraction


from abc import ABCMeta, abstractmethod


class Car(metaclass=ABCMeta):

    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def stop(self):
        pass


class City_car(Car):
    def __init__(self):
        self.engine = "city engine"
        self.tire = "city tire"

    def start(self):
        print(f"{self.engine} start.")

    def stop(self):
        print(f"{self.engine} stop.")


x = City_car()
x.start()
x.stop()

##################################################################################################


from abc import ABC, abstractmethod


class Book(ABC):
    def __init__(self, title, quantity, author, price):
        self.title = title
        self.quantity = quantity
        self.author = author
        self.__price = price
        self.__discount = None

    def set_discount(self, discount):
        self.__discount = discount

    def get_price(self):
        if self.__discount:
            return self.__price * (1 - self.__discount)
        return self.__price

    @abstractmethod
    def __repr__(self):
        return f"Book: {self.title}\nQuantity: {self.quantity}\nAuthor: {self.author}\nPrice: {self.get_price()}\n"


class Novel(Book):
    def __init__(self, title, quantity, author, price, pages):
        super().__init__(title, quantity, author, price)
        self.pages = pages

    def __repr__(self):
        return super().__repr__() + f"Pages: {self.pages}\n"

class Academic(Book):
    def __init__(self, title, quantity, author, price, branch):
        super().__init__(title, quantity, author, price)
        self.branch = branch

    def __repr__(self):
        return super().__repr__() + f"Branch: {self.branch}\n"


novel1 = Novel('Two States', 20, 'Chetan Bhagat', 300, 200)
novel1.set_discount(0.20)
print(novel1)

academic1 = Academic('Python Foundations', 12, 'PSF', 300, 'IT')
print(academic1)

##################################################################################################

"""
