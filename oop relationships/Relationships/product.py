class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def show_product(self):
        print(self.name, "-", self.price)


class PaymentService:
    def pay(self, amount):
        print("Payment successful:", amount)


class DeliveryService:
    def deliver(self, address):
        print("Order delivered to:", address)


class OnlineOrder:
    def __init__(self):
        self.products = [
            Product("Laptop", 50000),
            Product("Mouse", 500)
        ]

    def show_products(self):
        for product in self.products:
            product.show_product()

    def checkout(self, payment_service, delivery_service):
        total = sum(product.price for product in self.products)

        payment_service.pay(total)
        delivery_service.deliver("Rajahmundry")


order = OnlineOrder()
payment = PaymentService()
delivery = DeliveryService()

order.show_products()
order.checkout(payment, delivery)