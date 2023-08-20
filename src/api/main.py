from src.domain.repositories.book_repository import BookRepository
from src.domain.repositories.member_repository import MemberRepository
from src.domain.models.book.book import Book
from src.domain.models.member.member import Member
from src.application.services.borrowing_service import BorrowingService

book_repo = BookRepository()
member_repo = MemberRepository()
borrowing_service = BorrowingService(book_repo, member_repo)

# Sample Interaction
book = Book(id=1, title="Domain-Driven Design", author="Eric Evans")
member = Member(id=1, name="Alice")
book_repo.add_book(book)
member_repo.add_member(member)

borrowing_service.borrow_book(1, 1)

for l in member.current_loans:
    print(l.__dict__)  # It should show the loan details for student member Alice
