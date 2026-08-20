from abc import ABC, abstractmethod

class Shape(ABC):

    def __init__(self, color):
        self.color = color

    @abstractmethod
    def area(self):
        pass


class Circle(Shape):

    def area(self):
        radius = 5
        result = 3.14 * radius * radius
        print("Color:", self.color)
        print("Area of Circle:", result)


c = Circle("Red")
c.area()