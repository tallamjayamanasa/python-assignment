import math
class Circle:
    def area(self): return math.pi*3*3
class Rectangle:
    def area(self): return 10*5
class Square:
    def area(self): return 6*6
class Triangle:
    def area(self): return .5*8*4
def show(shape): print(shape.__class__.__name__,round(shape.area(),2))
for x in [Circle(),Rectangle(),Square(),Triangle()]: show(x)
