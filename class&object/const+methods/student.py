class Student:
    def __init__(self, name, age, course, marks):
        self.name = name
        self.age = age
        self.course = course
        self.marks = marks

student = Student("Jaya", 18, "CCN", 85)

print("Name:", student.name)
print("Age:", student.age)
print("Course:", student.course)
print("Marks:", student.marks)