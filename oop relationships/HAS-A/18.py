class Department:
    def __init__(self, name):
        self.name = name

    def show_department(self):
        print("Department:", self.name)

class Company:
    def __init__(self):
        self.departments = [
            Department("IT"),
            Department("HR"),
            Department("Finance")
        ]

    def show_departments(self):
        for department in self.departments:
            department.show_department()

company = Company()
company.show_departments()