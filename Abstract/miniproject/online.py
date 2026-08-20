from abc import ABC, abstractmethod


class Course(ABC):

    def __init__(self, name, duration):
        self.name = name
        self.duration = duration

    @abstractmethod
    def start_course(self):
        pass

    def display_details(self):
        print("Course:", self.name)
        print("Duration:", self.duration)


class OnlineCourse(Course):

    def start_course(self):
        print("Online course started")


class OfflineCourse(Course):

    def start_course(self):
        print("Offline course started")


class HybridCourse(Course):

    def start_course(self):
        print("Hybrid course started")


courses = [
    OnlineCourse("Python", "3 Months"),
    OfflineCourse("Java", "6 Months"),
    HybridCourse("Data Science", "4 Months")
]

for course in courses:
    course.display_details()
    course.start_course()
    print()