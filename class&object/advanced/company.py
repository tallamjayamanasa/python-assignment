class Company:
    def __init__(self, company_name):
        self.company_name = company_name
        self.employees = []

    def add_employee(self, name):
        self.employees.append(name)
        print(name, "added successfully")

    def remove_employee(self, name):
        if name in self.employees:
            self.employees.remove(name)
            print(name, "removed successfully")
        else:
            print(name, "not found")

    def search_employee(self, name):
        if name in self.employees:
            print(name, "is found")
        else:
            print(name, "is not found")

    def display_employees(self):
        print("\nEmployees in", self.company_name)

        for employee in self.employees:
            print(employee)


company = Company("ABC Technologies")

company.add_employee("Jaya")
company.add_employee("Rahul")
company.add_employee("Priya")
company.add_employee("Anil")

company.display_employees()

company.search_employee("Rahul")

company.remove_employee("Priya")

company.display_employees()