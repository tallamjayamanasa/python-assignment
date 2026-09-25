class Car:
    def start(self): print("Car starts")
class Bike:
    def start(self): print("Bike starts")
class Bus:
    def start(self): print("Bus starts")
class Truck:
    def start(self): print("Truck starts")
def start(v): v.start()
for x in [Car(),Bike(),Bus(),Truck()]: start(x)
