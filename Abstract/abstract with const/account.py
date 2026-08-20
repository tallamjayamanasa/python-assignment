from abc import ABC, abstractmethod

class Account(ABC):

    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.balance = balance

    @abstractmethod
    def account_type(self):
        pass


class SavingsAccount(Account):

    def account_type(self):
        print("Account Type: Savings Account")
        print("Account Number:", self.account_number)
        print("Balance:", self.balance)


class CurrentAccount(Account):

    def account_type(self):
        print("Account Type: Current Account")
        print("Account Number:", self.account_number)
        print("Balance:", self.balance)


s = SavingsAccount(123456, 25000)
c = CurrentAccount(789012, 50000)

s.account_type()
c.account_type()