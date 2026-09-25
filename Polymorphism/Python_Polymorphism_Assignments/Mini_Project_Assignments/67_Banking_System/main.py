class SavingsAccount:
    def calculate_interest(self,balance): return balance*.04
class CurrentAccount:
    def calculate_interest(self,balance): return balance*.01
class FixedDeposit:
    def calculate_interest(self,balance): return balance*.07
def show_interest(a): print(a.__class__.__name__,a.calculate_interest(10000))
for x in [SavingsAccount(),CurrentAccount(),FixedDeposit()]: show_interest(x)
