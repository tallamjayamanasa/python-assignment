class InvalidEmployeeIDError(Exception):
    pass


class InvalidSalaryError(Exception):
    pass


class InvalidDepartmentError(Exception):
    pass


class EmployeeManagement:
    def __init__(self):
        self.employees = {}

    def add_employee(self, emp_id, name, salary, department):
        if not emp_id.isdigit():
            raise InvalidEmployeeIDError(
                "Employee ID must contain numbers only."
            )

        if salary < 0:
            raise InvalidSalaryError(
                "Salary cannot be negative."
            )

        departments = ["HR", "IT", "SALES"]

        if department.upper() not in departments:
            raise InvalidDepartmentError(
                "Invalid department."
            )

        self.employees[emp_id] = {
            "name": name,
            "salary": salary,
            "department": department.upper()
        }

        print("Employee added successfully.")


system = EmployeeManagement()

try:
    emp_id = input("Enter employee ID: ")
    name = input("Enter employee name: ")
    salary = float(input("Enter salary: "))
    department = input("Enter department (HR/IT/SALES): ")

    system.add_employee(emp_id, name, salary, department)

except (InvalidEmployeeIDError, InvalidSalaryError,
        InvalidDepartmentError) as e:
    print("Error:", e)

except ValueError:
    print("Error: Enter a valid salary.")