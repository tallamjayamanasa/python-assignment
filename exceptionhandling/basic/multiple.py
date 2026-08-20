try:
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))

    numbers = [10, 20, 30]

    result = a / b
    print("Result:", result)

    index = int(input("Enter index: "))
    print("Element:", numbers[index])

except ValueError:
    print("Error: Please enter valid numbers.")

except ZeroDivisionError:
    print("Error: Cannot divide by zero.")

except IndexError:
    print("Error: Index is out of range.")