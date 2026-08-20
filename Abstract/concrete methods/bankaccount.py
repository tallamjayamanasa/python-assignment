from abc import ABC, abstractmethod

class BankAccount(ABC):

    def __init__(self, balance):
        self.balance = balance

    @abstractmethod
    def calculate_interest(self):
        pass

    def display_balance(self):
        print("Account Balance =", self.balance)


class SavingsAccount(BankAccount):

    def calculate_interest(self):
        interest = self.balance * 0.05
        print("Interest =", interest)


s = SavingsAccount(20000)

s.calculate_interest()
s.display_balance()