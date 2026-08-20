class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def total_price(self):
        return self.price * self.quantity

product = Product("Laptop", 50000, 2)

print("Product:", product.name)
print("Price:", product.price)
print("Quantity:", product.quantity)
print("Total Price:", product.total_price())