from abc import ABC, abstractmethod

class Delivery(ABC):

    @abstractmethod
    def calculate_charge(self):
        pass


class StandardDelivery(Delivery):

    def calculate_charge(self):
        return 100


class ExpressDelivery(Delivery):

    def calculate_charge(self):
        return 200


class SameDayDelivery(Delivery):

    def calculate_charge(self):
        return 300


deliveries = [
    StandardDelivery(),
    ExpressDelivery(),
    SameDayDelivery()
]

for delivery in deliveries:
    print("Delivery Charge =", delivery.calculate_charge())