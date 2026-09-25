class Person:
    def __init__(self, name):
        self.name = name


class Student(Person):
    def study(self):
        print(self.name, "is studying")


class Teacher(Person):
    def teach(self):
        print(self.name, "is teaching")


class Department:
    def __init__(self, name):
        self.name = name

    def show_department(self):
        print("Department:", self.name)


class Course:
    def __init__(self, name):
        self.name = name

    def show_course(self):
        print("Course:", self.name)


class NotificationService:
    def send_notification(self, message):
        print("Notification:", message)


class PaymentService:
    def pay(self, amount):
        print("Payment successful:", amount)


class CertificateGenerator:
    def generate(self, student):
        print("Certificate generated for:", student)


class College:
    def __init__(self):
        self.students = [
            Student("Jaya"),
            Student("Ravi")
        ]

        self.teachers = [
            Teacher("Mr. Kumar"),
            Teacher("Ms. Sita")
        ]

        self.departments = [
            Department("Computer Science"),
            Department("Mechanical")
        ]

        self.courses = [
            Course("Python"),
            Course("Java")
        ]

    def show_details(self):
        print("STUDENTS")
        for student in self.students:
            student.study()

        print("\nTEACHERS")
        for teacher in self.teachers:
            teacher.teach()

        print("\nDEPARTMENTS")
        for department in self.departments:
            department.show_department()

        print("\nCOURSES")
        for course in self.courses:
            course.show_course()

    def send_message(self, notification_service):
        notification_service.send_notification(
            "College will be closed tomorrow"
        )

    def make_payment(self, payment_service):
        payment_service.pay(10000)

    def give_certificate(self, certificate_generator):
        certificate_generator.generate(
            self.students[0].name
        )


college = College()

notification = NotificationService()
payment = PaymentService()
certificate = CertificateGenerator()

college.show_details()

college.send_message(notification)
college.make_payment(payment)
college.give_certificate(certificate)