from flask import Flask
import os
from dotenv import load_dotenv
from routes import book_blueprint
from models import db, Book, init_app
from flask_migrate import Migrate


# Load environment variables from .env file
load_dotenv()

app = Flask(__name__, instance_relative_config=True)
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY_FROM_ENV')

# Ensure instance folder exists
try:
    os.makedirs(app.instance_path, exist_ok=True)
except OSError:
    pass

app.config['SQLALCHEMY_DATABASE_URI'] = f"sqlite:///{os.path.join(app.instance_path, 'book.db')}"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

#import routes
app.register_blueprint(book_blueprint)

# Initialize the database and migration
init_app(app)
migrate = Migrate(app, db)

if __name__ == '__main__':
    app.run(debug=True, port=5002)
