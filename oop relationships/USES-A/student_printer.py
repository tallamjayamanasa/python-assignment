class Printer:
    def print_details(self, student):
        print(f"Student Name: {student.name}")
        print(f"Student ID: {student.student_id}")
        print(f"Grade: {student.grade}")


class Student:
    def __init__(self, name, student_id, grade):
        self.name = name
        self.student_id = student_id
        self.grade = grade
        self.printer = Printer()

    def display_details(self):
        self.printer.print_details(self)


def run_demo():
    student = Student("Alice Johnson", "S101", "A")
    print("Student -> Printer example")
    student.display_details()
    print()
