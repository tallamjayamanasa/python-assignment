class Laptop:
    def __init__(self, brand, ram, storage, price):
        self.brand = brand
        self.ram = ram
        self.storage = storage
        self.price = price

laptop1 = Laptop("Dell", "8GB", "512GB SSD", 55000)
laptop2 = Laptop("HP", "16GB", "1TB SSD", 70000)
laptop3 = Laptop("Lenovo", "8GB", "512GB SSD", 50000)

print(laptop1.brand, laptop1.ram, laptop1.storage, laptop1.price)
print(laptop2.brand, laptop2.ram, laptop2.storage, laptop2.price)
print(laptop3.brand, laptop3.ram, laptop3.storage, laptop3.price)