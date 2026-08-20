class Book:
    def __init__(self, title, author, price, pages):
        self.title = title
        self.author = author
        self.price = price
        self.pages = pages

book1 = Book("Python Basics", "John", 500, 250)
book2 = Book("Java Programming", "James", 600, 350)
book3 = Book("Web Development", "David", 450, 300)

print(book1.title, book1.author, book1.price, book1.pages)
print(book2.title, book2.author, book2.price, book2.pages)
print(book3.title, book3.author, book3.price, book3.pages)