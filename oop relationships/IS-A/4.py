class Employee:
    def work(self):
        print("Employee is working")

class Manager(Employee):
    def manage(self):
        print("Manager manages the team")

m = Manager()
m.work()
m.manage()