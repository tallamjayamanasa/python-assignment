from abc import ABC, abstractmethod


# Abstract Class
class Employee(ABC):

    # Constructor
    def __init__(self, name, employee_id, salary):
        self.name = name
        self.employee_id = employee_id
        self.salary = salary

    # Abstract Method
    @abstractmethod
    def calculate_salary(self):
        pass

    # Concrete Method
    def display_details(self):
        print("Name:", self.name)
        print("Employee ID:", self.employee_id)
        print("Basic Salary:", self.salary)


# Child Class 1
class Manager(Employee):

    def calculate_salary(self):
        bonus = 10000
        return self.salary + bonus


# Child Class 2
class Developer(Employee):

    def calculate_salary(self):
        bonus = 5000
        return self.salary + bonus


# Child Class 3
class Tester(Employee):

    def calculate_salary(self):
        bonus = 3000
        return self.salary + bonus


# Objects
employees = [
    Manager("Ravi", 101, 50000),
    Developer("Anu", 102, 40000),
    Tester("Sita", 103, 30000)
]


# Polymorphism
for employee in employees:

    employee.display_details()

    print("Final Salary:",
          employee.calculate_salary())

    print("----------------------")