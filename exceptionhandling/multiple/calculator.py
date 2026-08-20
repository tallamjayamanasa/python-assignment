try:
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))

    operator = input("Enter operator (+, -, *, /): ")

    if operator == "+":
        print("Result:", a + b)

    elif operator == "-":
        print("Result:", a - b)

    elif operator == "*":
        print("Result:", a * b)

    elif operator == "/":
        print("Result:", a / b)

    else:
        print("Error: Invalid operator.")

except ValueError:
    print("Error: Please enter valid numbers.")

except ZeroDivisionError:
    print("Error: Cannot divide by zero.")

except TypeError:
    print("Error: Invalid data type.")