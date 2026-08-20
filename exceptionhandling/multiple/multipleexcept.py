try:
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))

    print("Addition:", a + b)
    print("Subtraction:", a - b)
    print("Multiplication:", a * b)
    print("Division:", a / b)

    numbers = [10, 20, 30]
    index = int(input("Enter list index: "))

    print("List element:", numbers[index])

except ValueError:
    print("Error: Please enter valid integers.")

except ZeroDivisionError:
    print("Error: Cannot divide by zero.")

except IndexError:
    print("Error: List index is out of range.")

except TypeError:
    print("Error: Invalid data type.")

finally:
    print("Program execution completed.")