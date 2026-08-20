class Car:
    company = "Toyota"
    number_of_wheels = 4

    def __init__(self, model, price):
        self.model = model
        self.price = price

car1 = Car("Innova", 2500000)
car2 = Car("Fortuner", 3500000)
car3 = Car("Glanza", 1200000)

print("Company:", car1.company)
print("Wheels:", car1.number_of_wheels)
print("Model:", car1.model)
print("Price:", car1.price)

print()

print("Company:", car2.company)
print("Wheels:", car2.number_of_wheels)
print("Model:", car2.model)
print("Price:", car2.price)

print()
print("Company:", car3.company)
print("Wheels:", car3.number_of_wheels)
print("Model:", car3.model)
print("Price:", car3.price)