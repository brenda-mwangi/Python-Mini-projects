import smtplib
from app_password import app16
my_email = "sheecnc@gmail.com"
msg = "\n\n".join([
  "Subject: Dear Brian",
  "How are you?"
  ])
with smtplib.SMTP("smtp.gmail.com", 587) as connection:
    connection.ehlo()
    connection.starttls()
    connection.login(user=my_email, password=app16)
    connection.sendmail(from_addr=my_email, to_addrs="bryankamaa09@gmail.com", msg=msg)