class Employee:
    def __init__(self, emp_id, name, salary):
        self.emp_id = emp_id
        self.name = name
        self.salary = salary

    def calculate_annual_salary(self):
        return self.salary * 12

    def display(self):
        print("Employee ID:", self.emp_id)
        print("Name:", self.name)
        print("Monthly Salary:", self.salary)
        print("Annual Salary:", self.calculate_annual_salary())


employees = []

n = int(input("Enter number of employees: "))

for i in range(n):
    emp_id = int(input("Enter employee ID: "))
    name = input("Enter employee name: ")
    salary = float(input("Enter monthly salary: "))

    employees.append(Employee(emp_id, name, salary))

print("\n--- Employee Details ---")

for emp in employees:
    emp.display()
    print("----------------")