from flask import Flask, render_template, request, url_for, redirect, flash, send_from_directory, jsonify
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

login_manager = LoginManager(app)
login_manager.login_view = "login"

##CREATE TABLE IN DB
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(200))
    date = db.Column(db.String(20), default=lambda: datetime.now().strftime('%d-%m-%Y'))

    @staticmethod
    def get(user_id):
        return User.query.filter_by(id=user_id).first()

    @staticmethod
    def hash_password(password):
        return generate_password_hash(password, method='pbkdf2:sha256', salt_length=16)

    @staticmethod
    def check_password(passhash, password):
        return check_password_hash(passhash, password)

@login_manager.user_loader
def load_user(user_id):
    return User.get(user_id)

@app.route('/')
def home():
    if current_user.is_authenticated:
        return render_template("index.html", logged_in=True), 200
    else:
        return render_template("index.html", logged_in=False), 200


@app.route('/register', methods=["GET","POST"])
def register():
    if request.method == "POST":
        user_name = request.form["name"]
        user_email = request.form["email"]
        user_password = request.form["password"]

        new_user = User(
            name=user_name,
            email=user_email,
            password=User.hash_password(user_password)
            )
        if new_user is not None:
            try:
                db.session.add(new_user)
                db.session.commit()

                new_user2 =  User.query.filter_by(email=user_email).first()
                login_user(new_user2)
                return redirect(url_for('secrets')), 200

            except IntegrityError as e:
                db.session.rollback()
                return f"<h3>A user with that email already exists. Please try again.</h3>", 400

        else:
            return render_template("register.html")

    else:
        return render_template("register.html")

@app.route('/login', methods=["GET","POST"])
def login():
    if request.method == "POST":
        login_email = request.form["email"]
        login_password = request.form["password"]

        user = User.query.filter_by(email=login_email).first()
        if user and User.check_password(user.password, login_password):
            login_user(user)
            return redirect(url_for('secrets')), 200
        else:
            return jsonify(error={"PasswordError":"The password you entered is not correct."})

        # else:
        #     return jsonify(error={"EmailError":"Email you entered is not correct."})

    else:
        return render_template("login.html"), 200


@app.route('/secrets')
@login_required
def secrets():
    name = current_user.name
    return render_template("secrets.html", name=name), 200


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))

@app.route('/download')
@login_required
def download():
    pass

if __name__ == "__main__":
    app.run(debug=True)
