from abc import ABC, abstractmethod

class Employee(ABC):

    @abstractmethod
    def calculate_salary(self):
        pass

    def display_company(self):
        print("Company: ABC Technologies")


class Developer(Employee):

    def calculate_salary(self):
        print("Developer Salary = 50000")


d = Developer()

d.calculate_salary()
d.display_company()