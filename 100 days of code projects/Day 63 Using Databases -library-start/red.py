from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///books-project.db"
db.init_app(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String, unique=True, nullable=False)
    author = db.Column(db.String, unique=False, nullable=False)
    rating = db.Column(db.Float, unique=False, nullable=False)
    description = db.Column(db.String)

# create the database tables
# with app.app_context():
#     db.create_all()

# read all results
with app.app_context():
    result = db.session.execute(db.select(User).order_by(User.title))
    all_books = result.scalars()

    print(all_books)
