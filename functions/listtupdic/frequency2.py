def word_frequency(sentence):
    frequency = {}

    words = sentence.split()

    for word in words:
        frequency[word] = frequency.get(word, 0) + 1

    return frequency

sentence = "python is easy python is powerful"
print(word_frequency(sentence))