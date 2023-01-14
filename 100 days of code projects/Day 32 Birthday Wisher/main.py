import smtplib

my_email = "sheecnc@gmail.com"
msg = "\n\n".join([
  "Subject: Just a message",
  "Why, oh why"
  ])
with smtplib.SMTP("smtp.gmail.com", 587) as connection:
    connection.ehlo()
    connection.starttls()
    connection.login(user=my_email, password="wznmzkpaotyyrucu")
    connection.sendmail(from_addr=my_email, to_addrs="breshshilaxy@yahoo.com", msg=msg)