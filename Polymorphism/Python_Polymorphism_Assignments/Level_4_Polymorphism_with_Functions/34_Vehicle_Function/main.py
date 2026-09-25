class Car:
    def start(self): print("Car started")
class Bike:
    def start(self): print("Bike started")
def start_vehicle(v): v.start()
for x in [Car(), Bike()]: start_vehicle(x)
