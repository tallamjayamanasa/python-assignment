class Bird:
    def move(self): print("Bird flies")
class Dog:
    def move(self): print("Dog walks")
class Fish:
    def move(self): print("Fish swims")

for x in [Bird(), Dog(), Fish()]: x.move()
