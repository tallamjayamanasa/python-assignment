class ShoppingCart:
    def __init__(self):
        self.products = []

    def add_product(self, name, price, quantity):
        product = {
            "name": name,
            "price": price,
            "quantity": quantity
        }

        self.products.append(product)

    def calculate_total(self):
        total = 0

        for product in self.products:
            total += product["price"] * product["quantity"]

        return total

    def display_products(self):
        for product in self.products:
            print(
                product["name"],
                "- Price:", product["price"],
                "- Quantity:", product["quantity"]
            )


cart = ShoppingCart()

cart.add_product("Laptop", 50000, 1)
cart.add_product("Mouse", 1000, 2)
cart.add_product("Keyboard", 2000, 1)

cart.display_products()

print("Total Bill:", cart.calculate_total())