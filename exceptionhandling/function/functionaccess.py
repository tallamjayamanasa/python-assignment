def access_element(numbers, index):
    try:
        print("Element:", numbers[index])

    except IndexError:
        print("Error: Index is out of range.")


numbers = [10, 20, 30, 40, 50]

try:
    index = int(input("Enter index: "))
    access_element(numbers, index)

except ValueError:
    print("Error: Please enter a valid index.")