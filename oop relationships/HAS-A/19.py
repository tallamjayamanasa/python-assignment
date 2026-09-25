class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def show_product(self):
        print(self.name, "-", self.price)

class ShoppingCart:
    def __init__(self):
        self.products = [
            Product("Laptop", 50000),
            Product("Mouse", 500),
            Product("Keyboard", 1000)
        ]

    def show_cart(self):
        for product in self.products:
            product.show_product()

cart = ShoppingCart()
cart.show_cart()