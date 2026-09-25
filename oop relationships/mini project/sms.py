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


class School:
    def __init__(self):
        self.students = [
            Student("Jaya"),
            Student("Ravi")
        ]

        self.teachers = [
            Teacher("Mr. Kumar"),
            Teacher("Ms. Sita")
        ]

    def show_details(self):
        for student in self.students:
            student.study()

        for teacher in self.teachers:
            teacher.teach()

    def notify(self, service):
        service.send_notification("Tomorrow is a holiday")


school = School()
notification = NotificationService()

school.show_details()
school.notify(notification)