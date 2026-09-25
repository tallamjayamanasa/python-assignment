class Vehicle:
    def show_vehicle(self):
        print("This is a vehicle")


class Car(Vehicle):
    def show_vehicle(self):
        print("This is a car")


class Bike(Vehicle):
    def show_vehicle(self):
        print("This is a bike")


class Customer:
    def __init__(self, name):
        self.name = name


class PaymentService:
    def pay(self, amount):
        print("Rental payment:", amount)


class Rental:
    def __init__(self, customer, vehicle):
        self.customer = customer
        self.vehicle = vehicle

    def show_rental(self):
        print("Customer:", self.customer.name)
        self.vehicle.show_vehicle()

    def make_payment(self, payment):
        payment.pay(2000)


customer = Customer("Jaya")
vehicle = Car()

rental = Rental(customer, vehicle)
payment = PaymentService()

rental.show_rental()
rental.make_payment(payment)