# r mode
file = open("data.txt", "r")
print(file.read())
file.close()

# w mode
file = open("data.txt", "w")
file.write("New Data")
file.close()

# a mode
file = open("data.txt", "a")
file.write("\nMore Data")
file.close()