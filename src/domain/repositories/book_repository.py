class BookRepository:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def find_by_id(self, id):
        return next((book for book in self.books if book.id == id), None)