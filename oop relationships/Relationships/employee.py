class Employee:
    def work(self):
        print("Employee is working")


class Laptop:
    def start(self):
        print("Laptop is started")


class Developer(Employee):
    def __init__(self):
        self.laptop = Laptop()

    def code(self):
        print("Developer is writing code")


developer = Developer()

developer.work()
developer.laptop.start()
developer.code()