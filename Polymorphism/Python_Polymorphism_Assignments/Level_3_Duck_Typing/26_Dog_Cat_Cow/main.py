class Dog:
    def sound(self): print("Woof")
class Cat:
    def sound(self): print("Meow")
class Cow:
    def sound(self): print("Moo")
def animal_sound(animal): animal.sound()
for x in [Dog(), Cat(), Cow()]: animal_sound(x)
