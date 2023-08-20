# tests/test_services.py

from src.domain.services.late_fee_calculator import LateFeeCalculator
from src.application.services.borrowing_service import BorrowingService

# Mocking some dependencies for the sake of simplicity
class MockBook:
    def __init__(self, days_since_due_date):
        self._days_since_due_date = days_since_due_date

    def days_since_due_date(self):
        return self._days_since_due_date

    def is_borrowed_by(self, user):
        return True  # Always true for this simple mock

    def mark_as_returned(self):
        pass

class MockUser:
    def apply_fee(self, fee):
        self.fee = fee

class MockBookRepository:
    def __init__(self):
        self.books = []

    def find_by_id(self, book_id):
        return MockBook(10)

    def add_book(self, book):
        self.books.append(book)

class MockMemberRepository:
    def __init__(self):
        self.members = []

    def find_by_id(self, book_id):
        return MockUser()

    def add_member(self, member):
        self.members.append(member)

def test_late_fee_calculator():
    assert LateFeeCalculator.calculate_fee(-5) == 0.0
    assert LateFeeCalculator.calculate_fee(0) == 0.0
    assert LateFeeCalculator.calculate_fee(3) == 1.5
    assert LateFeeCalculator.calculate_fee(7) == 3.5
    assert LateFeeCalculator.calculate_fee(10) == 6.5

def test_return_book():
    # book_repository = {"find_by_id": lambda x: MockBook(10)}
    # user_repository = {"find_by_id": lambda x: MockUser()}
    book_repository = MockBookRepository()
    user_repository = MockMemberRepository()
    service = BorrowingService(book_repository, user_repository)
    
    fee = service.return_book("some_book_id", "some_user_id")
    assert fee == 6.5
