balance = 0
transactions = []

def deposit():
    global balance

    amount = float(input("Enter deposit amount: "))

    if amount > 0:
        balance += amount
        transactions.append("Deposited: " + str(amount))
        print("Amount deposited successfully.")
    else:
        print("Invalid amount.")

def withdraw():
    global balance

    amount = float(input("Enter withdrawal amount: "))

    if amount <= 0:
        print("Invalid amount.")
    elif amount > balance:
        print("Insufficient balance.")
    else:
        balance -= amount
        transactions.append("Withdrawn: " + str(amount))
        print("Amount withdrawn successfully.")

def check_balance():
    print("Current balance:", balance)

def transaction_history():
    print("\n--- Transaction History ---")

    if not transactions:
        print("No transactions.")
    else:
        for transaction in transactions:
            print(transaction)


while True:
    print("\n--- Banking System ---")
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Check Balance")
    print("4. Transaction History")
    print("5. Exit")

    choice = int(input("Enter choice: "))

    if choice == 1:
        deposit()
    elif choice == 2:
        withdraw()
    elif choice == 3:
        check_balance()
    elif choice == 4:
        transaction_history()
    elif choice == 5:
        print("Thank you for using banking system.")
        break
    else:
        print("Invalid choice")