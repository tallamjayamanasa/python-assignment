class Student:
    college_name = "Aditya Polytechnic College"   # Class variable

    def __init__(self, name, age):
        self.name = name       # Instance variable
        self.age = age         # Instance variable


student1 = Student("Jaya", 18)
student2 = Student("Rahul", 19)

print("Student 1:")
print("Name:", student1.name)
print("Age:", student1.age)
print("College:", student1.college_name)

print("\nStudent 2:")
print("Name:", student2.name)
print("Age:", student2.age)
print("College:", student2.college_name)