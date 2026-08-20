class Mobile:
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price

mobile1 = Mobile("Samsung", "Galaxy S25", 70000)

print("Brand:", mobile1.brand)
print("Model:", mobile1.model)
print("Price:", mobile1.price)