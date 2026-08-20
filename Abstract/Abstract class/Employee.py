from abc import ABC, abstractmethod

class Employee(ABC):
    @abstractmethod
    def work(self):
        pass

class Developer(Employee):
    def work(self):
        print("Developer writes code")

class Tester(Employee):
    def work(self):
        print("Tester tests software")

d = Developer()
t = Tester()

d.work()
t.work()