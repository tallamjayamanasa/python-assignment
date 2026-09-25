class Student:
    def __init__(self, name):
        self.name = name

    def show_student(self):
        print("Student:", self.name)

class College:
    def __init__(self):
        self.students = [
            Student("Jaya"),
            Student("Ravi"),
            Student("Anu")
        ]

    def show_students(self):
        for student in self.students:
            student.show_student()

college = College()
college.show_students()