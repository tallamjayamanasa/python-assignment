from abc import ABC, abstractmethod

class Employee(ABC):

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    @abstractmethod
    def work(self):
        pass


class Manager(Employee):

    def work(self):
        print(self.name, "works as Manager")
        print("Salary:", self.salary)


class Developer(Employee):

    def work(self):
        print(self.name, "works as Developer")
        print("Salary:", self.salary)


class Tester(Employee):

    def work(self):
        print(self.name, "works as Tester")
        print("Salary:", self.salary)


m = Manager("Ravi", 60000)
d = Developer("Anil", 50000)
t = Tester("Sita", 40000)

m.work()
d.work()
t.work()