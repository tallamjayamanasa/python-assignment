class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def total_price(self):
        return self.price * self.quantity

product1 = Product("Pen", 20, 5)
product2 = Product("Book", 100, 3)
product3 = Product("Bag", 500, 2)

print(product1.name, "Total:", product1.total_price())
print(product2.name, "Total:", product2.total_price())
print(product3.name, "Total:", product3.total_price())