from datetime import datetime, timedelta

class Loan:
    def __init__(self, book, member):
        self.book = book
        self.member = member
        self.start_date = datetime.now()
        self.end_date = self.start_date + timedelta(days=14)  # Assuming 2 weeks loan period
