class Department:
    def __init__(self, name):
        self.name = name

    def show_department(self):
        print("Department:", self.name)


class Employee:
    def __init__(self, name):
        self.name = name

    def show_employee(self):
        print("Employee:", self.name)


class PayrollService:
    def process_salary(self):
        print("Salary processed")


class Company:
    def __init__(self):
        self.departments = [
            Department("IT"),
            Department("HR")
        ]

        self.employees = [
            Employee("Jaya"),
            Employee("Ravi")
        ]

    def show_details(self):
        for department in self.departments:
            department.show_department()

        for employee in self.employees:
            employee.show_employee()

    def process_payroll(self, payroll_service):
        payroll_service.process_salary()


company = Company()
payroll = PayrollService()

company.show_details()
company.process_payroll(payroll)