class EmailService:
    def send_confirmation(self, order):
        print(f"Sending confirmation email for order #{order.order_id} to {order.customer_email}.")


class Order:
    def __init__(self, order_id, customer_email):
        self.order_id = order_id
        self.customer_email = customer_email
        self.email_service = EmailService()

    def confirm_order(self):
        self.email_service.send_confirmation(self)


def run_demo():
    order = Order(305, "customer@example.com")
    print("Order -> EmailService example")
    order.confirm_order()
    print()
