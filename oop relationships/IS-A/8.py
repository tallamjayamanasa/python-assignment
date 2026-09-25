class Person:
    def details(self):
        print("Name: Jaya")
        print("Age: 18")

class Student(Person):
    def study(self):
        print("Student is studying")

class Teacher(Person):
    def teach(self):
        print("Teacher is teaching")

s = Student()
s.details()
s.study()

t = Teacher()
t.details()
t.teach()