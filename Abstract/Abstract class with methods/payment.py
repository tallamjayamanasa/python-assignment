from abc import ABC, abstractmethod

class Payment(ABC):

    @abstractmethod
    def pay(self):
        pass

    @abstractmethod
    def refund(self):
        pass


class UPI(Payment):

    def pay(self):
        print("Payment made using UPI")

    def refund(self):
        print("UPI payment refunded")


class CreditCard(Payment):

    def pay(self):
        print("Payment made using Credit Card")

    def refund(self):
        print("Credit Card payment refunded")


class NetBanking(Payment):

    def pay(self):
        print("Payment made using Net Banking")

    def refund(self):
        print("Net Banking payment refunded")


u = UPI()
c = CreditCard()
n = NetBanking()

u.pay()
u.refund()

c.pay()
c.refund()

n.pay()
n.refund()