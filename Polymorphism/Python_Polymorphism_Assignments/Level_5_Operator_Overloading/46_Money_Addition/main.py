class Money:
    def __init__(self,amount): self.amount=amount
    def __add__(self,other): return Money(self.amount+other.amount)
print("Total:", (Money(500)+Money(250)).amount)
