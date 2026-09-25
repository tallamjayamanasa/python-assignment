class Food:
    def prepare(self): print("Food is prepared")
class Pizza(Food):
    def prepare(self): print("Pizza is prepared")
class Burger(Food):
    def prepare(self): print("Burger is prepared")
class Biryani(Food):
    def prepare(self): print("Biryani is prepared")

for x in [Pizza(), Burger(), Biryani()]: x.prepare()
