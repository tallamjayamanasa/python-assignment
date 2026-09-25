from abc import ABC, abstractmethod
class Vehicle(ABC):
    @abstractmethod
    def start(self): pass
    @abstractmethod
    def stop(self): pass
class Car(Vehicle):
    def start(self): print("Car starts")
    def stop(self): print("Car stops")
class Bike(Vehicle):
    def start(self): print("Bike starts")
    def stop(self): print("Bike stops")
class Bus(Vehicle):
    def start(self): print("Bus starts")
    def stop(self): print("Bus stops")
for x in [Car(),Bike(),Bus()]: x.start(); x.stop()
