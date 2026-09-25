name = input("Enter student name: ")
age = int(input("Enter age: "))
marks = float(input("Enter marks: "))

if age >= 17 and marks >= 60:
    print(name, "is eligible")
else:
    print(name, "is not eligible")