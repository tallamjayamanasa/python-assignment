class Person:
    def show_person(self):
        print("I am a person")

class Student(Person):
    def show_student(self):
        print("I am a student")

s = Student()
s.show_person()
s.show_student()