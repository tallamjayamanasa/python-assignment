class PaymentService:
    def make_payment(self, amount):
        print("Payment completed:", amount)


class Order:
    def checkout(self, payment_service):
        payment_service.make_payment(1500)


order = Order()
payment = PaymentService()

order.checkout(payment)