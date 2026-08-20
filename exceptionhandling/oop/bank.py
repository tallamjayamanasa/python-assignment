class InsufficientBalanceError(Exception):
    pass


class BankAccount:
    def __init__(self, balance):
        self.balance = balance

    def withdraw(self, amount):
        try:
            if amount > self.balance:
                raise InsufficientBalanceError("Insufficient balance.")

            self.balance -= amount
            print("Withdrawal successful.")
            print("Remaining balance:", self.balance)

        except InsufficientBalanceError as e:
            print("Error:", e)


account = BankAccount(5000)

try:
    amount = float(input("Enter withdrawal amount: "))
    account.withdraw(amount)

except ValueError:
    print("Error: Enter a valid amount.")