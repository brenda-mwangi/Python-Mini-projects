from flask import Flask, render_template, request, url_for, redirect, flash, send_from_directory
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin, login_user, LoginManager, login_required, current_user, logout_user
from datetime import datetime
from sqlalchemy.exc import IntegrityError

app = Flask(__name__)

app.config['SECRET_KEY'] = 'any-secret-key-you-choose'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

##CREATE TABLE IN DB
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(200))
    date = db.Column(db.String(20), default=lambda: datetime.now().strftime('%d-%m-%Y'))
#Line below only required once, when creating DB.
# with app.app_context():
#     db.create_all()


@app.route('/')
def home():
    return render_template("index.html"), 200


@app.route('/register', methods=["GET","POST"])
def register():
    if request.method == "POST":
        user_name = request.form["name"]
        user_email = request.form["email"]
        user_password = request.form["password"]

        new_user = User(name=user_name,email=user_email,password=user_password)
        if new_user is not None:
            try:
                db.session.add(new_user)
                db.session.commit()
                return redirect(url_for('secrets', user=user_name )), 200
            except IntegrityError as e:
                db.session.rollback()
                return f"<h3>A user with that email already exists. Please try again.</h3>", 400

        else:
            return render_template("register.html")

    else:
        return render_template("register.html")


@app.route('/login')
def login():
    return render_template("login.html")


@app.route('/secrets/<name>')
def secrets(name):
    return render_template("secrets.html", name=name)


@app.route('/logout')
def logout():
    pass


@app.route('/download')
def download():
    pass


if __name__ == "__main__":
    app.run(debug=True)
