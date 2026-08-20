try:
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))

    result = a / b
    print("Result:", result)

except ValueError:
    print("Error: Invalid numeric input.")

except TypeError:
    print("Error: Invalid data type.")

except ZeroDivisionError:
    print("Error: Cannot divide by zero.")