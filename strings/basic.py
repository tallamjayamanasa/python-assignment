#1. Create a string containing your name and print it.

name = "Jaya"
print(name)

#Create a string containing your college name and print its length.

college = "Aditya Polytechnic College"
print(len(college))

#Create a string and print its first character.

text = "Python"
print(text[0])

#Create a string and print its last character.

text = "Python"
print(text[-1])

#Create a string and print the first 5 characters using slicing.

text = "Python Programming"
print(text[:5])

#Create a string and print the last 5 characters using slicing.

text = "Python Programming"
print(text[-5:])

#Create a string and print the string in reverse order.

text = "Python"
print(text[::-1])

#Create two strings and concatenate them.

first = "Hello"
second = "Python"

result = first + " " + second
print(result)

#Create a string and check whether a particular character exists in it.

text = "Python"

if "P" in text:
    print("Character exists")
else:
    print("Character does not exist")

#Create a string and check whether a particular word exists in it.

text = "I am learning Python programming"

if "Python" in text:
    print("Word exists")
else:
    print("Word does not exist")