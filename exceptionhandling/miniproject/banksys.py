class InsufficientBalanceError(Exception):
    pass


class InvalidAmountError(Exception):
    pass


class InvalidAccountError(Exception):
    pass


class Bank:
    def __init__(self):
        self.accounts = {
            "1001": 5000,
            "1002": 10000
        }

    def deposit(self, account, amount):
        if account not in self.accounts:
            raise InvalidAccountError("Invalid account number.")

        if amount <= 0:
            raise InvalidAmountError("Amount must be greater than zero.")

        self.accounts[account] += amount
        print("Deposit successful.")
        print("Balance:", self.accounts[account])

    def withdraw(self, account, amount):
        if account not in self.accounts:
            raise InvalidAccountError("Invalid account number.")

        if amount <= 0:
            raise InvalidAmountError("Amount must be greater than zero.")

        if amount > self.accounts[account]:
            raise InsufficientBalanceError("Insufficient balance.")

        self.accounts[account] -= amount
        print("Withdrawal successful.")
        print("Balance:", self.accounts[account])


bank = Bank()

try:
    account = input("Enter account number: ")
    amount = float(input("Enter amount: "))
    choice = input("Enter deposit or withdraw: ").lower()

    if choice == "deposit":
        bank.deposit(account, amount)
    elif choice == "withdraw":
        bank.withdraw(account, amount)
    else:
        print("Invalid choice.")

except (InvalidAccountError, InvalidAmountError,
        InsufficientBalanceError) as e:
    print("Error:", e)

except ValueError:
    print("Error: Enter a valid amount.")