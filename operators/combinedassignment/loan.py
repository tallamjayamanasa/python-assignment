salary = float(input("Enter monthly salary: "))
age = int(input("Enter age: "))

if salary >= 25000 and age >= 21:
    print("Person is eligible for the loan")
else:
    print("Person is not eligible for the loan")