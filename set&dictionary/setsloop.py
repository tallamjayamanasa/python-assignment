
#Create a set of numbers and print only the even numbers.

fruits = {"apple", "banana", "mango", "orange", "grapes"}

print(fruits) 

#Create a set of numbers and print only the odd numbers.

numbers = {10, 20, 30, 40, 50}

print("Length:", len(numbers))

#Create two sets of student names and find students who are present in both sets.

numbers = {10, 20, 30}

numbers.add(40)

print(numbers)

#Create two sets of student names and find students who are present only in the first set.

students1 = {"Ravi", "Sita", "John", "Anu"}
students2 = {"John", "Anu", "Rahul", "Priya"}

for student in students1:
    if student not in students2:
        print(student)

#Create two sets of numbers and find all unique numbers from both sets.

set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

unique = set()

for num in set1:
    unique.add(num)

for num in set2:
    unique.add(num)

print("Unique numbers:", unique)

#Create a set of numbers and find the largest number without using max().

numbers = {10, 25, 5, 40, 15}

largest = None

for num in numbers:
    if largest is None or num > largest:
        largest = num

print("Largest number:", largest)


#Create a set of numbers and find the smallest number without using min().

numbers = {10, 25, 5, 40, 15}

smallest = None

for num in numbers:
    if smallest is None or num < smallest:
        smallest = num

print("Smallest number:", smallest)

#Create a list of duplicate student names and use a set to display only unique names.

students = ["Ravi", "Sita", "Ravi", "John", "Sita", "Anu"]

unique_students = set()

for student in students:
    unique_students.add(student)

print("Unique students:", unique_students)

#Create two sets representing students enrolled in Python and Java. Find students enrolled in both courses.

python_students = {"Ravi", "Sita", "John", "Anu"}
java_students = {"John", "Anu", "Rahul", "Priya"}

both = set()

for student in python_students:
    if student in java_students:
        both.add(student)

print("Students enrolled in both:", both)

#Create two sets representing students who attended two different events. Find students who attended exactly one even

event1 = {"Ravi", "Sita", "John", "Anu"}
event2 = {"John", "Anu", "Rahul", "Priya"}

exactly_one = set()

for student in event1:
    if student not in event2:
        exactly_one.add(student)

for student in event2:
    if student not in event1:
        exactly_one.add(student)

print("Students who attended exactly one event:", exactly_one)