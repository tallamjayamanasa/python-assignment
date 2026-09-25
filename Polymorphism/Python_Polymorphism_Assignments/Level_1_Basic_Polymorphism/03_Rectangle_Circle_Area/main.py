import math
class Rectangle:
    def area(self): return 10 * 5
class Circle:
    def area(self): return math.pi * 3 * 3

for s in [Rectangle(), Circle()]: print("Area:", round(s.area(), 2))
