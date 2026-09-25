class BankAccount:
    def calculate_interest(self, balance): return 0
class SavingsAccount(BankAccount):
    def calculate_interest(self, balance): return balance*0.04
class CurrentAccount(BankAccount):
    def calculate_interest(self, balance): return balance*0.01

for x in [SavingsAccount(), CurrentAccount()]: print(round(x.calculate_interest(10000),2))
