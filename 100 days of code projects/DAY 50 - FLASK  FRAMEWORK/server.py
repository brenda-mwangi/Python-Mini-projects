from flask import Flask
import random
app = Flask(__name__)

class Generate:
    def __init__(self):
        pass
@app.route("/")
def hello():
    return "<h1>Guess a number between 0 and 9</h1>"\
    "<img src='https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif'>"

@app.route("/<int:guess>")


if __name__ == "__main__":
    app.run(debug=True)
