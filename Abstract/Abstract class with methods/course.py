from abc import ABC, abstractmethod

class Course(ABC):

    @abstractmethod
    def start_course(self):
        pass

    @abstractmethod
    def get_duration(self):
        pass


class OnlineCourse(Course):

    def start_course(self):
        print("Online course started")

    def get_duration(self):
        print("Online course duration = 3 months")


class OfflineCourse(Course):

    def start_course(self):
        print("Offline course started")

    def get_duration(self):
        print("Offline course duration = 6 months")


o = OnlineCourse()
f = OfflineCourse()

o.start_course()
o.get_duration()

f.start_course()
f.get_duration()