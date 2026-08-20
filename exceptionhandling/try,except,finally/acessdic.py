student = {
    "name": "Jaya",
    "age": 18,
    "course": "Python"
}

try:
    key = input("Enter key: ")
    print("Value:", student[key])

except KeyError:
    print("Error: Key not found.")

finally:
    print("Dictionary operation completed.")