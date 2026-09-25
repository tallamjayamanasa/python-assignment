class Rectangle:
    def __init__(self,w,h): self.w,self.h=w,h
    def __eq__(self,other): return self.w*self.h==other.w*other.h
print("Same area:", Rectangle(4,5)==Rectangle(2,10))
