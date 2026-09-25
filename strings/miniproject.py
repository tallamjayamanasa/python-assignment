
#Create a Password Strength Checker using strings.

password = input("Enter password: ")

has_digit = False
has_upper = False
has_lower = False
has_special = False

for ch in password:
    if ch.isdigit():
        has_digit = True
    elif ch.isupper():
        has_upper = True
    elif ch.islower():
        has_lower = True
    else:
        has_special = True

if len(password) >= 8 and has_digit and has_upper and has_lower and has_special:
    print("Strong Password")
elif len(password) >= 6:
    print("Medium Password")
else:
    print("Weak Password")


#Create a Username Validation System using string methods.


username = input("Enter username: ")

if len(username) < 5:
    print("Username must have at least 5 characters")
elif not username.isalnum():
    print("Username must contain only letters and numbers")
elif username[0].isdigit():
    print("Username should not start with a number")
else:
    print("Valid Username")


#Create a Word Frequency Counter that accepts a paragraph and displays the frequency of every word.


paragraph = input("Enter a paragraph: ")

words = paragraph.lower().split()

frequency = {}

for word in words:
    if word in frequency:
        frequency[word] += 1
    else:
        frequency[word] = 1

print("Word Frequency:")

for word in frequency:
    print(word, ":", frequency[word])



#Create a Text Analyzer that displays characters, words, vowels, consonants, digits, spaces, and special characters.

text = input("Enter a sentence: ")

characters = 0
words = len(text.split())
vowels = 0
consonants = 0
digits = 0
spaces = 0
special = 0

for ch in text:

    if ch.isalpha():
        characters += 1

        if ch.lower() in "aeiou":
            vowels += 1
        else:
            consonants += 1

    elif ch.isdigit():
        digits += 1

    elif ch == " ":
        spaces += 1

    else:
        special += 1

print("Characters:", characters)
print("Words:", words)
print("Vowels:", vowels)
print("Consonants:", consonants)
print("Digits:", digits)
print("Spaces:", spaces)
print("Special characters:", special)


#Create a String Menu-Driven Program with options for reverse, palindrome, vowel count, word count, character frequency, uppercase, lowercase, and exit.

text = input("Enter a string: ")

while True:

    print("\n----- STRING MENU -----")
    print("1. Reverse")
    print("2. Palindrome")
    print("3. Vowel Count")
    print("4. Word Count")
    print("5. Character Frequency")
    print("6. Uppercase")
    print("7. Lowercase")
    print("8. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":

        reverse = ""

        for ch in text:
            reverse = ch + reverse

        print("Reverse:", reverse)

    elif choice == "2":

        reverse = ""

        for ch in text:
            reverse = ch + reverse

        if text == reverse:
            print("Palindrome")
        else:
            print("Not a Palindrome")

    elif choice == "3":

        count = 0

        for ch in text:
            if ch.lower() in "aeiou":
                count += 1

        print("Vowels:", count)

    elif choice == "4":

        words = text.split()
        print("Words:", len(words))

    elif choice == "5":

        frequency = {}

        for ch in text:
            if ch in frequency:
                frequency[ch] += 1
            else:
                frequency[ch] = 1

        for ch in frequency:
            print(ch, ":", frequency[ch])

    elif choice == "6":

        print("Uppercase:", text.upper())

    elif choice == "7":

        print("Lowercase:", text.lower())

    elif choice == "8":

        print("Program exited")
        break

    else:

        print("Invalid choice")

