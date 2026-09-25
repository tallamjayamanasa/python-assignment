class Circle:
    def area(self): return 3.14*3*3
class Rectangle:
    def area(self): return 10*5
def calculate_area(shape): print("Area:", round(shape.area(),2))
for x in [Circle(), Rectangle()]: calculate_area(x)
