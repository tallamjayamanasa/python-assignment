try:
    file = open("sample.txt", "r")

    print("File content:")
    print(file.read())

    file.close()

except FileNotFoundError:
    print("Sorry, the file does not exist.")

finally:
    print("File operation completed.")