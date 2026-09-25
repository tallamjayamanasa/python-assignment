#Convert a string to uppercase using upper()

text = "python programming"
print(text.upper())

#Convert a string to lowercase using lower()

text = "PYTHON PROGRAMMING"
print(text.lower())

#convert the first character to uppercase using capitalize()

text = "python programming"
print(text.capitalize())

#Convert the first character of each word to uppercase using title()

text = "python programming"
print(text.title())

#Swap uppercase and lowercase using swapcase()

text = "Hello Python"
print(text.swapcase())

#Remove spaces from beginning and end using strip()

text = "   Hello Python   "
print(text.strip())

#Remove spaces from beginning using lstrip()

text = "   Hello Python   "
print(text.lstrip())

#Remove spaces from end using rstrip()

text = "   Hello Python   "
print(text.rstrip())

#Replace one word with another using replace()

text = "I like Java"
result = text.replace("Java", "Python")
print(result)

#Count how many times a character appears using count()

text = "banana"
print(text.count("a"))

#. Find the position of a character using find()

text = "Python"
print(text.find("t"))

#. Find the position of a word using index()

text = "I am learning Python"
print(text.index("Python"))

#Check if a string starts with a specific character using startswith()

text = "Python is easy"

if text.startswith("Python"):
    print("String starts with Python")
else:
    print("String does not start with Python")

#Check if a string ends with a specific character using endswith()

text = "I am learning Python"

if text.endswith("Python"):
    print("String ends with Python")
else:
    print("String does not end with Python")

#Check whether a string contains only alphabets using isalpha()

text = "Python"

if text.isalpha():
    print("String contains only alphabets")
else:
    print("String contains other characters")


