from flask import Flask

app = Flask(__name__)

def make_bold(function):
    def wrapper():
        return f"<b>{function()}<b>"
    return wrapper

def make_emphasis(function):
    def wrapper():
        return f"<em>{function()}<em>"
    return wrapper

def make_underline(function):
    def wrapper():
        return f"<u>{function()}<u>"
    return wrapper

@app.route("/")
def hello_world():
    return "<p style='color: blue;'>Hello, World!</p>"


@app.route("/bye")
@make_bold
@make_emphasis
@make_underline
def say_bye():
    return "Bye"

@app.route("/username/<name>/<int:age>")
def greet(name, age):
    return f"Hello {name}, you're {age} years!"


if __name__ == "__main__":
    app.run(debug=True)
