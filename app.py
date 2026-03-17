from flask import Flask
import os
from dotenv import load_dotenv
from routes import book_blueprint


# Load environment variables from .env file
load_dotenv()

app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY_FROM_ENV')
app. config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///./dtabase/book.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

#import routes
app.register_blueprint(book_blueprint)

if __name__ == '__main__':
    app.run(debug=True, port=5002)
