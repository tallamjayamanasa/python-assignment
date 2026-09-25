class SearchService:
    def search(self, query):
        print(f"Searching library catalog for: {query}")
        return ["Book 1", "Book 2"]


class Library:
    def __init__(self):
        self.search_service = SearchService()

    def find_books(self, query):
        return self.search_service.search(query)


def run_demo():
    library = Library()
    print("Library -> SearchService example")
    books = library.find_books("python")
    print(f"Search results: {books}")
    print()
