maths = int(input("Enter Mathematics marks: "))
science = int(input("Enter Science marks: "))

if maths >= 35 or science >= 35:
    print("Student passed at least one subject")
else:
    print("Student failed both subjects")