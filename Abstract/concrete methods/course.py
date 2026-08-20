from abc import ABC, abstractmethod

class Course(ABC):

    def __init__(self, name, duration):
        self.name = name
        self.duration = duration

    @abstractmethod
    def start(self):
        pass

    def display_course_details(self):
        print("Course:", self.name)
        print("Duration:", self.duration)


class OnlineCourse(Course):

    def start(self):
        print("Online course started")


c = OnlineCourse("Python", "3 Months")

c.start()
c.display_course_details()