class ShoppingCart:
    def __init__(self,items): self.items=items
    def __add__(self,other): return ShoppingCart(self.items+other.items)
cart=ShoppingCart(["Book","Pen"])+ShoppingCart(["Bag"])
print("Combined cart:", cart.items)
