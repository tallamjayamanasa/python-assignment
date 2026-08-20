class Calculator:
    def add(self, a, b):
        return a + b

    def display_result(self, a, b):
        result = self.add(a, b)
        print("Result:", result)


calculator = Calculator()

calculator.display_result(20, 30)