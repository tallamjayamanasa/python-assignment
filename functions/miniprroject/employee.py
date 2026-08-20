employees = {}

def add_employee():
    emp_id = input("Enter employee ID: ")
    name = input("Enter employee name: ")
    salary = float(input("Enter salary: "))

    employees[emp_id] = {
        "name": name,
        "salary": salary
    }

    print("Employee added successfully.")

def search_employee():
    emp_id = input("Enter employee ID: ")

    if emp_id in employees:
        print("Name:", employees[emp_id]["name"])
        print("Salary:", employees[emp_id]["salary"])
    else:
        print("Employee not found.")

def update_employee():
    emp_id = input("Enter employee ID: ")

    if emp_id in employees:
        employees[emp_id]["name"] = input("Enter new name: ")
        employees[emp_id]["salary"] = float(input("Enter new salary: "))
        print("Employee updated.")
    else:
        print("Employee not found.")

def delete_employee():
    emp_id = input("Enter employee ID: ")

    if emp_id in employees:
        del employees[emp_id]
        print("Employee deleted.")
    else:
        print("Employee not found.")

def display_employees():
    for emp_id, data in employees.items():
        print("\nID:", emp_id)
        print("Name:", data["name"])
        print("Salary:", data["salary"])


while True:
    print("\n--- Employee Management ---")
    print("1. Add")
    print("2. Search")
    print("3. Update")
    print("4. Delete")
    print("5. Display")
    print("6. Exit")

    choice = int(input("Enter choice: "))

    if choice == 1:
        add_employee()
    elif choice == 2:
        search_employee()
    elif choice == 3:
        update_employee()
    elif choice == 4:
        delete_employee()
    elif choice == 5:
        display_employees()
    elif choice == 6:
        break
    else:
        print("Invalid choice")