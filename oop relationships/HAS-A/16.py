class Employee:
    def __init__(self, name):
        self.name = name

    def show_employee(self):
        print("Employee:", self.name)

class Department:
    def __init__(self):
        self.employees = [
            Employee("Ravi"),
            Employee("Sita"),
            Employee("Kiran")
        ]

    def show_employees(self):
        for employee in self.employees:
            employee.show_employee()

department = Department()
department.show_employees()