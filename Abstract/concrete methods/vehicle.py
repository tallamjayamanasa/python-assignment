from abc import ABC, abstractmethod

class Vehicle(ABC):

    @abstractmethod
    def start(self):
        pass

    def display_info(self):
        print("Vehicle is used for transportation")


class Car(Vehicle):

    def start(self):
        print("Car starts")


c = Car()

c.start()
c.display_info()