#Create a set containing 5 fruits and print all elements.

fruits = {"apple", "banana", "mango", "orange", "grapes"}

print(fruits)


#Create a set of numbers and find its length.

numbers = {10, 20, 30, 40, 50}

print("Length:", len(numbers))

#Create a set and add a new element using `add()`.

numbers = {10, 20, 30}

numbers.add(40)

print(numbers)

#Create a set and add multiple elements using `update()`.

numbers = {10, 20, 30}

numbers.update([40, 50, 60])

print(numbers)

#Create a set and remove a specific element using `remove()`.

fruits = {"apple", "banana", "mango"}

fruits.remove("banana")

print(fruits)

#Create a set and remove a specific element using `discard()`.

fruits = {"apple", "banana", "mango"}

fruits.discard("banana")

print(fruits)

#Create a set and remove an element using `pop()`.

numbers = {10, 20, 30, 40}

removed = numbers.pop()

print("Removed element:", removed)
print("Remaining set:", numbers)

#Create a set of numbers and check whether a particular number exists.

numbers = {10, 20, 30, 40, 50}

if 30 in numbers:
    print("30 exists in the set")
else:
    print("30 does not exist")

#Create two sets and find their union.

set1 = {1, 2, 3}
set2 = {3, 4, 5}

result = set1.union(set2)

print("Union:", result)

#Create two sets and find their intersection.

set1 = {1, 2, 3}
set2 = {3, 4, 5}

result = set1.intersection(set2)

print("Intersection:", result)

#Create two sets and find their difference.

set1 = {1, 2, 3}
set2 = {3, 4, 5}

result = set1.difference(set2)

print("Difference:", result)

#Create two sets and find their symmetric difference.

set1 = {1, 2, 3}
set2 = {3, 4, 5}

result = set1.symmetric_difference(set2)

print("Symmetric Difference:", result)

#Create two sets and check whether one set is a subset of another set.

set1 = {1, 2}
set2 = {1, 2, 3, 4}

if set1.issubset(set2):
    print("set1 is a subset of set2")
else:
    print("set1 is not a subset of set2")

#Create two sets and check whether one set is a superset of another set.

set1 = {1, 2, 3, 4}
set2 = {1, 2}

if set1.issuperset(set2):
    print("set1 is a superset of set2")
else:
    print("set1 is not a superset of set2")

#Create a list containing duplicate values and convert it into a set to remove duplicates.

numbers = [10, 20, 10, 30, 20, 40, 30]

print("Original list:", numbers)

unique_numbers = set(numbers)

print("Set without duplicates:", unique_numbers)