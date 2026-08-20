books = {}

def add_book():
    book_id = input("Enter book ID: ")
    title = input("Enter book title: ")

    books[book_id] = {
        "title": title,
        "issued": False
    }

    print("Book added.")

def search_book():
    book_id = input("Enter book ID: ")

    if book_id in books:
        print("Title:", books[book_id]["title"])
        print("Issued:", books[book_id]["issued"])
    else:
        print("Book not found.")

def issue_book():
    book_id = input("Enter book ID: ")

    if book_id in books:
        if not books[book_id]["issued"]:
            books[book_id]["issued"] = True
            print("Book issued.")
        else:
            print("Book is already issued.")
    else:
        print("Book not found.")

def return_book():
    book_id = input("Enter book ID: ")

    if book_id in books:
        books[book_id]["issued"] = False
        print("Book returned.")
    else:
        print("Book not found.")

def display_available_books():
    print("\n--- Available Books ---")

    for book_id, data in books.items():
        if not data["issued"]:
            print(book_id, "-", data["title"])


while True:
    print("\n--- Library Management ---")
    print("1. Add Book")
    print("2. Search Book")
    print("3. Issue Book")
    print("4. Return Book")
    print("5. Display Available Books")
    print("6. Exit")

    choice = int(input("Enter choice: "))

    if choice == 1:
        add_book()
    elif choice == 2:
        search_book()
    elif choice == 3:
        issue_book()
    elif choice == 4:
        return_book()
    elif choice == 5:
        display_available_books()
    elif choice == 6:
        break
    else:
        print("Invalid choice")