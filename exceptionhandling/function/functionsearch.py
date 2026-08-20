def search_key(student, key):
    try:
        print("Value:", student[key])

    except KeyError:
        print("Error: Key not found.")


student = {
    "name": "Jaya",
    "age": 18,
    "course": "Python"
}

key = input("Enter key: ")

search_key(student, key)