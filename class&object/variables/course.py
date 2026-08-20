class Course:
    institute_name = "ABC Institute"

    def __init__(self, course_name, duration):
        self.course_name = course_name
        self.duration = duration

course1 = Course("Python", "3 Months")
course2 = Course("Java", "4 Months")
course3 = Course("Web Development", "6 Months")

print("Institute:", course1.institute_name)
print("Course:", course1.course_name)
print("Duration:", course1.duration)

print()

print("Institute:", course2.institute_name)
print("Course:", course2.course_name)
print("Duration:", course2.duration)

print()

print("Institute:", course3.institute_name)
print("Course:", course3.course_name)
print("Duration:", course3.duration)