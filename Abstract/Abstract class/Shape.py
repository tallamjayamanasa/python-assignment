from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def area(self):
        r = 5
        result = 3.14 * r * r
        print("Area of Circle =", result)

class Rectangle(Shape):
    def area(self):
        length = 10
        breadth = 5
        result = length * breadth
        print("Area of Rectangle =", result)

c = Circle()
r = Rectangle()

c.area()
r.area()