class College:
    def __init__(self, name, location, course):
        self.name = name
        self.location = location
        self.course = course

college1 = College("Aditya College", "Surampalem", "CSE")
college2 = College("ABC College", "Vijayawada", "ECE")
college3 = College("XYZ College", "Hyderabad", "IT")

print(college1.name, college1.location, college1.course)
print(college2.name, college2.location, college2.course)
print(college3.name, college3.location, college3.course)