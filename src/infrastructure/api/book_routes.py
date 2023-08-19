from flask import Flask, jsonify
from src.application.services.borrowing_service import BorrowingService

app = Flask(__name__)
borrowing_service = BorrowingService()  # Simplified initialization for brevity

@app.route('/books/<int:book_id>', methods=['GET'])
def get_book(book_id):
    book_dto = borrowing_service.get_book_details(book_id)
    return jsonify(book_dto.__dict__)
