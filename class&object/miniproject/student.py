class Student:
    def __init__(self, roll_no, name, marks):
        self.roll_no = roll_no
        self.name = name
        self.marks = marks

    def display(self):
        print("Roll No:", self.roll_no)
        print("Name:", self.name)
        print("Marks:", self.marks)


students = []

while True:
    print("\n--- Student Management System ---")
    print("1. Add Student")
    print("2. Search Student")
    print("3. Update Student")
    print("4. Delete Student")
    print("5. Display Students")
    print("6. Exit")

    choice = int(input("Enter choice: "))

    if choice == 1:
        roll = int(input("Enter roll number: "))
        name = input("Enter name: ")
        marks = float(input("Enter marks: "))

        students.append(Student(roll, name, marks))
        print("Student added successfully.")

    elif choice == 2:
        roll = int(input("Enter roll number: "))
        found = False

        for s in students:
            if s.roll_no == roll:
                s.display()
                found = True
                break

        if not found:
            print("Student not found.")

    elif choice == 3:
        roll = int(input("Enter roll number: "))

        for s in students:
            if s.roll_no == roll:
                s.name = input("Enter new name: ")
                s.marks = float(input("Enter new marks: "))
                print("Student updated.")
                break
        else:
            print("Student not found.")

    elif choice == 4:
        roll = int(input("Enter roll number: "))

        for s in students:
            if s.roll_no == roll:
                students.remove(s)
                print("Student deleted.")
                break
        else:
            print("Student not found.")

    elif choice == 5:
        if len(students) == 0:
            print("No students available.")
        else:
            for s in students:
                s.display()
                print("----------------")

    elif choice == 6:
        print("Program ended.")
        break

    else:
        print("Invalid choice.")