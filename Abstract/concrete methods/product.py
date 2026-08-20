from abc import ABC, abstractmethod

class Product(ABC):

    def __init__(self, name, price):
        self.name = name
        self.price = price

    @abstractmethod
    def calculate_discount(self):
        pass

    def display_product(self):
        print("Product:", self.name)
        print("Price:", self.price)


class Mobile(Product):

    def calculate_discount(self):
        discount = self.price * 0.10
        print("Discount =", discount)


m = Mobile("Mobile Phone", 20000)

m.calculate_discount()
m.display_product()