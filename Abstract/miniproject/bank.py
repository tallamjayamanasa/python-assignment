from abc import ABC, abstractmethod


class BankAccount(ABC):

    def __init__(self, account_number, holder_name, balance):
        self.account_number = account_number
        self.holder_name = holder_name
        self.balance = balance

    @abstractmethod
    def calculate_interest(self):
        pass

    def deposit(self, amount):
        self.balance += amount
        print("Deposited:", amount)

    def display_balance(self):
        print("Account Holder:", self.holder_name)
        print("Balance:", self.balance)


class SavingsAccount(BankAccount):

    def calculate_interest(self):
        interest = self.balance * 0.05
        print("Savings Interest:", interest)


class CurrentAccount(BankAccount):

    def calculate_interest(self):
        interest = self.balance * 0.02
        print("Current Interest:", interest)


accounts = [
    SavingsAccount(101, "Ravi", 20000),
    CurrentAccount(102, "Anu", 30000)
]

for account in accounts:
    account.display_balance()
    account.calculate_interest()
    print()