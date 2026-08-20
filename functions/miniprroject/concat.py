contacts = {}

def add_contact():
    name = input("Enter name: ")
    phone = input("Enter phone number: ")

    contacts[name] = phone
    print("Contact added.")

def search_contact():
    name = input("Enter name: ")

    if name in contacts:
        print("Phone:", contacts[name])
    else:
        print("Contact not found.")

def update_contact():
    name = input("Enter name: ")

    if name in contacts:
        contacts[name] = input("Enter new phone number: ")
        print("Contact updated.")
    else:
        print("Contact not found.")

def delete_contact():
    name = input("Enter name: ")

    if name in contacts:
        del contacts[name]
        print("Contact deleted.")
    else:
        print("Contact not found.")

def display_contacts():
    for name, phone in contacts.items():
        print("Name:", name, "| Phone:", phone)


while True:
    print("\n--- Contact Management ---")
    print("1. Add")
    print("2. Search")
    print("3. Update")
    print("4. Delete")
    print("5. Display")
    print("6. Exit")

    choice = int(input("Enter choice: "))

    if choice == 1:
        add_contact()
    elif choice == 2:
        search_contact()
    elif choice == 3:
        update_contact()
    elif choice == 4:
        delete_contact()
    elif choice == 5:
        display_contacts()
    elif choice == 6:
        break
    else:
        print("Invalid choice")