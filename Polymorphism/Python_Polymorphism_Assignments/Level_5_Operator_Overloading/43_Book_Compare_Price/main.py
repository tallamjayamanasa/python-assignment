class Book:
    def __init__(self,price): self.price=price
    def __gt__(self,other): return self.price>other.price
a,b=Book(500),Book(300)
print("First book is costlier:", a>b)
