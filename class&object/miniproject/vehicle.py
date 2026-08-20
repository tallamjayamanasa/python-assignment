class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def display(self):
        print("Brand:", self.brand)
        print("Model:", self.model)


class Car(Vehicle):
    def __init__(self, brand, model, doors):
        super().__init__(brand, model)
        self.doors = doors

    def display(self):
        super().display()
        print("Doors:", self.doors)


class Bike(Vehicle):
    def __init__(self, brand, model, engine):
        super().__init__(brand, model)
        self.engine = engine

    def display(self):
        super().display()
        print("Engine:", self.engine)


class Truck(Vehicle):
    def __init__(self, brand, model, capacity):
        super().__init__(brand, model)
        self.capacity = capacity

    def display(self):
        super().display()
        print("Capacity:", self.capacity)


car = Car("Toyota", "Innova", 4)
bike = Bike("Honda", "Shine", "125cc")
truck = Truck("Tata", "Prima", "20 Tons")

print("--- Car ---")
car.display()

print("\n--- Bike ---")
bike.display()

print("\n--- Truck ---")
truck.display()