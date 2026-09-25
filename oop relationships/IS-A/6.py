class Vehicle:
    def start(self):
        print("Vehicle starts")

class Car(Vehicle):
    def type(self):
        print("This is a Car")

class Bike(Vehicle):
    def type(self):
        print("This is a Bike")

class Bus(Vehicle):
    def type(self):
        print("This is a Bus")

c = Car()
b = Bike()
bus = Bus()

c.start()
c.type()

b.start()
b.type()

bus.start()
bus.type()