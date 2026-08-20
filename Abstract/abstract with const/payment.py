from abc import ABC, abstractmethod

class Payment(ABC):

    def __init__(self, amount, transaction_id):
        self.amount = amount
        self.transaction_id = transaction_id

    @abstractmethod
    def pay(self):
        pass


class UPI(Payment):

    def pay(self):
        print("Payment Method: UPI")
        print("Amount:", self.amount)
        print("Transaction ID:", self.transaction_id)


class CreditCard(Payment):

    def pay(self):
        print("Payment Method: Credit Card")
        print("Amount:", self.amount)
        print("Transaction ID:", self.transaction_id)


class NetBanking(Payment):

    def pay(self):
        print("Payment Method: Net Banking")
        print("Amount:", self.amount)
        print("Transaction ID:", self.transaction_id)


u = UPI(1000, "UPI101")
c = CreditCard(2000, "CARD102")
n = NetBanking(3000, "NET103")

u.pay()
c.pay()
n.pay()