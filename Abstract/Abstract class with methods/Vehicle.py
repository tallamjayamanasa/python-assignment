from abc import ABC, abstractmethod

class Vehicle(ABC):

    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def stop(self):
        pass


class Car(Vehicle):

    def start(self):
        print("Car starts")

    def stop(self):
        print("Car stops")


class Bike(Vehicle):

    def start(self):
        print("Bike starts")

    def stop(self):
        print("Bike stops")


c = Car()
b = Bike()

c.start()
c.stop()

b.start()
b.stop()