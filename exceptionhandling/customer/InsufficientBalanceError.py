class InsufficientBalanceError(Exception):
    pass


try:
    balance = 5000
    amount = float(input("Enter withdrawal amount: "))

    if amount > balance:
        raise InsufficientBalanceError("Insufficient balance.")

    balance -= amount

    print("Withdrawal successful.")
    print("Remaining balance:", balance)

except InsufficientBalanceError as e:
    print("Error:", e)