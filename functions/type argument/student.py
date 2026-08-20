def student_details(*marks, **details):
    print("Student Details:")
    for key, value in details.items():
        print(key, ":", value)

    print("Marks:", marks)

student_details(
    85, 90, 78, 88,
    name="Jaya",
    age=18,
    course="CCN"
)