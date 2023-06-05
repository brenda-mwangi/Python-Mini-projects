from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p style='color: blue;'>Hello, World!</p>"

@app.route("/bye")
def say_bye():
    return "bye"

@app.route("/username/<name>/<int:number>")
def greet(name, number):
    return f"Hello {name}, you're {number} years!"


if __name__ == "__main__":
    app.run(debug=True)
