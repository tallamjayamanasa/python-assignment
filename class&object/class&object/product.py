class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

product1 = Product("Laptop", 50000, 2)

print("Product Name:", product1.name)
print("Price:", product1.price)
print("Quantity:", product1.quantity)