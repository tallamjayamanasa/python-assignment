class Payment:
    def pay(self): print("Payment")
class UPI(Payment):
    def pay(self): print("Paid by UPI")
class CreditCard(Payment):
    def pay(self): print("Paid by Credit Card")
class NetBanking(Payment):
    def pay(self): print("Paid by Net Banking")

for x in [UPI(), CreditCard(), NetBanking()]: x.pay()
