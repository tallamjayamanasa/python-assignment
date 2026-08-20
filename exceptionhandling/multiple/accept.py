numbers = [10, 20, 30, 40, 50]

try:
    index = int(input("Enter index: "))

    if index < 0:
        print("Negative indexes are not allowed.")
    else:
        print("Element:", numbers[index])

except ValueError:
    print("Error: Please enter a valid integer.")

except IndexError:
    print("Error: Index is out of range.")

except TypeError:
    print("Error: Invalid data type.")