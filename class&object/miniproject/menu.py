class Student:
    # Class variable
    school = "ABC School"
    count = 0

    # Constructor
    def __init__(self, roll_no, name, marks):
        # Instance variables
        self.roll_no = roll_no
        self.name = name
        self.marks = marks

        Student.count += 1

    # Instance method
    def display(self):
        print("Roll No:", self.roll_no)
        print("Name:", self.name)
        print("Marks:", self.marks)
        print("School:", Student.school)

    # Instance method
    def result(self):
        if self.marks >= 40:
            print("Result: Pass")
        else:
            print("Result: Fail")


students = []

while True:
    print("\n--- OOP Application ---")
    print("1. Create Student")
    print("2. Display Students")
    print("3. Display Student Count")
    print("4. Display School Name")
    print("5. Check Result")
    print("6. Exit")

    choice = int(input("Enter choice: "))

    if choice == 1:
        roll = int(input("Enter roll number: "))
        name = input("Enter name: ")
        marks = float(input("Enter marks: "))

        student = Student(roll, name, marks)
        students.append(student)

        print("Student object created.")

    elif choice == 2:
        if len(students) == 0:
            print("No students available.")
        else:
            for student in students:
                student.display()
                print("----------------")

    elif choice == 3:
        print("Total Student Objects:", Student.count)

    elif choice == 4:
        print("School Name:", Student.school)

    elif choice == 5:
        roll = int(input("Enter roll number: "))

        for student in students:
            if student.roll_no == roll:
                student.result()
                break
        else:
            print("Student not found.")

    elif choice == 6:
        print("Program ended.")
        break

    else:
        print("Invalid choice.")