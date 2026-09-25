salary = float(input("Enter salary: "))
increment = float(input("Enter increment percentage: "))

increase = salary * increment / 100
new_salary = salary + increase

print("Salary after increment:", new_salary)