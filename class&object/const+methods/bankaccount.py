class BankAccount:
    def __init__(self, account_holder, account_number, balance):
        self.account_holder = account_holder
        self.account_number = account_number
        self.balance = balance

account = BankAccount("Jaya", "1234567890", 25000)

print("Account Holder:", account.account_holder)
print("Account Number:", account.account_number)
print("Initial Balance:", account.balance)