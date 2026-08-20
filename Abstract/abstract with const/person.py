from abc import ABC, abstractmethod

class Person(ABC):

    def __init__(self, name, age):
        self.name = name
        self.age = age

    @abstractmethod
    def role(self):
        pass


class Student(Person):

    def role(self):
        print(self.name, "is a Student")
        print("Age:", self.age)


class Teacher(Person):

    def role(self):
        print(self.name, "is a Teacher")
        print("Age:", self.age)


class Doctor(Person):

    def role(self):
        print(self.name, "is a Doctor")
        print("Age:", self.age)


s = Student("Rahul", 20)
t = Teacher("Priya", 35)
d = Doctor("Arun", 40)

s.role()
t.role()
d.role()