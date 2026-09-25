class Person:
    def role(self): print("Person")
class Student(Person):
    def role(self): print("Student")
class Teacher(Person):
    def role(self): print("Teacher")
class Doctor(Person):
    def role(self): print("Doctor")

for x in [Student(), Teacher(), Doctor()]: x.role()
