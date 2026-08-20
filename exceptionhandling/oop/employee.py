class InvalidSalaryError(Exception):
    pass


class Employee:
    def __init__(self, name):
        self.name = name
        self.salary = 0

    def set_salary(self, salary):
        try:
            if salary < 0:
                raise InvalidSalaryError(
                    "Salary cannot be negative."
                )

            self.salary = salary
            print("Employee:", self.name)
            print("Salary:", self.salary)

        except InvalidSalaryError as e:
            print("Error:", e)


employee = Employee("Rahul")

try:
    salary = float(input("Enter salary: "))
    employee.set_salary(salary)

except ValueError:
    print("Error: Enter a valid salary.")