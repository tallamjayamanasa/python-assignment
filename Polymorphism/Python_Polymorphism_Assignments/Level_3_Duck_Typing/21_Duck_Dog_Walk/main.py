class Duck:
    def walk(self): print("Duck walks")
class Dog:
    def walk(self): print("Dog walks")
def make_walk(obj): obj.walk()
for x in [Duck(), Dog()]: make_walk(x)
