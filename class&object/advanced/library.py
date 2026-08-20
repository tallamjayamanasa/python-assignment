class LibraryBook:
    def __init__(self, title):
        self.title = title
        self.issued = False

    def issue_book(self):
        if self.issued:
            print("Book is already issued")
        else:
            self.issued = True
            print("Book issued successfully")

    def return_book(self):
        if self.issued:
            self.issued = False
            print("Book returned successfully")
        else:
            print("Book was not issued")

    def display(self):
        print("Book:", self.title)

        if self.issued:
            print("Status: Issued")
        else:
            print("Status: Available")


book = LibraryBook("Python Programming")

book.display()

book.issue_book()
book.display()

book.return_book()
book.display()