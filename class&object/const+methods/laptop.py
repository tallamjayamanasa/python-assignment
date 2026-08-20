class Laptop:
    def __init__(self, brand, model, ram, storage, processor, price):
        self.brand = brand
        self.model = model
        self.ram = ram
        self.storage = storage
        self.processor = processor
        self.price = price

    def display(self):
        print("Brand:", self.brand)
        print("Model:", self.model)
        print("RAM:", self.ram)
        print("Storage:", self.storage)
        print("Processor:", self.processor)
        print("Price:", self.price)

laptop = Laptop(
    "Dell",
    "Inspiron",
    "8GB",
    "512GB SSD",
    "Intel i5",
    55000
)

laptop.display()