class Printer:
    def print_details(self, name):
        print("Printing student details:", name)


class Student:
    def __init__(self, name):
        self.name = name

    def print_student(self, printer):
        printer.print_details(self.name)


student = Student("Jaya")
printer = Printer()

student.print_student(printer)