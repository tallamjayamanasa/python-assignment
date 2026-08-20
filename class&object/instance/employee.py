class Employee:
    def __init__(self, name, department, salary):
        self.name = name
        self.department = department
        self.salary = salary

employee1 = Employee("Ravi", "HR", 30000)
employee2 = Employee("Anil", "IT", 45000)
employee3 = Employee("Sneha", "Finance", 40000)
employee4 = Employee("Priya", "Marketing", 35000)
employee5 = Employee("Kiran", "IT", 50000)

print(employee1.name, employee1.department, employee1.salary)
print(employee2.name, employee2.department, employee2.salary)
print(employee3.name, employee3.department, employee3.salary)
print(employee4.name, employee4.department, employee4.salary)
print(employee5.name, employee5.department, employee5.salary)