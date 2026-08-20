from abc import ABC, abstractmethod

class Product(ABC):

    def __init__(self, name, price):
        self.name = name
        self.price = price

    @abstractmethod
    def calculate_discount(self):
        pass


class Mobile(Product):

    def calculate_discount(self):
        discount = self.price * 0.10
        final_price = self.price - discount

        print("Product:", self.name)
        print("Price:", self.price)
        print("Discount:", discount)
        print("Final Price:", final_price)


m = Mobile("Mobile Phone", 20000)
m.calculate_discount()