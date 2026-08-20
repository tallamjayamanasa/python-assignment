from abc import ABC, abstractmethod


class Delivery(ABC):

    def __init__(self, distance):
        self.distance = distance

    @abstractmethod
    def calculate_charge(self):
        pass

    def display_distance(self):
        print("Distance:", self.distance, "km")


class StandardDelivery(Delivery):

    def calculate_charge(self):
        return self.distance * 20


class ExpressDelivery(Delivery):

    def calculate_charge(self):
        return self.distance * 40


class SameDayDelivery(Delivery):

    def calculate_charge(self):
        return self.distance * 60


deliveries = [
    StandardDelivery(5),
    ExpressDelivery(5),
    SameDayDelivery(5)
]

for delivery in deliveries:
    delivery.display_distance()
    print("Delivery Charge:", delivery.calculate_charge())
    print()