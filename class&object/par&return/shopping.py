class ShoppingCart:
    def __init__(self):
        self.products = []

    def add_product(self, name, price):
        self.products.append([name, price])

    def remove_product(self, name):
        for product in self.products:
            if product[0] == name:
                self.products.remove(product)
                return "Product removed"

        return "Product not found"

    def calculate_total(self):
        total = 0

        for product in self.products:
            total = total + product[1]

        return total


cart = ShoppingCart()

cart.add_product("Laptop", 50000)
cart.add_product("Mouse", 1000)
cart.add_product("Keyboard", 2000)

print("Total:", cart.calculate_total())

print(cart.remove_product("Mouse"))

print("Total after removal:", cart.calculate_total())