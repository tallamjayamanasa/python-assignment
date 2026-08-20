def read_file(filename):
    file = None

    try:
        file = open(filename, "r")
        print("File content:")
        print(file.read())

    except FileNotFoundError:
        print("Error: File not found.")

    except PermissionError:
        print("Error: Permission denied.")

    finally:
        if file:
            file.close()
        print("File operation completed.")


filename = input("Enter file name: ")

read_file(filename)