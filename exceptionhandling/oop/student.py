class InvalidMarksError(Exception):
    pass


class Student:
    def __init__(self, name):
        self.name = name
        self.marks = 0

    def set_marks(self, marks):
        try:
            if marks < 0 or marks > 100:
                raise InvalidMarksError(
                    "Marks must be between 0 and 100."
                )

            self.marks = marks
            print("Student:", self.name)
            print("Marks:", self.marks)

        except InvalidMarksError as e:
            print("Error:", e)


student = Student("Jaya")

try:
    marks = float(input("Enter marks: "))
    student.set_marks(marks)

except ValueError:
    print("Error: Enter valid marks.")