class Distance:
    def __init__(self,meters): self.meters=meters
    def __add__(self,other): return Distance(self.meters+other.meters)
print((Distance(5)+Distance(7)).meters, "meters")
