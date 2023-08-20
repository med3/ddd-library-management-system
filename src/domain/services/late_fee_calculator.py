# domain/services/late_fee_calculator.py

class LateFeeCalculator:
    @staticmethod
    def calculate_fee(days_late: int) -> float:
        """Calculate late fee based on the number of days a book is late."""

        if days_late <= 0:
            return 0.0
        elif days_late <= 7:
            return days_late * 0.5  # 50 cents per day for the first week
        else:
            return 7 * 0.5 + (days_late - 7) * 1  # 1 dollar per day after the first week
