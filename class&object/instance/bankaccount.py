class BankAccount:
    def __init__(self, account_holder, account_number, balance):
        self.account_holder = account_holder
        self.account_number = account_number
        self.balance = balance

account1 = BankAccount("Jaya", "10001", 25000)
account2 = BankAccount("Rahul", "10002", 40000)

print("Account 1")
print("Holder:", account1.account_holder)
print("Account Number:", account1.account_number)
print("Balance:", account1.balance)

print("\n Account 2")
print("Holder:", account2.account_holder)
print("Account Number:", account2.account_number)
print("Balance:", account2.balance)