from abc import ABC, abstractmethod


class Vehicle(ABC):

    def __init__(self, vehicle_number, brand):
        self.vehicle_number = vehicle_number
        self.brand = brand

    @abstractmethod
    def calculate_rent(self, days):
        pass

    def display_info(self):
        print("Vehicle Number:", self.vehicle_number)
        print("Brand:", self.brand)


class Car(Vehicle):

    def calculate_rent(self, days):
        return days * 1500


class Bike(Vehicle):

    def calculate_rent(self, days):
        return days * 500


class Van(Vehicle):

    def calculate_rent(self, days):
        return days * 2000


vehicles = [
    Car("AP01AB1234", "Toyota"),
    Bike("AP01CD5678", "Honda"),
    Van("AP01EF9012", "Force")
]

days = 3

for vehicle in vehicles:
    vehicle.display_info()
    print("Rent for", days, "days:", vehicle.calculate_rent(days))
    print()