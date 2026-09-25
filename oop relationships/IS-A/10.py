class Employee:
    def employee_details(self):
        print("Employee is working")

class Developer(Employee):
    def develop(self):
        print("Developer writes code")

class Tester(Employee):
    def test(self):
        print("Tester tests the software")

class Manager(Employee):
    def manage(self):
        print("Manager manages the team")

d = Developer()
d.employee_details()
d.develop()

t = Tester()
t.employee_details()
t.test()

m = Manager()
m.employee_details()
m.manage()