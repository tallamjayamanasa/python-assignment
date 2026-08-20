class BookNotAvailableError(Exception):
    pass


class Library:
    def __init__(self):
        self.books = {
            "python": True,
            "java": False,
            "c": True
        }

    def issue_book(self, book):
        try:
            if book not in self.books:
                raise BookNotAvailableError(
                    "Book does not exist in the library."
                )

            if not self.books[book]:
                raise BookNotAvailableError(
                    "Book is currently unavailable."
                )

            self.books[book] = False
            print("Book issued successfully.")

        except BookNotAvailableError as e:
            print("Error:", e)


library = Library()

book = input("Enter book name: ").lower()

library.issue_book(book)