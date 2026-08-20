from abc import ABC, abstractmethod

class BankAccount(ABC):
    @abstractmethod
    def calculate_interest(self):
        pass

class SavingsAccount(BankAccount):
    def calculate_interest(self):
        print("Savings Account interest = 5%")

class CurrentAccount(BankAccount):
    def calculate_interest(self):
        print("Current Account interest = 2%")

s = SavingsAccount()
c = CurrentAccount()

s.calculate_interest()
c.calculate_interest()