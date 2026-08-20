try:
    number = int(input("Enter a number: "))

except ValueError:
    print("Error: Please enter a valid number.")

else:
    print("Square:", number * number)