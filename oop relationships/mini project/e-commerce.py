class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def show_product(self):
        print(self.name, "-", self.price)


class ElectronicsProduct(Product):
    def show_type(self):
        print("Electronics Product")


class ClothingProduct(Product):
    def show_type(self):
        print("Clothing Product")


class PaymentService:
    def pay(self, amount):
        print("Payment successful:", amount)


class DeliveryService:
    def deliver(self, address):
        print("Delivered to:", address)


class ShoppingCart:
    def __init__(self):
        self.products = [
            ElectronicsProduct("Laptop", 50000),
            ClothingProduct("Shirt", 1000)
        ]

    def show_products(self):
        for product in self.products:
            product.show_product()

    def checkout(self, payment, delivery):
        total = sum(product.price for product in self.products)
        payment.pay(total)
        delivery.deliver("Rajahmundry")


cart = ShoppingCart()
payment = PaymentService()
delivery = DeliveryService()

cart.show_products()
cart.checkout(payment, delivery)