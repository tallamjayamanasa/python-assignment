class NotificationService:
    def send(self, student, message):
        print(f"Sending notification to {student.name}: {message}")


class Student:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.notification_service = NotificationService()

    def notify(self, message):
        self.notification_service.send(self, message)


def run_demo():
    student = Student("Brian Smith", "brian@example.com")
    print("Student -> NotificationService example")
    student.notify("Your exam results are ready.")
    print()
