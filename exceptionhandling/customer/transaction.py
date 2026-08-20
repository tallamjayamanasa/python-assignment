class InvalidTransactionError(Exception):
    pass


try:
    balance = 5000

    transaction = input(
        "Enter transaction type (deposit/withdraw): "
    ).lower()

    amount = float(input("Enter amount: "))

    if amount <= 0:
        raise InvalidTransactionError(
            "Transaction amount must be greater than zero."
        )

    if transaction == "deposit":
        balance += amount
        print("Deposit successful.")

    elif transaction == "withdraw":
        if amount > balance:
            raise InvalidTransactionError("Insufficient balance.")

        balance -= amount
        print("Withdrawal successful.")

    else:
        raise InvalidTransactionError("Invalid transaction type.")

    print("Current balance:", balance)

except InvalidTransactionError as e:
    print("Error:", e)