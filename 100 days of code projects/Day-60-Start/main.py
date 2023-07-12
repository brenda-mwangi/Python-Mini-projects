from flask import Flask, render_template, request
import requests
import smtplib
from app_pass import emailpass, my_email
from datetime import datetime
# USE YOUR OWN npoint LINK! ADD AN IMAGE URL FOR YOUR POST. 👇
posts = requests.get("https://api.npoint.io/4152611fd8cc3f8b70c5").json()[1:]

app = Flask(__name__)

year = datetime.now().year

@app.route('/')
def get_all_posts():
    return render_template("index.html", all_posts=posts, current_year= year)


@app.route("/about")
def about():
    return render_template("about.html", current_year= year)


@app.route("/post/<int:index>")
def show_post(index):
    requested_post = None
    for blog_post in posts:
        if blog_post["id"] == index:
            requested_post = blog_post
    return render_template("post.html", post=requested_post, current_year= year)


@app.route("/contact", methods=['get', "post"])
def contact():
    if request.method == "POST":
        name = request.form['name']
        email = request.form['email']
        phone = request.form['phone']
        message = request.form['message']

        mail = "\n\n".join([
                f"Subject: {name} from SmartBlog",
                f"{message}"
            ])

        try:
            connection=smtplib.SMTP("smtp.gmail.com", 587)
            connection.starttls()
            connection.ehlo()
            connection.login(user= my_email, password=emailpass)
            connection.sendmail(from_addr=my_email, to_addrs=email, msg=mail)
            connection.close()
            print("Email sent successfully!")

        except smtplib.SMTPException as e:
            print("Error: unable to send email")
            print(str(e))

        return render_template("contact.html", email=email, message=message, phone=phone, method_used=request.method, success= "Successfully Sent")
    else:
        return render_template("contact.html", current_year= year)


if __name__ == "__main__":
    app.run(debug=True, port=5001)
