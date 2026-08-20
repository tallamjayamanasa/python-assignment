class Car:
    def __init__(self, brand, color, price):
        self.brand = brand
        self.color = color
        self.price = price

car1 = Car("Toyota", "Red", 800000)
car2 = Car("Honda", "White", 900000)
car3 = Car("BMW", "Black", 2500000)

print(car1.brand, car1.color, car1.price)
print(car2.brand, car2.color, car2.price)
print(car3.brand, car3.color, car3.price)