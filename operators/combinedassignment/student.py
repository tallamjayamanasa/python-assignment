maths = int(input("Enter Maths marks: "))
python = int(input("Enter Python marks: "))
sql = int(input("Enter SQL marks: "))

if maths >= 35 and python >= 35 and sql >= 35:
    print("Student passed all subjects")
else:
    print("Student failed")