try:
    balance = 5000
    amount = float(input("Enter withdrawal amount: "))

    if amount > balance:
        raise ValueError("Insufficient balance.")

    balance = balance - amount

    print("Withdrawal successful.")
    print("Remaining balance:", balance)

except ValueError as e:
    print("Error:", e)