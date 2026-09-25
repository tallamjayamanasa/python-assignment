
#Convert a string into a list of characters.

text = "Python"

characters = list(text)

print(characters)

#Convert a list of characters into a string.

characters = ['P', 'y', 't', 'h', 'o', 'n']

text = "".join(characters)

print(text)

#Create a sentence and split it into a list of words.

sentence = "I am learning Python"

words = sentence.split()

print(words)

#Create a list of words and join them into a single sentence using join().

words = ["I", "love", "Python"]

sentence = " ".join(words)

print(sentence)

#Create a sentence and create a list containing only words with more than 5 characters.

sentence = "Python programming is very interesting"

words = sentence.split()

result = []

for word in words:
    if len(word) > 5:
        result.append(word)

print(result)

#Create a sentence and count the frequency of each word.

sentence = "python is easy and python is powerful"

words = sentence.split()

frequency = {}

for word in words:
    if word in frequency:
        frequency[word] += 1
    else:
        frequency[word] = 1

print(frequency)

#Create a list of names and join them into a single string separated by commas.

names = ["Jaya", "Manasa", "Bhavani", "Hasini"]

result = ", ".join(names)

print(result)

#Create a sentence and remove duplicate words.

sentence = "Python is easy Python is powerful"

words = sentence.split()

result = []

for word in words:
    if word not in result:
        result.append(word)

print(" ".join(result))


#Create a sentence and display the words in alphabetical order.

sentence = "banana apple mango orange"

words = sentence.split()

words.sort()

print(words)

#Create a sentence and find the longest and shortest words.

sentence = "Python is a powerful language"

words = sentence.split()

longest = words[0]
shortest = words[0]

for word in words:
    if len(word) > len(longest):
        longest = word

    if len(word) < len(shortest):
        shortest = word

print("Longest word:", longest)
print("Shortest word:", shortest)
