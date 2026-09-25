class UPI:
    def pay(self): print("UPI paid")
class Card:
    def pay(self): print("Card paid")
def process(payment): payment.pay()
for x in [UPI(), Card()]: process(x)
