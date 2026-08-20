class InvalidPINError(Exception):
    pass


class InsufficientBalanceError(Exception):
    pass


class InvalidWithdrawalError(Exception):
    pass


class InvalidAccountError(Exception):
    pass


class ATM:
    def __init__(self):
        self.accounts = {
            "1001": {
                "pin": "1234",
                "balance": 10000
            }
        }

    def withdraw(self, account, pin, amount):
        if account not in self.accounts:
            raise InvalidAccountError("Invalid account.")

        if pin != self.accounts[account]["pin"]:
            raise InvalidPINError("Invalid PIN.")

        if amount <= 0:
            raise InvalidWithdrawalError(
                "Withdrawal amount must be greater than zero."
            )

        if amount > self.accounts[account]["balance"]:
            raise InsufficientBalanceError(
                "Insufficient balance."
            )

        self.accounts[account]["balance"] -= amount

        print("Withdrawal successful.")
        print("Remaining balance:",
              self.accounts[account]["balance"])


atm = ATM()

try:
    account = input("Enter account number: ")
    pin = input("Enter PIN: ")
    amount = float(input("Enter withdrawal amount: "))

    atm.withdraw(account, pin, amount)

except (InvalidAccountError, InvalidPINError,
        InvalidWithdrawalError, InsufficientBalanceError) as e:
    print("Error:", e)

except ValueError:
    print("Error: Enter a valid amount.")