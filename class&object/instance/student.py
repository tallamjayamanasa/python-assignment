class Student:
    def __init__(self, name, age, course):
        self.name = name
        self.age = age
        self.course = course

student1 = Student("Jaya", 18, "CCN")
student2 = Student("Rahul", 19, "CSE")
student3 = Student("Priya", 18, "ECE")

print(student1.name, student1.age, student1.course)
print(student2.name, student2.age, student2.course)
print(student3.name, student3.age, student3.course)