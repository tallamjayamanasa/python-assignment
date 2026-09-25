class Manager:
    def calculate_salary(self): return 60000
class Developer:
    def calculate_salary(self): return 50000
class Tester:
    def calculate_salary(self): return 40000
class Intern:
    def calculate_salary(self): return 15000
def show(e): print(e.__class__.__name__,e.calculate_salary())
for x in [Manager(),Developer(),Tester(),Intern()]: show(x)
