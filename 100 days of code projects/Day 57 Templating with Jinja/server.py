from flask import Flask, render_template
import random
from datetime import datetime
import requests

app = Flask(__name__)

@app.route('/')
def home():
    random_num = random.randint(1,10)
    year = datetime.now().year
    return render_template("index.html", num=random_num, current_year=year)


@app.route("/guess/<string:name>")
def guess(name):
    gender_url = f"https://api.genderize.io?name={name}"
    age_url = f"https://api.agify.io?name={name}"

    gender_response = requests.get(url=gender_url)
    age_response = requests.get(url=age_url)

    gender = gender_response.json()['gender']
    age = int(age_response.json()['age'])

    return render_template("genderage.html", name=name, gender=gender, age=age)

@app.route("/blogs")
def get_blogs():
    url = "https://api.npoint.io/4152611fd8cc3f8b70c5"
    response = requests.get(url)
    data = response.json()[1:]
    return render_template("blogs.html", data=data)


@app.route("/blogs/<int:num>")
def get_individual_blog(num):
    url = "https://api.npoint.io/4152611fd8cc3f8b70c5"
    data = requests.get(url).json()
    print(data[num])
    return render_template("oneBlog.html", data=data[num])

if __name__ == "__main__":
    app.run(debug=True)
