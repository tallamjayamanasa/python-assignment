try:
    value = input("Enter a number: ")
    number = int(value)

    print("Integer value:", number)

except ValueError:
    print("Error: Cannot convert the string into an integer.")