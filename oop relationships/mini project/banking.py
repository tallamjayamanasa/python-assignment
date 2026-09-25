class BankAccount:
    def __init__(self, balance):
        self.balance = balance

    def show_balance(self):
        print("Balance:", self.balance)

    def pay(self, payment_service, amount):
        payment_service.make_payment(amount)


class SavingsAccount(BankAccount):
    def show_type(self):
        print("Savings Account")


class CurrentAccount(BankAccount):
    def show_type(self):
        print("Current Account")


class Customer:
    def __init__(self, name):
        self.name = name

    def show_customer(self):
        print("Customer:", self.name)


class PaymentService:
    def make_payment(self, amount):
        print("Payment successful:", amount)


class Bank:
    def __init__(self):
        self.customers = [
            Customer("Jaya"),
            Customer("Ravi")
        ]


bank = Bank()
account = SavingsAccount(10000)
payment = PaymentService()

for customer in bank.customers:
    customer.show_customer()

account.show_type()
account.show_balance()
account.pay(payment, 2000)