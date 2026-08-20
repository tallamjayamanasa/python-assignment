class Car:
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price

    def start(self):
        print("Car Started")

    def stop(self):
        print("Car Stopped")

    def display(self):
        print("Brand:", self.brand)
        print("Model:", self.model)
        print("Price:", self.price)

car = Car("Toyota", "Innova", 2500000)

car.display()
car.start()
car.stop()