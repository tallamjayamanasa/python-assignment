class Calculator:
    def addition(self, a, b):
        return a + b

    def subtraction(self, a, b):
        return a - b

    def multiplication(self, a, b):
        return a * b

    def division(self, a, b):
        return a / b

calc = Calculator()

print("Addition:", calc.addition(20, 10))
print("Subtraction:", calc.subtraction(20, 10))
print("Multiplication:", calc.multiplication(20, 10))
print("Division:", calc.division(20, 10))