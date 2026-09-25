class BankAccount:
    def account_details(self):
        print("Bank account is active")

class SavingsAccount(BankAccount):
    def savings(self):
        print("This is a Savings Account")

class CurrentAccount(BankAccount):
    def current(self):
        print("This is a Current Account")

s = SavingsAccount()
s.account_details()
s.savings()

c = CurrentAccount()
c.account_details()
c.current()