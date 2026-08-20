class Employee:
    company_name = "ABC Technologies"
    employee_count = 0

    def __init__(self, name):
        self.name = name
        Employee.employee_count += 1

employee1 = Employee("Ravi")
employee2 = Employee("Anil")
employee3 = Employee("Sita")

print("Company:", Employee.company_name)
print("Employee Count:", Employee.employee_count)