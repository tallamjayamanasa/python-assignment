#Check whether a string contains only numbers using isdigit()

text = "12345"

if text.isdigit():
     print("String contains only numbers")
else:
    print("String does not contain only numbers")

#Check whether a string contains alphabets and numbers using isalnum()

text = "Python123"

if text.isalnum():
    print("String contains only alphabets and numbers")
else:
    print("String contains special characters")

#Check whether a string contains spaces using isspace()

text = "     "

if text.isspace():
    print("String contains only spaces")
else:
    print("String does not contain only spaces")

#Check whether a string contains lowercase letters using islower()

text = "python"

if text.islower():
    print("String is in lowercase")
else:
    print("String is not in lowercase")

#Check whether a string contains uppercase letters using isupper()

text = "PYTHON"

if text.isupper():
    print("String is in uppercase")
else:
    print("String is not in uppercase")

#Check whether a string is in title case using istitle()

text = "Python Programming"

if text.istitle():

    print("String is in title case")
else:
    print("String is not in title case")

#Ask the user to enter a username and check whether it contains only alphabets and numbers

username = input("Enter username: ")

if username.isalnum():
    print("Valid username")
else:
    print("Invalid username")

#Ask the user to enter a password and check whether it contains at least one digit

password = input("Enter password: ")

has_digit = False

for ch in password:
    if ch.isdigit():
        has_digit = True
        break

if has_digit:
    print("Password contains at least one digit")
else:
    print("Password does not contain a digit")

#Ask the user to enter a string and check whether it is empty or contains characters

text = input("Enter a string: ")

if text == "":
    print("String is empty")
else:
    print("String contains characters")

#Ask the user to enter an email address and check whether it contains "@" and "."


email = input("Enter email address: ")

if "@" in email and "." in email:
    print("Valid email format")
else:
    print("Invalid email format")
    