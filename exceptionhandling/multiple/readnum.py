try:
    file = open("numbers.txt", "r")

    total = 0

    for line in file:
        try:
            number = int(line.strip())
            total += number
        except ValueError:
            print("Invalid data found:", line.strip())

    file.close()

    print("Total:", total)

except FileNotFoundError:
    print("Error: File not found.")

except PermissionError:
    print("Error: Permission denied.")

finally:
    print("File operation completed.")