class Student:
    object_count = 0

    def __init__(self, name):
        self.name = name
        Student.object_count += 1

student1 = Student("Jaya")
student2 = Student("Rahul")
student3 = Student("Priya")

print("Total objects:", Student.object_count)