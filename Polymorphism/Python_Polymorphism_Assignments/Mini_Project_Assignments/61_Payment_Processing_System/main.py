class UPI:
    def pay(self,amount): print("UPI paid",amount)
class CreditCard:
    def pay(self,amount): print("Credit Card paid",amount)
class DebitCard:
    def pay(self,amount): print("Debit Card paid",amount)
class NetBanking:
    def pay(self,amount): print("Net Banking paid",amount)
def process_payment(method,amount): method.pay(amount)
for x in [UPI(),CreditCard(),DebitCard(),NetBanking()]: process_payment(x,1000)
