class Student:
    def __init__(self, name):
        self.name = name

student1 = Student("Jaya")
student2 = student1
student3 = Student("Jaya")

print(student1 is student2)
print(student1 is student3)