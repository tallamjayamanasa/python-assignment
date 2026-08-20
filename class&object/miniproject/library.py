class Book:
    def __init__(self, book_id, title, author):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.issued = False

    def display(self):
        print("Book ID:", self.book_id)
        print("Title:", self.title)
        print("Author:", self.author)
        print("Status:", "Issued" if self.issued else "Available")


books = []

while True:
    print("\n--- Library Management System ---")
    print("1. Add Book")
    print("2. Search Book")
    print("3. Issue Book")
    print("4. Return Book")
    print("5. Display Books")
    print("6. Exit")

    choice = int(input("Enter choice: "))

    if choice == 1:
        book_id = int(input("Enter book ID: "))
        title = input("Enter book title: ")
        author = input("Enter author: ")

        books.append(Book(book_id, title, author))
        print("Book added.")

    elif choice == 2:
        book_id = int(input("Enter book ID: "))

        for book in books:
            if book.book_id == book_id:
                book.display()
                break
        else:
            print("Book not found.")

    elif choice == 3:
        book_id = int(input("Enter book ID: "))

        for book in books:
            if book.book_id == book_id:
                if not book.issued:
                    book.issued = True
                    print("Book issued.")
                else:
                    print("Book is already issued.")
                break
        else:
            print("Book not found.")

    elif choice == 4:
        book_id = int(input("Enter book ID: "))

        for book in books:
            if book.book_id == book_id:
                book.issued = False
                print("Book returned.")
                break
        else:
            print("Book not found.")

    elif choice == 5:
        for book in books:
            book.display()
            print("----------------")

    elif choice == 6:
        break

    else:
        print("Invalid choice.")