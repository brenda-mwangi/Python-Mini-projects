from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route("/")
@app.route("/home")
def home():
    url = 'https://api.npoint.io/4152611fd8cc3f8b70c5'
    response= requests.get(url).json()[1:]
    return render_template("index.html", blogs= response)

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/<string:title>/<int:num>")
def single_post(num,title):
    url = 'https://api.npoint.io/4152611fd8cc3f8b70c5'
    response= requests.get(url).json()[num]

    return render_template("post.html", blog = response)

if __name__ == "__main__":
    app.run(debug=True)
