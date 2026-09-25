class UPI:
    def pay(self,amount): print("UPI paid",amount)
class Card:
    def pay(self,amount): print("Card paid",amount)
class NetBanking:
    def pay(self,amount): print("Net Banking paid",amount)
def checkout(payment): payment.pay(1500)
for x in [UPI(),Card(),NetBanking()]: checkout(x)
