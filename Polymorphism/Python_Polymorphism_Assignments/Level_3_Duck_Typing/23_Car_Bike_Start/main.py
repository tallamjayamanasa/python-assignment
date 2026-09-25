class Car:
    def start(self): print("Car started")
class Bike:
    def start(self): print("Bike started")
def start_vehicle(obj): obj.start()
for x in [Car(), Bike()]: start_vehicle(x)
