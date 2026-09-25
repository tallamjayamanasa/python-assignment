class Product:
    def __init__(self,price): self.price=price
    def __add__(self,other): return self.price+other.price
print("Combined price:", Product(100)+Product(250))
