from flask import Blueprint, jsonify, request
from models import Book, db

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
    try:
        book = Book()
        book.title = request.form['title']
        book.author = request.form['author']
        book.isbn = request.form['isbn']
        book.price = request.form['price']
        book.image_url = request.form['image_url']

        # create a new Book instance and save it to the database
        db.session.add(book)
        db.session.commit()

        response = {"Message": "Book created successfully", "Book": book.serialize()}
    except Exception as e:
        print(str(e))
        response = {"Message": "Failed to create book"}
    return jsonify(response)

@book_blueprint.route('/<int:book_isbn>', methods=['GET'])
def get_book(book_isbn):
    # book = Book.query.get_or_404(book_id)
    # return jsonify(book.to_dict()), 200
    return f"Found - Book with ISBN {book_isbn}"