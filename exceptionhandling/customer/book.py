class BookNotAvailableError(Exception):
    pass


try:
    books = {
        "python": True,
        "java": False,
        "c": True
    }

    book = input("Enter book name: ").lower()

    if book not in books:
        raise BookNotAvailableError("Book does not exist in the library.")

    if not books[book]:
        raise BookNotAvailableError("Book is currently not available.")

    print("Book is available.")

except BookNotAvailableError as e:
    print("Error:", e)