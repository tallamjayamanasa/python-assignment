class Animal:
    def sound(self): print("Animal makes a sound")
class Dog(Animal):
    def sound(self): print("Dog: Woof")
class Cat(Animal):
    def sound(self): print("Cat: Meow")
class Cow(Animal):
    def sound(self): print("Cow: Moo")

for x in [Dog(), Cat(), Cow()]: x.sound()
