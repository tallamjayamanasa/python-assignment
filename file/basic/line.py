file = open("students.txt", "r")

for line in file:
    print(line, end="")

file.close()