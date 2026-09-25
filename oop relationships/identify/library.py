class Book:
    def __init__(self, name):
        self.name = name

    def show_book(self):
        print("Book:", self.name)


class Library:
    def __init__(self):
        self.books = [
            Book("Python"),
            Book("Java"),
            Book("SQL")
        ]

    def show_books(self):
        for book in self.books:
            book.show_book()


library = Library()
library.show_books()