class BookNotAvailableError(Exception):
    pass


class InvalidBookIDError(Exception):
    pass


class DuplicateBookError(Exception):
    pass


class Library:
    def __init__(self):
        self.books = {}

    def add_book(self, book_id, title):
        if not book_id:
            raise InvalidBookIDError("Book ID cannot be empty.")

        if book_id in self.books:
            raise DuplicateBookError("Book already exists.")

        self.books[book_id] = title
        print("Book added successfully.")

    def issue_book(self, book_id):
        if book_id not in self.books:
            raise BookNotAvailableError("Book is not available.")

        print("Book issued:", self.books[book_id])


library = Library()

try:
    book_id = input("Enter book ID: ")
    title = input("Enter book title: ")

    library.add_book(book_id, title)

    issue_id = input("Enter book ID to issue: ")
    library.issue_book(issue_id)

except (InvalidBookIDError, DuplicateBookError,
        BookNotAvailableError) as e:
    print("Error:", e)