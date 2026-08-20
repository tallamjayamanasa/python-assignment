class Employee:
    def __init__(self, name, monthly_salary):
        self.name = name
        self.monthly_salary = monthly_salary

    def annual_salary(self):
        return self.monthly_salary * 12

employee = Employee("Rahul", 30000)

print("Employee Name:", employee.name)
print("Monthly Salary:", employee.monthly_salary)
print("Annual Salary:", employee.annual_salary())