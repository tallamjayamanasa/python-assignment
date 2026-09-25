
#Write a program to check whether a string is a palindrome.

text = input("Enter a string: ")

reverse = ""

for ch in text:
    reverse = ch + reverse

if text == reverse:
    print("Palindrome")
else:
    print("Not a palindrome")

#Write a program to count the frequency of each character in a string.

text = input("Enter a string: ")

frequency = {}

for ch in text:
    if ch in frequency:
        frequency[ch] += 1
    else:
        frequency[ch] = 1

for ch in frequency:
    print(ch, ":", frequency[ch])

#Write a program to find the first non-repeated character in a string.

text = input("Enter a string: ")

for ch in text:
    if text.count(ch) == 1:
        print("First non-repeated character:", ch)
        break
else:
    print("No non-repeated character")

#Write a program to find the first repeated character in a string.

text = input("Enter a string: ")

for ch in text:
    if text.count(ch) > 1:
        print("First repeated character:", ch)
        break
else:
    print("No repeated character")

#Write a program to remove duplicate characters from a string.

text = input("Enter a string: ")

result = ""

for ch in text:
    if ch not in result:
        result += ch

print("After removing duplicates:", result)

#Write a program to find the largest word in a sentence.

sentence = input("Enter a sentence: ")

words = sentence.split()

largest = words[0]

for word in words:
    if len(word) > len(largest):
        largest = word

print("Largest word:", largest)

#Write a program to find the smallest word in a sentence.

sentence = input("Enter a sentence: ")

words = sentence.split()

smallest = words[0]

for word in words:
    if len(word) < len(smallest):
        smallest = word

print("Smallest word:", smallest)

#Write a program to count the number of words in a sentence without using split().

sentence = input("Enter a sentence: ")

count = 0
in_word = False

for ch in sentence:
    if ch != " " and not in_word:
        count += 1
        in_word = True
    elif ch == " ":
        in_word = False

print("Number of words:", count)

#write a program to reverse each word in a sentence.

sentence = input("Enter a sentence: ")

words = sentence.split()
result = ""

for word in words:
    reverse = ""

    for ch in word:
        reverse = ch + reverse

    result += reverse + " "

print("Result:", result)

#Write a program to reverse the order of words in a sentence.


sentence = input("Enter a sentence: ")

words = sentence.split()
result = ""

for word in words:
    result = word + " " + result

print("Reversed sentence:", result)