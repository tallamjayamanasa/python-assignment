class Employee:
    def work(self):
        print("Employee is working")


class Developer(Employee):
    def work(self):
        print("Developer writes code")


class Manager(Employee):
    def work(self):
        print("Manager manages the team")


class Department:
    def __init__(self, name):
        self.name = name

    def show_department(self):
        print("Department:", self.name)


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
            Developer(),
            Manager()
        ]

    def show_details(self):
        for department in self.departments:
            department.show_department()

        for employee in self.employees:
            employee.work()

    def process_payroll(self, payroll):
        payroll.process_salary()


company = Company()
payroll = PayrollService()

company.show_details()
company.process_payroll(payroll)