class Person:
    def show_person(self):
        print("I am a person")


class Course:
    def show_course(self):
        print("Course: Python")


class Student(Person):
    def __init__(self):
        self.course = Course()

    def study(self):
        print("Student is studying")


student = Student()

student.show_person()
student.course.show_course()
student.study()