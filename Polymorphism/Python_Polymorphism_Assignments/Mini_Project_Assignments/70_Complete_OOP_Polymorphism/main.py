from abc import ABC, abstractmethod

# Method overriding
class Animal:
    def sound(self): print("Animal sound")
class Dog(Animal):
    def sound(self): print("Dog: Woof")

# Duck typing
class Duck:
    def walk(self): print("Duck walks")
def make_walk(obj): obj.walk()

# Operator overloading
class Money:
    def __init__(self,amount): self.amount=amount
    def __add__(self,other): return Money(self.amount+other.amount)

# Abstract class
class Payment(ABC):
    @abstractmethod
    def pay(self): pass
class UPI(Payment):
    def pay(self): print("UPI payment")

print("Method Overriding:")
Dog().sound()
print("Duck Typing:")
make_walk(Duck())
print("Operator Overloading:")
print("Total money:",(Money(100)+Money(200)).amount)
print("Abstract Class:")
UPI().pay()
