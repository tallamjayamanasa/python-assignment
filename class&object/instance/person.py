class Person:
    def __init__(self, name, age, city):
        self.name = name
        self.age = age
        self.city = city

person1 = Person("Rahul", 20, "Hyderabad")
person2 = Person("Priya", 19, "Vijayawada")

print("Person 1")
print("Name:", person1.name)
print("Age:", person1.age)
print("City:", person1.city)

print("\nPerson 2")
print("Name:", person2.name)
print("Age:", person2.age)
print("City:", person2.city)