from abc import ABC, abstractmethod

class Shape(ABC):

    @abstractmethod
    def area(self):
        pass


class Circle(Shape):

    def area(self):
        radius = 5
        return 3.14 * radius * radius


class Rectangle(Shape):

    def area(self):
        length = 10
        breadth = 5
        return length * breadth


class Triangle(Shape):

    def area(self):
        base = 10
        height = 5
        return 0.5 * base * height


shapes = [Circle(), Rectangle(), Triangle()]

for shape in shapes:
    print("Area =", shape.area())