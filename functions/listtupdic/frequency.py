def character_frequency(text):
    frequency = {}

    for char in text:
        frequency[char] = frequency.get(char, 0) + 1

    return frequency

text = "hello"
print(character_frequency(text))