class Student:
    college_name = "Aditya Polytechnic College"

    def __init__(self, student_name):
        self.student_name = student_name

student1 = Student("Jaya")
student2 = Student("Rahul")
student3 = Student("Priya")

print("Student:", student1.student_name)
print("College:", student1.college_name)

print("Student:", student2.student_name)
print("College:", student2.college_name)

print("Student:", student3.student_name)
print("College:", student3.college_name)