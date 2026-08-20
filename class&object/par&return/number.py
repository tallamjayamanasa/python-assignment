class Number:
    def __init__(self, number):
        self.number = number

    def even_or_odd(self):
        if self.number % 2 == 0:
            return "Even"
        else:
            return "Odd"

    def prime(self):
        if self.number < 2:
            return False

        for i in range(2, self.number):
            if self.number % i == 0:
                return False

        return True

    def palindrome(self):
        value = str(self.number)

        if value == value[::-1]:
            return True
        else:
            return False


number = Number(121)

print("Number:", number.number)
print("Even/Odd:", number.even_or_odd())
print("Prime:", number.prime())
print("Palindrome:", number.palindrome())