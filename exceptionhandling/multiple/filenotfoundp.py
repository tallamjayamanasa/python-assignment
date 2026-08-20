try:
    file = open("sample.txt", "r")
    print(file.read())
    file.close()

except FileNotFoundError:
    print("Error: File does not exist.")

except PermissionError:
    print("Error: You do not have permission to access this file.")