class UPIPayment:
    def pay(self): print("UPI payment processed")
class CardPayment:
    def pay(self): print("Card payment processed")
def process_payment(payment): payment.pay()
for x in [UPIPayment(), CardPayment()]: process_payment(x)
