from abc import ABC, abstractmethod


class LibraryItem(ABC):

    def __init__(self, title):
        self.title = title

    @abstractmethod
    def display_type(self):
        pass

    def display_title(self):
        print("Title:", self.title)


class Book(LibraryItem):

    def display_type(self):
        print("Type: Book")


class Magazine(LibraryItem):

    def display_type(self):
        print("Type: Magazine")


class Newspaper(LibraryItem):

    def display_type(self):
        print("Type: Newspaper")


items = [
    Book("Python Programming"),
    Magazine("Technology Today"),
    Newspaper("Daily News")
]

for item in items:
    item.display_title()
    item.display_type()
    print()