from src.application.dto.book_dto import BookDTO

class BookMapper:
    @staticmethod
    def to_dto(book):
        return BookDTO(id=book.id, title=book.title, author=book.author, on_loan=book.on_loan)
