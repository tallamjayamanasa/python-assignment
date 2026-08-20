from abc import ABC, abstractmethod

class UniversityCourse(ABC):

    @abstractmethod
    def course_details(self):
        pass


class Engineering(UniversityCourse):

    def course_details(self):
        print("Engineering Course - 4 Years")


class Medical(UniversityCourse):

    def course_details(self):
        print("Medical Course - 5 Years")


class Management(UniversityCourse):

    def course_details(self):
        print("Management Course - 2 Years")


courses = [
    Engineering(),
    Medical(),
    Management()
]

for course in courses:
    course.course_details()