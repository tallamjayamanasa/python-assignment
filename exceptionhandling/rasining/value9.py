try:
    attendance = float(input("Enter attendance percentage: "))

    if attendance < 75:
        raise ValueError("Attendance must be at least 75%.")

    print("Attendance:", attendance)
    print("Student is eligible.")

except ValueError as e:
    print("Error:", e)