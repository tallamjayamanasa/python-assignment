file = None

try:
    file = open("sample.txt", "r")

except FileNotFoundError:
    print("Error: File not found.")

else:
    print("File content:")
    print(file.read())

finally:
    if file:
        file.close()
    print("File operation completed.")