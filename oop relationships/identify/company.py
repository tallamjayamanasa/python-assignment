class Employee:
    def __init__(self, name):
        self.name = name

    def show_employee(self):
        print("Employee:", self.name)


class Company:
    def __init__(self):
        self.employees = [
            Employee("Jaya"),
            Employee("Ravi"),
            Employee("Anu")
        ]

    def show_employees(self):
        for employee in self.employees:
            employee.show_employee()


company = Company()
company.show_employees()