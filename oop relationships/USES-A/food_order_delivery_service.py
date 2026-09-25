class DeliveryService:
    def schedule_delivery(self, order):
        print(f"Scheduling delivery for food order #{order.order_id} to {order.address}.")


class FoodOrder:
    def __init__(self, order_id, address):
        self.order_id = order_id
        self.address = address
        self.delivery_service = DeliveryService()

    def place_order(self):
        self.delivery_service.schedule_delivery(self)


def run_demo():
    order = FoodOrder(42, "12 Main Street")
    print("FoodOrder -> DeliveryService example")
    order.place_order()
    print()
