class BankAccount:
    def __init__(self, account_holder, balance):
        self.account_holder = account_holder
        self.balance = balance

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print("Withdrawal successful")
            print("Remaining Balance:", self.balance)
        else:
            print("Insufficient balance")

    def deposit(self, amount):
        self.balance += amount
        print("Deposit successful")
        print("Current Balance:", self.balance)


account = BankAccount("Jaya", 10000)

account.withdraw(3000)
account.withdraw(10000)