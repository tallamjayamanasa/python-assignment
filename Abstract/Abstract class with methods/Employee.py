from abc import ABC, abstractmethod

class Employee(ABC):

    @abstractmethod
    def calculate_salary(self):
        pass

    @abstractmethod
    def display_details(self):
        pass


class Manager(Employee):

    def calculate_salary(self):
        print("Manager Salary = 50000")

    def display_details(self):
        print("Employee: Manager")


class Developer(Employee):

    def calculate_salary(self):
        print("Developer Salary = 40000")

    def display_details(self):
        print("Employee: Developer")


m = Manager()
d = Developer()

m.display_details()
m.calculate_salary()

d.display_details()
d.calculate_salary()