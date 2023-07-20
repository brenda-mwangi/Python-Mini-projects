from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///books.db"
db.init_app(app)

class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String, unique=True, nullable=False)
    author = db.Column(db.String, unique=False, nullable=False)
    rating = db.Column(db.Float, unique=False, nullable=False)
    description = db.Column(db.String)

# create the database tables
# with app.app_context():
#     db.create_all()

# read all results


@app.route('/', methods=['GET', 'POST'])
def home():
    return render_template("index.html", books=db.session.execute(db.select(Book)).scalars())

@app.route("/add", methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        book_name = request.form['book_name']
        book_author = request.form['book_author']
        book_rating = request.form['rating']

        with app.app_context():
            new_book = Book(title=book_name, author=book_author, rating=book_rating)
            db.session.add(new_book)
            db.session.commit()
        return redirect(url_for('home'))

    return render_template("add.html")

@app.route("/edit/<int:book_id>", methods=['GET', 'POST'])
def edit_rating(book_id):

    if request.method == 'POST':
        new_rate = request.form['new_rate']

        with app.app_context():
            book_to_update = db.session.execute(db.select(Book).where(Book.id == book_id)).scalar()
            book_to_update.rating = new_rate
            db.session.commit()
        return redirect(url_for('home'))

    return render_template("edit.html", book=db.session.execute(db.select(Book).where(Book.id == book_id)).scalar())


@app.route("/delete", methods=['GET', 'POST'])
def delete():
    book_id = request.args.get("book_id")
    with app.app_context():
        book_to_delete = db.session.execute(db.select(Book).where(Book.id == book_id)).scalar()
        db.session.delete(book_to_delete)
        db.session.commit()
    return redirect(url_for('home'))

if __name__ == "__main__":
    app.run(debug=True)

