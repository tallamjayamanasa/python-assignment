class Employee:
    def __init__(self,salary): self.salary=salary
    def __gt__(self,other): return self.salary>other.salary
print("Employee 1 has higher salary:", Employee(50000)>Employee(45000))
