from abc import ABC, abstractmethod

class ECommercePayment(ABC):

    @abstractmethod
    def pay(self, amount):
        pass


class UPI(ECommercePayment):

    def pay(self, amount):
        print("Paid", amount, "using UPI")


class CreditCard(ECommercePayment):

    def pay(self, amount):
        print("Paid", amount, "using Credit Card")


class DebitCard(ECommercePayment):

    def pay(self, amount):
        print("Paid", amount, "using Debit Card")


class NetBanking(ECommercePayment):

    def pay(self, amount):
        print("Paid", amount, "using Net Banking")


payments = [
    UPI(),
    CreditCard(),
    DebitCard(),
    NetBanking()
]

for payment in payments:
    payment.pay(2000)