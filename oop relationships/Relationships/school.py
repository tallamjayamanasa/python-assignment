class Teacher:
    def __init__(self, name):
        self.name = name

    def show_teacher(self):
        print("Teacher:", self.name)


class Student:
    def __init__(self, name):
        self.name = name

    def show_student(self):
        print("Student:", self.name)


class NotificationService:
    def send_notification(self, message):
        print("Notification:", message)


class School:
    def __init__(self):
        self.teachers = [
            Teacher("Mr. Kumar"),
            Teacher("Ms. Sita")
        ]

        self.students = [
            Student("Jaya"),
            Student("Ravi")
        ]

    def show_details(self):
        for teacher in self.teachers:
            teacher.show_teacher()

        for student in self.students:
            student.show_student()

    def notify(self, notification_service):
        notification_service.send_notification(
            "Tomorrow is a holiday"
        )


school = School()
notification = NotificationService()

school.show_details()
school.notify(notification)