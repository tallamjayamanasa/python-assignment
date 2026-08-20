class Student:
    student_count = 0

    def __init__(self, name):
        self.name = name
        Student.student_count += 1


student1 = Student("Jaya")
student2 = Student("Rahul")
student3 = Student("Priya")
student4 = Student("Anil")

print("Student 1:", student1.name)
print("Student 2:", student2.name)
print("Student 3:", student3.name)
print("Student 4:", student4.name)

print("Total Students:", Student.student_count)