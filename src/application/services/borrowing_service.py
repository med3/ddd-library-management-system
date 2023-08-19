from src.domain.repositories.book_repository import BookRepository
from src.domain.repositories.member_repository import MemberRepository

class BorrowingService:
    def __init__(self, book_repository, member_repository):
        self.book_repository = book_repository
        self.member_repository = member_repository

    def borrow_book(self, book_id, member_id):
        book = self.book_repository.find_by_id(book_id)
        member = self.member_repository.find_by_id(member_id)

        if book and member and not book.on_loan:
            member.borrow(book)
            book.mark_as_on_loan()

