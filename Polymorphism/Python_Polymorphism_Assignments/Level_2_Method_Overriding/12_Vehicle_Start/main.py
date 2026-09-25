class Vehicle:
    def start(self): print("Vehicle starts")
class Car(Vehicle):
    def start(self): print("Car starts")
class Bike(Vehicle):
    def start(self): print("Bike starts")
class Bus(Vehicle):
    def start(self): print("Bus starts")

for x in [Car(), Bike(), Bus()]: x.start()
