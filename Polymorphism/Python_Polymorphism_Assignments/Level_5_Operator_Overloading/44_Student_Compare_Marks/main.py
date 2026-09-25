class Student:
    def __init__(self,marks): self.marks=marks
    def __gt__(self,other): return self.marks>other.marks
print("Student 1 has higher marks:", Student(85)>Student(75))
