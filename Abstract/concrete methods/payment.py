from abc import ABC, abstractmethod

class Payment(ABC):

    def __init__(self, amount):
        self.amount = amount

    @abstractmethod
    def pay(self):
        pass

    def display_amount(self):
        print("Payment Amount =", self.amount)


class UPI(Payment):

    def pay(self):
        print("Payment made using UPI")


u = UPI(1500)

u.pay()
u.display_amount()