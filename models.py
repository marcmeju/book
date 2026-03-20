from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()

def init_app(app):
    db.app = app
    db.init_app(app)

class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    author = db.Column(db.String(100), nullable=False)
    isbn = db.Column(db.String(20), unique=True, nullable=False)
    price = db.Column(db.Float, nullable=False)
    image_url = db.Column(db.String(255), nullable=True)

    def __repr__(self):
        return f"<Book {self.title} by {self.author}>"
    
    def serialize(self):
        return {
            'id': self.id,
            'title': self.title,
            'author': self.author,
            'isbn': self.isbn,
            'price': self.price,
            'image_url': self.image_url
        }