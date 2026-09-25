
#Write a program to check whether two strings are anagrams.

str1 = input("Enter first string: ")
str2 = input("Enter second string: ")

if sorted(str1.lower()) == sorted(str2.lower()):
    print("Strings are anagrams")
else:
    print("Strings are not anagrams")

#Write a program to find all duplicate characters in a string.

text = input("Enter a string: ")

duplicates = []

for ch in text:
    if text.count(ch) > 1 and ch not in duplicates:
        duplicates.append(ch)

print("Duplicate characters:", duplicates)

#Write a program to find all unique characters in a string.

text = input("Enter a string: ")

unique = []

for ch in text:
    if text.count(ch) == 1:
        unique.append(ch)

print("Unique characters:", unique)

#Write a program to find the most frequently occurring character.

text = input("Enter a string: ")

max_count = 0
most_frequent = ""

for ch in text:
    count = text.count(ch)

    if count > max_count:
        max_count = count
        most_frequent = ch

print("Most frequent character:", most_frequent)
print("Frequency:", max_count)

#Write a program to capitalize the first letter of every word without using title().

sentence = input("Enter a sentence: ")

words = sentence.split()
result = []

for word in words:
    word = word[0].upper() + word[1:]
    result.append(word)

print("Result:", " ".join(result))


#Write a program to remove punctuation marks from a string.

text = input("Enter a string: ")

result = ""

for ch in text:
    if ch.isalnum() or ch.isspace():
        result += ch

print("After removing punctuation:", result)

#Write a program to extract all numbers from a string.


text = input("Enter a string: ")

numbers = ""

for ch in text:
    if ch.isdigit():
        numbers += ch

print("Numbers:", numbers)

#Write a program to extract all words beginning with a particular letter.


sentence = input("Enter a sentence: ")
letter = input("Enter starting letter: ")

words = sentence.split()

for word in words:
    if word.lower().startswith(letter.lower()):
        print(word)

#Write a program to find the number of words, characters, digits, vowels, and spaces in a sentence.


sentence = input("Enter a sentence: ")

words = sentence.split()

word_count = len(words)
character_count = 0
digit_count = 0
vowel_count = 0
space_count = 0

for ch in sentence:
    if ch.isalpha():
        character_count += 1

    if ch.isdigit():
        digit_count += 1

    if ch.lower() in "aeiou":
        vowel_count += 1

    if ch == " ":
        space_count += 1

print("Number of words:", word_count)
print("Number of characters:", character_count)
print("Number of digits:", digit_count)
print("Number of vowels:", vowel_count)
print("Number of spaces:", space_count)


#Write a program to check whether a string contains only unique characters.

text = input("Enter a string: ")

unique = True

for ch in text:
    if text.count(ch) > 1:
        unique = False
        break

if unique:
    print("String contains only unique characters")
else:
    print("String contains duplicate characters")
