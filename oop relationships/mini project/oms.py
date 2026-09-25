class Person:
    def __init__(self, name):
        self.name = name


class Student(Person):
    def study(self):
        print(self.name, "is studying")


class Teacher(Person):
    def teach(self):
        print(self.name, "is teaching")


class NotificationService:
    def send_notification(self, message):
        print("Notification:", message)


class CertificateGenerator:
    def generate(self, student):
        print("Certificate generated for:", student)


class Course:
    def __init__(self, name, teacher, students):
        self.name = name
        self.teacher = teacher
        self.students = students

    def show_course(self):
        print("Course:", self.name)
        print("Teacher:", self.teacher.name)

        for student in self.students:
            print("Student:", student.name)

    def notify(self, service):
        service.send_notification("Course completed")

    def generate_certificate(self, generator, student):
        generator.generate(student.name)


teacher = Teacher("Mr. Kumar")

students = [
    Student("Jaya"),
    Student("Ravi")
]

course = Course("Python", teacher, students)

notification = NotificationService()
certificate = CertificateGenerator()

course.show_course()
course.notify(notification)
course.generate_certificate(certificate, students[0])