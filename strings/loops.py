#Write a program to count the number of vowels in a string.

text = input("Enter a string: ")

count = 0

for ch in text:
    if ch.lower() in "aeiou":
        count += 1

print("Number of vowels:", count)

#Write a program to count the number of consonants in a string.

text = input("Enter a string: ")

count = 0

for ch in text:
    if ch.isalpha() and ch.lower() not in "aeiou":
        count += 1

print("Number of consonants:", count)

#Write a program to count the number of digits in a string.

text = input("Enter a string: ")

count = 0

for ch in text:
    if ch.isdigit():
        count += 1

print("Number of digits:", count)

#Write a program to count the number of spaces in a string.

text = input("Enter a string: ")

count = 0

for ch in text:
    if ch == " ":
        count += 1

print("Number of spaces:", count)

#Write a program to count uppercase and lowercase characters separately.

text = input("Enter a string: ")

uppercase = 0
lowercase = 0

for ch in text:
    if ch.isupper():
        uppercase += 1
    elif ch.islower():
        lowercase += 1

print("Uppercase characters:", uppercase)
print("Lowercase characters:", lowercase)

#Write a program to print each character of a string on a separate line.

text = input("Enter a string: ")

for ch in text:
    print(ch)

#Write a program to print only the vowels from a string.

text = input("Enter a string: ")

for ch in text:
    if ch.lower() in "aeiou":
        print(ch)

#Write a program to print only the consonants from a string.

text = input("Enter a string: ")

for ch in text:
    if ch.isalpha() and ch.lower() not in "aeiou":
        print(ch)

#Write a program to remove all spaces from a string without using replace().

text = input("Enter a string: ")

result = ""

for ch in text:
    if ch != " ":
        result += ch

print("String without spaces:", result)

#Write a program to reverse a string without using slicing or reversed().

text = input("Enter a string: ")

result = ""

for ch in text:
    result = ch + result

print("Reversed string:", result)
