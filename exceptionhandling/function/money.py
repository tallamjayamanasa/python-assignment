def withdraw(balance, amount):
    try:
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive.")

        if amount > balance:
            raise ValueError("Insufficient balance.")

        balance -= amount

        print("Withdrawal successful.")
        print("Remaining balance:", balance)

    except ValueError as e:
        print("Error:", e)


try:
    balance = 5000
    amount = float(input("Enter withdrawal amount: "))

    withdraw(balance, amount)

except ValueError:
    print("Error: Please enter a valid amount.")