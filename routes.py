from flask import Blueprint, jsonify, request

book_blueprint = Blueprint('book_api_routes', __name__, url_prefix='/api/book')


@book_blueprint.route('/', methods=['GET'])
def get_books():
    return "Welcome to the Book API!"

@book_blueprint.route('/all', methods=['GET'])
def get_all_books():
#    books = Book.query.all()
#    return jsonify([book.to_dict() for book in books]), 200
    return "All books"

@book_blueprint.route('/create', methods=['POST'])
def create_book():
    return "New book created"

@book_blueprint.route('/<int:book_isbn>', methods=['GET'])
def get_book(book_isbn):
    # book = Book.query.get_or_404(book_id)
    # return jsonify(book.to_dict()), 200
    return f"Found - Book with ISBN {book_isbn}"