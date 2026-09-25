from abc import ABC, abstractmethod
class Shape(ABC):
    @abstractmethod
    def area(self): pass
class Circle(Shape):
    def area(self): return 3.14*3*3
class Rectangle(Shape):
    def area(self): return 10*5
class Triangle(Shape):
    def area(self): return .5*8*4
for x in [Circle(),Rectangle(),Triangle()]: print(x.__class__.__name__, round(x.area(),2))
