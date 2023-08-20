from src.domain.models.loan.loan import Loan
from src.domain.services.late_fee_calculator import LateFeeCalculator


# class BorrowingService:
#     def __init__(self, book_repository, member_repository):
#         self.book_repository = book_repository
#         self.member_repository = member_repository

#     def borrow_book(self, book_id, member_id):
#         book = self.book_repository.find_by_id(book_id)
#         member = self.member_repository.find_by_id(member_id)

#         if book and member and not book.on_loan:
#             member.borrow(book)
#             book.mark_as_on_loan()



class BorrowingService:
    def __init__(self, book_repo, member_repo):
        self.book_repo = book_repo
        self.member_repo = member_repo

    def borrow_book(self, book_id, member_id):
        book = self.book_repo.find_by_id(book_id)
        member = self.member_repo.find_by_id(member_id)

        if not book.on_loan:
            loan = Loan(book, member)
            member.current_loans.append(loan)
            book.on_loan = True

    def return_book(self, book_id, user_id):
        book = self.book_repo.find_by_id(book_id)
        user = self.member_repo.find_by_id(user_id)

        if not book.is_borrowed_by(user):
            raise ValueError("The book is not borrowed by this user.")

        days_late = book.days_since_due_date()
        late_fee = LateFeeCalculator.calculate_fee(days_late)

        user.apply_fee(late_fee)
        book.mark_as_returned()
        
        # Ideally, persist these changes to a datastore
        self.book_repo.add_book(book)
        self.member_repo.add_member(user)

        return late_fee