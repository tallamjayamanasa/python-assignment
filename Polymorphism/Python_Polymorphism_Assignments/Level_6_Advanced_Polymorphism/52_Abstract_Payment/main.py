from abc import ABC, abstractmethod
class Payment(ABC):
    @abstractmethod
    def pay(self): pass
class UPI(Payment):
    def pay(self): print("UPI payment")
class Card(Payment):
    def pay(self): print("Card payment")
class NetBanking(Payment):
    def pay(self): print("Net Banking payment")
for x in [UPI(),Card(),NetBanking()]: x.pay()
