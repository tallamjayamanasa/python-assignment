class InvalidMarksError(Exception):
    pass


class DuplicateStudentError(Exception):
    pass


class StudentNotFoundError(Exception):
    pass


class StudentManagement:
    def __init__(self):
        self.students = {}

    def add_student(self, student_id, name, marks):
        if student_id in self.students:
            raise DuplicateStudentError("Student ID already exists.")

        if marks < 0 or marks > 100:
            raise InvalidMarksError("Marks must be between 0 and 100.")

        self.students[student_id] = {
            "name": name,
            "marks": marks
        }

        print("Student added successfully.")

    def search_student(self, student_id):
        if student_id not in self.students:
            raise StudentNotFoundError("Student not found.")

        print("Student ID:", student_id)
        print("Name:", self.students[student_id]["name"])
        print("Marks:", self.students[student_id]["marks"])


system = StudentManagement()

try:
    student_id = input("Enter student ID: ")
    name = input("Enter student name: ")
    marks = float(input("Enter marks: "))

    system.add_student(student_id, name, marks)

    search_id = input("Enter ID to search: ")
    system.search_student(search_id)

except (InvalidMarksError, DuplicateStudentError,
        StudentNotFoundError) as e:
    print("Error:", e)

except ValueError:
    print("Error: Enter valid marks.")