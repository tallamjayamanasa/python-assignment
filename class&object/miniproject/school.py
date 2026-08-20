class Student:
    def __init__(self, student_id, name):
        self.student_id = student_id
        self.name = name

    def display(self):
        print("Student ID:", self.student_id)
        print("Student Name:", self.name)


class Teacher:
    def __init__(self, teacher_id, name, subject):
        self.teacher_id = teacher_id
        self.name = name
        self.subject = subject

    def display(self):
        print("Teacher ID:", self.teacher_id)
        print("Teacher Name:", self.name)
        print("Subject:", self.subject)


class Course:
    def __init__(self, course_id, course_name):
        self.course_id = course_id
        self.course_name = course_name

    def display(self):
        print("Course ID:", self.course_id)
        print("Course Name:", self.course_name)


student = Student(1, "Anjali")
teacher = Teacher(101, "Ramesh", "Python")
course = Course(201, "Computer Science")

student.display()
print()

teacher.display()
print()

course.display()