class BankAccount:
    bank_name = "State Bank"

    def __init__(self, account_holder, balance):
        self.account_holder = account_holder
        self.balance = balance

account1 = BankAccount("Jaya", 25000)
account2 = BankAccount("Rahul", 30000)
account3 = BankAccount("Priya", 40000)

print(account1.account_holder, account1.bank_name)
print(account2.account_holder, account2.bank_name)
print(account3.account_holder, account3.bank_name)