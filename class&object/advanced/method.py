class Student:
    def __init__(self, name, course):
        self.name = name
        self.course = course

    def get_info(self):
        return self.name + " - " + self.course


class College:
    def __init__(self, college_name, student):
        self.college_name = college_name
        self.student = student

    def student_information(self):
        return self.student.get_info()


student = Student("Jaya", "CCN")

college = College("Aditya Polytechnic College", student)

print("College:", college.college_name)
print("Student Information:", college.student_information())