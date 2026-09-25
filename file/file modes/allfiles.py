# Create and write data
file = open("student.txt", "w")
file.write("Name: Jaya Manasa\n")
file.write("Course: Diploma CCN\n")
file.close()

# Read data
file = open("student.txt", "r")
print("Existing Data:")
print(file.read())
file.close()

# Append new data
file = open("student.txt", "a")
file.write("College: Aditya Polytechnic College\n")
file.close()

# Read updated data
file = open("student.txt", "r")
print("Updated Data:")
print(file.read())
file.close()