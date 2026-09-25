class Person:
    def show_person(self):
        print("This is a person")


class Librarian(Person):
    def manage_library(self):
        print("Librarian manages the library")


class Book:
    def __init__(self, title):
        self.title = title

    def show_book(self):
        print("Book:", self.title)


class SearchService:
    def search(self, title):
        print("Searching for:", title)


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

    def search_book(self, service, title):
        service.search(title)


librarian = Librarian()
library = Library()
search = SearchService()

librarian.show_person()
librarian.manage_library()

library.show_books()
library.search_book(search, "Python")