students = {}

def add_student():
    name = input("Enter student name: ")

    marks = []

    for i in range(3):
        mark = float(input("Enter mark: "))
        marks.append(mark)

    students[name] = marks
    print("Student added.")

def calculate_result():
    for name, marks in students.items():
        total = sum(marks)
        average = total / len(marks)

        if average >= 90:
            grade = "A"
        elif average >= 75:
            grade = "B"
        elif average >= 60:
            grade = "C"
        elif average >= 40:
            grade = "D"
        else:
            grade = "F"

        status = "Pass" if average >= 40 else "Fail"

        print("\nName:", name)
        print("Total:", total)
        print("Average:", average)
        print("Grade:", grade)
        print("Status:", status)

def topper():
    if students:
        name = max(students, key=lambda x: sum(students[x]))
        print("Topper:", name)
        print("Marks:", sum(students[name]))
    else:
        print("No students available.")


while True:
    print("\n--- Student Grade Management ---")
    print("1. Add Student")
    print("2. Display Results")
    print("3. Find Topper")
    print("4. Exit")

    choice = int(input("Enter choice: "))

    if choice == 1:
        add_student()
    elif choice == 2:
        calculate_result()
    elif choice == 3:
        topper()
    elif choice == 4:
        break
    else:
        print("Invalid choice")