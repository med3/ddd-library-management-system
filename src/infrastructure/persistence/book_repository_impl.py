from src.domain.repositories.book_repository import BookRepository
from src.domain.models.book import Book

# Assuming using SQLAlchemy as ORM
from sqlalchemy.orm import Session

class BookRepositorySQLAlchemy(BookRepository):
    def __init__(self, session: Session):
        self.session = session

    def find_by_id(self, book_id):
        return self.session.query(Book).filter(Book.id == book_id).first()

    def save(self, book):
        self.session.add(book)
        self.session.commit()
