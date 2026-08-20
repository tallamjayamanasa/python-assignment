class Student:
    college_name = "Aditya Polytechnic College"

    def __init__(self, name):
        self.name = name

student1 = Student("Jaya")
student2 = Student("Rahul")
student3 = Student("Priya")

print(student1.name, student1.college_name)
print(student2.name, student2.college_name)
print(student3.name, student3.college_name)