from abc import ABC, abstractmethod

class Food(ABC):
    @abstractmethod
    def prepare(self):
        pass

class Pizza(Food):
    def prepare(self):
        print("Pizza is being prepared")

class Burger(Food):
    def prepare(self):
        print("Burger is being prepared")

p = Pizza()
b = Burger()

p.prepare()
b.prepare()