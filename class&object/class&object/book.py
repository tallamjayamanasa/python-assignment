class Book:
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price

book1 = Book("Python Basics", "John", 500)
book2 = Book("Java Programming", "James", 600)

print("Book 1")
print("Title:", book1.title)
print("Author:", book1.author)
print("Price:", book1.price)

print("\nBook 2")
print("Title:", book2.title)
print("Author:", book2.author)
print("Price:", book2.price)