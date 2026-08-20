class Product:
    category = "Electronics"

    def __init__(self, name, price):
        self.name = name
        self.price = price

product1 = Product("Laptop", 50000)
product2 = Product("Mobile", 20000)
product3 = Product("Tablet", 30000)

print(product1.name, product1.category)
print(product2.name, product2.category)
print(product3.name, product3.category)