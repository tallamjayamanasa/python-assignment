numbers = [10, 20, 30, 40, 50]

try:
    index = int(input("Enter list index: "))
    print("Element:", numbers[index])

except ValueError:
    print("Error: Please enter an integer.")

except IndexError:
    print("Error: Index is out of range.")