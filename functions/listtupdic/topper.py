def find_topper(marks):
    return max(marks, key=marks.get)

students = {
    "Ravi": 85,
    "Anu": 92,
    "Sita": 88
}

print(find_topper(students))