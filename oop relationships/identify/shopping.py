class PaymentGateway:
    def pay(self, amount):
        print("Payment successful:", amount)


class ShoppingCart:
    def checkout(self, gateway):
        gateway.pay(2500)


cart = ShoppingCart()
gateway = PaymentGateway()

cart.checkout(gateway)