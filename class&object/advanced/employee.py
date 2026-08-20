class Employee:
    def __init__(self, name, monthly_salary):
        self.name = name
        self.monthly_salary = monthly_salary

    def annual_salary(self):
        return self.monthly_salary * 12

    def display(self):
        print("Name:", self.name)
        print("Monthly Salary:", self.monthly_salary)
        print("Annual Salary:", self.annual_salary())


employee = Employee("Rahul", 30000)

employee.display()