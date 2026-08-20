from abc import ABC, abstractmethod

class EmployeePayroll(ABC):

    @abstractmethod
    def calculate_salary(self):
        pass


class FullTimeEmployee(EmployeePayroll):

    def calculate_salary(self):
        print("Full-Time Employee Salary = 50000")


class PartTimeEmployee(EmployeePayroll):

    def calculate_salary(self):
        print("Part-Time Employee Salary = 25000")


class ContractEmployee(EmployeePayroll):

    def calculate_salary(self):
        print("Contract Employee Salary = 35000")


employees = [
    FullTimeEmployee(),
    PartTimeEmployee(),
    ContractEmployee()
]

for employee in employees:
    employee.calculate_salary()