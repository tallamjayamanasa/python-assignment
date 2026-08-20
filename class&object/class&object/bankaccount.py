class BankAccount:
    def __init__(self, holder_name, account_number):
        self.holder_name = holder_name
        self.account_number = account_number

account1 = BankAccount("Jaya", "1234567890")

print("Account Holder:", account1.holder_name)
print("Account Number:", account1.account_number)