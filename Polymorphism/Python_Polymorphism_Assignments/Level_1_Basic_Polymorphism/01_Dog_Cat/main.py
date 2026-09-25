class Dog:
    def sound(self): print("Dog says: Woof")

class Cat:
    def sound(self): print("Cat says: Meow")

for animal in [Dog(), Cat()]: animal.sound()
