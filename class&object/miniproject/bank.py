class BankAccount:
    def __init__(self, account_no, name, balance=0):
        self.account_no = account_no
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print("Amount deposited successfully.")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print("Amount withdrawn successfully.")
        else:
            print("Insufficient balance.")

    def check_balance(self):
        print("Balance:", self.balance)

    def display(self):
        print("Account Number:", self.account_no)
        print("Account Holder:", self.name)
        print("Balance:", self.balance)


accounts = []

while True:
    print("\n--- Bank Management System ---")
    print("1. Create Account")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Check Balance")
    print("5. Account Details")
    print("6. Exit")

    choice = int(input("Enter choice: "))

    if choice == 1:
        acc_no = int(input("Enter account number: "))
        name = input("Enter name: ")
        accounts.append(BankAccount(acc_no, name))
        print("Account created.")

    elif choice == 2:
        acc_no = int(input("Enter account number: "))
        amount = float(input("Enter amount: "))

        for acc in accounts:
            if acc.account_no == acc_no:
                acc.deposit(amount)
                break
        else:
            print("Account not found.")

    elif choice == 3:
        acc_no = int(input("Enter account number: "))
        amount = float(input("Enter amount: "))

        for acc in accounts:
            if acc.account_no == acc_no:
                acc.withdraw(amount)
                break
        else:
            print("Account not found.")

    elif choice == 4:
        acc_no = int(input("Enter account number: "))

        for acc in accounts:
            if acc.account_no == acc_no:
                acc.check_balance()
                break
        else:
            print("Account not found.")

    elif choice == 5:
        acc_no = int(input("Enter account number: "))

        for acc in accounts:
            if acc.account_no == acc_no:
                acc.display()
                break
        else:
            print("Account not found.")

    elif choice == 6:
        break

    else:
        print("Invalid choice.")