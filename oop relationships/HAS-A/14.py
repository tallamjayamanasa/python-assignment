class Book:
    def __init__(self, title):
        self.title = title

    def show_book(self):
        print("Book:", self.title)

class Library:
    def __init__(self):
        self.books = [
            Book("Python"),
            Book("Java"),
            Book("Database")
        ]

    def show_books(self):
        for book in self.books:
            book.show_book()

library = Library()
library.show_books()