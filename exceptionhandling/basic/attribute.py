class Student:
    def __init__(self):
        self.name = "Jaya"

student = Student()

try:
    print(student.age)

except AttributeError:
    print("Error: Attribute does not exist.")