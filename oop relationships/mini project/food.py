class Order:
    def show_order(self):
        print("This is an order")


class FoodOrder(Order):
    def place_order(self):
        print("Food order placed")


class MenuItem:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def show_item(self):
        print(self.name, "-", self.price)


class Restaurant:
    def __init__(self):
        self.menu = [
            MenuItem("Pizza", 300),
            MenuItem("Burger", 150)
        ]

    def show_menu(self):
        for item in self.menu:
            item.show_item()


class PaymentService:
    def pay(self, amount):
        print("Payment successful:", amount)


class DeliveryService:
    def deliver(self, address):
        print("Delivered to:", address)


order = FoodOrder()
restaurant = Restaurant()
payment = PaymentService()
delivery = DeliveryService()

order.show_order()
order.place_order()

restaurant.show_menu()

payment.pay(450)
delivery.deliver("Rajahmundry")