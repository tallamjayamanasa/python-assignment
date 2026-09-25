class Temperature:
    def __init__(self,c): self.c=c
    def __gt__(self,other): return self.c>other.c
print("Temperature 1 is higher:", Temperature(35)>Temperature(30))
