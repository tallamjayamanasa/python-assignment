from abc import ABC, abstractmethod


class Payment(ABC):

    def __init__(self, amount):
        self.amount = amount

    @abstractmethod
    def pay(self):
        pass

    def display_amount(self):
        print("Payment Amount:", self.amount)


class UPI(Payment):

    def pay(self):
        print("Payment completed using UPI")


class CreditCard(Payment):

    def pay(self):
        print("Payment completed using Credit Card")


class DebitCard(Payment):

    def pay(self):
        print("Payment completed using Debit Card")


class NetBanking(Payment):

    def pay(self):
        print("Payment completed using Net Banking")


payments = [
    UPI(1500),
    CreditCard(2500),
    DebitCard(1000),
    NetBanking(3000)
]

for payment in payments:
    payment.display_amount()
    payment.pay()
    print()