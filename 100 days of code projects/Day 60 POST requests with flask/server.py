from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route("/")
@app.route("/home")
def home():
    return render_template("index.html")

@app.route("/login", methods=["POST"])
def login():
    error = None
    if request.method == 'POST':
        user = request.form['username']
        password = request.form['password']

    else:
        error = 'Invalid username/password'
    return render_template('login.html', error=error, username=user, password=password)

if __name__ == "__main__":
    app.run(debug=True)
