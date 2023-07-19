from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, Length
import email_validator
from flask_wtf.csrf import CSRFProtect
from flask_bootstrap import Bootstrap5

app = Flask(__name__)
bootstrap = Bootstrap5(app)

app.config['SECRET_KEY'] = 'Tcv36vd78bci3'
csrf = CSRFProtect(app)

class MyForm(FlaskForm):
    email = StringField(label='Email', validators=[DataRequired(), Email(granular_message=True)])
    password= PasswordField(label='Password', validators=[Length(min=8, message='Password must be at least 8 characters long'), DataRequired(message='Password is required')])
    submit = SubmitField(label="Log In")

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/login",methods=['GET', 'POST'])
def login():
    loginForm = MyForm()

    if loginForm.validate_on_submit():
        if (loginForm.email.data == "admin@email.com") and (loginForm.password.data == "12345678"):
            return render_template("success.html")
        else:
            return render_template("denied.html")

    return render_template("login.html", form=loginForm)

if __name__ == '__main__':
    app.run(debug=True)
