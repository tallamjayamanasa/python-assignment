from abc import ABC, abstractmethod
class Employee(ABC):
    @abstractmethod
    def calculate_salary(self): pass
class Manager(Employee):
    def calculate_salary(self): return 60000
class Developer(Employee):
    def calculate_salary(self): return 50000
for x in [Manager(),Developer()]: print(x.__class__.__name__,x.calculate_salary())
