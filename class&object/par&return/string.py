class StringOperations:
    def __init__(self, text):
        self.text = text

    def reverse(self):
        return self.text[::-1]

    def count_vowels(self):
        count = 0

        for ch in self.text.lower():
            if ch in "aeiou":
                count += 1

        return count

    def palindrome(self):
        if self.text == self.text[::-1]:
            return True
        else:
            return False


string = StringOperations("madam")

print("Original String:", string.text)
print("Reverse:", string.reverse())
print("Vowels:", string.count_vowels())
print("Palindrome:", string.palindrome())