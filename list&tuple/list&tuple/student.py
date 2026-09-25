students = [
    ("Jaya", 85),
    ("Ravi", 70),
    ("Sita", 90),
    ("Kiran", 75)
]

search_name = input("Enter student name: ")

found = False

for name, marks in students:
    if name == search_name:
        print("Student Found")
        print("Name:", name)
        print("Marks:", marks)
        found = True
        break

if not found:
    print("Student Not Found")