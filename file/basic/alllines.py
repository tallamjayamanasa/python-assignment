file = open("students.txt", "r")

lines = file.readlines()

file.close()

print(lines)