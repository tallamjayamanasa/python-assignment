employees = [
    ("Jaya", "Developer", 40000),
    ("Ravi", "Manager", 60000),
    ("Sita", "Tester", 35000),
    ("Kiran", "Designer", 45000)
]

highest = employees[0]

for employee in employees:
    if employee[2] > highest[2]:
        highest = employee

print("Highest Salary Employee:")
print("Name:", highest[0])
print("Designation:", highest[1])
print("Salary:", highest[2])