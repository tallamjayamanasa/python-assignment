class Calculator:
    def addition(self, a, b):
        return a + b

    def subtraction(self, a, b):
        return a - b

    def multiplication(self, a, b):
        return a * b

    def division(self, a, b):
        return a / b

calculator = Calculator()

print("Addition:", calculator.addition(20, 10))
print("Subtraction:", calculator.subtraction(20, 10))
print("Multiplication:", calculator.multiplication(20, 10))
print("Division:", calculator.division(20, 10))