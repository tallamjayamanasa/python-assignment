try:
    a = int(input("Enter a number: "))
    b = int(input("Enter another number: "))

    print("Result:", a / b)

except ZeroDivisionError:
    print("Error: Cannot divide by zero.")

finally:
    print("Finally block always executes.")