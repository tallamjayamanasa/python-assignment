class Book:
    def __init__(self, name):
        self.name = name

    def show_book(self):
        print("Book:", self.name)


class SearchService:
    def search(self, book_name):
        print("Searching for:", book_name)


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

    def search_book(self, search_service, book_name):
        search_service.search(book_name)


library = Library()
search = SearchService()

library.show_books()
library.search_book(search, "Python")