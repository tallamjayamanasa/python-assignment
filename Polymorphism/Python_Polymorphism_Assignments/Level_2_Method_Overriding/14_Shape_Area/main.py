import math
class Shape:
    def area(self): return 0
class Rectangle(Shape):
    def area(self): return 10*5
class Circle(Shape):
    def area(self): return math.pi*3*3
class Triangle(Shape):
    def area(self): return 0.5*8*4

for x in [Rectangle(), Circle(), Triangle()]: print(x.__class__.__name__, round(x.area(),2))
