class Car:
    def __init__(self, brand, model, year, price):
        self.brand = brand
        self.model = model
        self.year = year
        self.price = price

car1 = Car("Toyota", "Innova", 2024, 2500000)
car2 = Car("Honda", "City", 2023, 1500000)
car3 = Car("BMW", "X1", 2025, 5000000)

print(car1.brand, car1.model, car1.year, car1.price)
print(car2.brand, car2.model, car2.year, car2.price)
print(car3.brand, car3.model, car3.year, car3.price)