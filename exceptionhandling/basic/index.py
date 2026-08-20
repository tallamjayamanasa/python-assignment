numbers = [10, 20, 30, 40]

try:
    index = int(input("Enter index: "))
    print("Element:", numbers[index])

except IndexError:
    print("Error: Index is out of range.")