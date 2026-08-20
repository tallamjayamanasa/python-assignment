from abc import ABC, abstractmethod

class Employee(ABC):

    def __init__(self, name, employee_id):
        self.name = name
        self.employee_id = employee_id

    @abstractmethod
    def calculate_salary(self):
        pass


class Developer(Employee):

    def calculate_salary(self):
        print("Employee Name:", self.name)
        print("Employee ID:", self.employee_id)
        print("Salary: 40000")


d = Developer("Ravi", 101)
d.calculate_salary()