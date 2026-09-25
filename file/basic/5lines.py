file = open("students.txt", "r")

for i in range(5):
    line = file.readline()

    if line == "":
        break

    print(line, end="")

file.close()