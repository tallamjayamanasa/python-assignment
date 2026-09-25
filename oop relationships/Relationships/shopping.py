class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def show_product(self):
        print(self.name, "-", self.price)


class PaymentGateway:
    def pay(self, amount):
        print("Payment successful:", amount)


class ShoppingCart:
    def __init__(self):
        self.products = [
            Product("Laptop", 50000),
            Product("Mouse", 500)
        ]

    def show_products(self):
        for product in self.products:
            product.show_product()

    def checkout(self, payment_gateway):
        total = sum(product.price for product in self.products)
        payment_gateway.pay(total)


cart = ShoppingCart()
gateway = PaymentGateway()

cart.show_products()
cart.checkout(gateway)