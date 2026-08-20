class InvalidEnrollmentError(Exception):
    pass


class Course:
    def __init__(self, name, capacity):
        self.name = name
        self.capacity = capacity
        self.students = []

    def enroll(self, student):
        try:
            if student.strip() == "":
                raise InvalidEnrollmentError(
                    "Student name cannot be empty."
                )

            if len(self.students) >= self.capacity:
                raise InvalidEnrollmentError(
                    "Course is full."
                )

            if student in self.students:
                raise InvalidEnrollmentError(
                    "Student is already enrolled."
                )

            self.students.append(student)

            print("Enrollment successful.")
            print("Student:", student)
            print("Course:", self.name)

        except InvalidEnrollmentError as e:
            print("Error:", e)


course = Course("Python Programming", 2)

student = input("Enter student name: ")

course.enroll(student)