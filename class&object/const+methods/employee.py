class Employee:
    def __init__(self, employee_id, name, department, salary):
        self.employee_id = employee_id
        self.name = name
        self.department = department
        self.salary = salary

employee = Employee(101, "Rahul", "IT", 35000)

print("Employee ID:", employee.employee_id)
print("Name:", employee.name)
print("Department:", employee.department)
print("Salary:", employee.salary)