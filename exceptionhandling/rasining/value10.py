try:
    salary = float(input("Enter employee salary: "))

    if salary < 0:
        raise ValueError("Salary cannot be negative.")

    print("Employee salary:", salary)

except ValueError as e:
    print("Error:", e)