class ReportGenerator:
    def generate_report(self, employee):
        print(f"Generating performance report for {employee.name}.")
        print(f"Department: {employee.department}")
        print(f"Role: {employee.role}")


class Employee:
    def __init__(self, name, department, role):
        self.name = name
        self.department = department
        self.role = role
        self.report_generator = ReportGenerator()

    def create_report(self):
        self.report_generator.generate_report(self)


def run_demo():
    employee = Employee("Maria Gomez", "Engineering", "Team Lead")
    print("Employee -> ReportGenerator example")
    employee.create_report()
    print()
