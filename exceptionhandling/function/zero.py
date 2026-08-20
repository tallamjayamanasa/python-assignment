def divide(a, b):
    try:
        result = a / b
        print("Result:", result)

    except ZeroDivisionError:
        print("Error: Cannot divide by zero.")


try:
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))
    divide(a, b)

except ValueError:
    print("Error: Please enter valid numbers.")