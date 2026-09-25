class Vehicle:
    def start(self):
        print("Vehicle starts")


class Engine:
    def run(self):
        print("Engine is running")


class Car(Vehicle):
    def __init__(self):
        self.engine = Engine()

    def drive(self):
        print("Car is driving")


car = Car()

car.start()
car.engine.run()
car.drive()