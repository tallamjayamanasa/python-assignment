class Student:
    def display(self): print("Student: Jaya")
class Teacher:
    def display(self): print("Teacher: Python")

for x in [Student(), Teacher()]: x.display()
