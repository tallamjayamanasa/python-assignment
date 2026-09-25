class Teacher:
    def teach(self):
        print("Teacher is teaching")

class Student:
    def study(self):
        print("Student is studying")

class School:
    def __init__(self):
        self.teacher = Teacher()
        self.student = Student()

    def show(self):
        self.teacher.teach()
        self.student.study()

school = School()
school.show()