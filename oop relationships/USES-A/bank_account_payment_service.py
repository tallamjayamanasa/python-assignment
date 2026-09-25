class PaymentService:
    def process_payment(self, account_holder, amount):
        print(f"Processing payment of ${amount:.2f} for {account_holder}.")
        return True


class BankAccount:
    def __init__(self, account_holder, balance):
        self.account_holder = account_holder
        self.balance = balance
        self.payment_service = PaymentService()

    def pay_bill(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            self.payment_service.process_payment(self.account_holder, amount)
            print(f"Remaining balance: ${self.balance:.2f}")
        else:
            print("Insufficient funds.")


def run_demo():
    account = BankAccount("David Lee", 5000.00)
    print("BankAccount -> PaymentService example")
    account.pay_bill(250.00)
    print()


