class Employee:
    def __init__(self, name, id, salary):
        self.name = name
        self.id = id
        self.salary = salary

employee1 = Employee("Rahul", 101, 30000)

print("Employee Name:", employee1.name)
print("Employee ID:", employee1.id)
print("Salary:", employee1.salary)