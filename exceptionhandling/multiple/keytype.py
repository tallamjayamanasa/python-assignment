student = {
    "name": "Jaya",
    "age": 18,
    "course": "Python"
}

try:
    key = input("Enter dictionary key: ")
    print("Value:", student[key])

except KeyError:
    print("Error: Key not found.")

except TypeError:
    print("Error: Invalid key type.")