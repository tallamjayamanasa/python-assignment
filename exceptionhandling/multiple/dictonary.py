student = {
    "name": "Jaya",
    "age": 18,
    "course": "Python"
}

try:
    key = input("Enter dictionary key: ")

    if key == "":
        raise ValueError("Key cannot be empty.")

    print("Value:", student[key])

except ValueError as e:
    print("Error:", e)

except KeyError:
    print("Error: Key does not exist.")

except TypeError:
    print("Error: Invalid key type.")