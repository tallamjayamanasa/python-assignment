from abc import ABC, abstractmethod

class Course(ABC):

    def __init__(self, course_name, duration):
        self.course_name = course_name
        self.duration = duration

    @abstractmethod
    def start_course(self):
        pass


class OnlineCourse(Course):

    def start_course(self):
        print("Course:", self.course_name)
        print("Duration:", self.duration)
        print("Online course started")


class OfflineCourse(Course):

    def start_course(self):
        print("Course:", self.course_name)
        print("Duration:", self.duration)
        print("Offline course started")


o = OnlineCourse("Python", "3 Months")
f = OfflineCourse("Java", "6 Months")

o.start_course()
f.start_course()