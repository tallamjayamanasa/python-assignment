from abc import ABC, abstractmethod

class Shape(ABC):

    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass


class Rectangle(Shape):

    def area(self):
        length = 10
        breadth = 5
        print("Area of Rectangle =", length * breadth)

    def perimeter(self):
        length = 10
        breadth = 5
        print("Perimeter of Rectangle =", 2 * (length + breadth))


class Circle(Shape):

    def area(self):
        radius = 5
        print("Area of Circle =", 3.14 * radius * radius)

    def perimeter(self):
        radius = 5
        print("Perimeter of Circle =", 2 * 3.14 * radius)


r = Rectangle()
c = Circle()

r.area()
r.perimeter()

c.area()
c.perimeter()