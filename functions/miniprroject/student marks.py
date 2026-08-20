students = {}

def add_student():
    roll = input("Enter roll number: ")
    name = input("Enter student name: ")
    marks = float(input("Enter marks: "))

    students[roll] = {
        "name": name,
        "marks": marks
    }

    print("Student added successfully.")

def search_student():
    roll = input("Enter roll number: ")

    if roll in students:
        print("Name:", students[roll]["name"])
        print("Marks:", students[roll]["marks"])
    else:
        print("Student not found.")

def update_student():
    roll = input("Enter roll number: ")

    if roll in students:
        students[roll]["name"] = input("Enter new name: ")
        students[roll]["marks"] = float(input("Enter new marks: "))
        print("Student updated.")
    else:
        print("Student not found.")

def delete_student():
    roll = input("Enter roll number: ")

    if roll in students:
        del students[roll]
        print("Student deleted.")
    else:
        print("Student not found.")

def display_students():
    if not students:
        print("No students available.")
        return

    for roll, data in students.items():
        print("\nRoll:", roll)
        print("Name:", data["name"])
        print("Marks:", data["marks"])


while True:
    print("\n--- Student Management ---")
    print("1. Add Student")
    print("2. Search Student")
    print("3. Update Student")
    print("4. Delete Student")
    print("5. Display Students")
    print("6. Exit")

    choice = int(input("Enter choice: "))

    if choice == 1:
        add_student()
    elif choice == 2:
        search_student()
    elif choice == 3:
        update_student()
    elif choice == 4:
        delete_student()
    elif choice == 5:
        display_students()
    elif choice == 6:
        break
    else:
        print("Invalid choice")