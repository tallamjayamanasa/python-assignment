class PaymentGateway:
    def charge(self, cart_owner, total_amount):
        print(f"Charging ${total_amount:.2f} to {cart_owner} via payment gateway.")
        return True


class ShoppingCart:
    def __init__(self, cart_owner):
        self.cart_owner = cart_owner
        self.items = []
        self.payment_gateway = PaymentGateway()

    def add_item(self, item, price):
        self.items.append((item, price))

    def checkout(self):
        total = sum(price for _, price in self.items)
        if total > 0:
            self.payment_gateway.charge(self.cart_owner, total)
            print(f"Checkout complete for {self.cart_owner}.")
        else:
            print("Cart is empty.")


def run_demo():
    cart = ShoppingCart("Sarah")
    cart.add_item("Laptop", 1200.00)
    cart.add_item("Mouse", 35.00)
    print("ShoppingCart -> PaymentGateway example")
    cart.checkout()
    print()
