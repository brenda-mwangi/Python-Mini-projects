import smtplib
from app_password import app, my_email, special
msg = "\n\n".join([
  "Subject: Dear Brian",
  "How are you?"
  ])
with smtplib.SMTP("smtp.gmail.com", 587) as connection:
    connection.ehlo()
    connection.starttls()
    connection.login(user=my_email, password=app)
    connection.sendmail(from_addr=my_email, to_addrs= special, msg=msg)