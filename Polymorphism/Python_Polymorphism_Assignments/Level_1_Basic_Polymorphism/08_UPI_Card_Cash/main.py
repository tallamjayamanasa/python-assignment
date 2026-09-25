class UPIPayment:
    def pay(self): print("Paid using UPI")
class CardPayment:
    def pay(self): print("Paid using Card")
class CashPayment:
    def pay(self): print("Paid using Cash")

for x in [UPIPayment(), CardPayment(), CashPayment()]: x.pay()
