try:
    file = open("newfile.txt", "x")
    file.write("Welcome to Python")
    file.close()

    print("File created successfully")

except FileExistsError:
    print("File already exists")