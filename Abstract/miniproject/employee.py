from abc import ABC, abstractmethod


class EmployeePayroll(ABC):

    def __init__(self, name, employee_id):
        self.name = name
        self.employee_id = employee_id

    @abstractmethod
    def calculate_salary(self):
        pass

    def display_details(self):
        print("Name:", self.name)
        print("Employee ID:", self.employee_id)


class FullTimeEmployee(EmployeePayroll):

    def calculate_salary(self):
        return 50000


class PartTimeEmployee(EmployeePayroll):

    def calculate_salary(self):
        return 25000


class ContractEmployee(EmployeePayroll):

    def calculate_salary(self):
        return 35000


employees = [
    FullTimeEmployee("Ravi", 101),
    PartTimeEmployee("Anu", 102),
    ContractEmployee("Sita", 103)
]

for employee in employees:
    employee.display_details()
    print("Salary:", employee.calculate_salary())
    print()