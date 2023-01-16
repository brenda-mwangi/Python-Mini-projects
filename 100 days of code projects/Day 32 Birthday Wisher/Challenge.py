import smtplib
import datetime as dt
import random
from app_password import app16

time = dt.datetime.now()
today = time.weekday()

if today == 0:
    with open("quotes.txt", mode="r") as file:
        quotes = [i.strip() for i in file.readlines()]
        quote_of_the_day = random.choice(quotes)
else:
    print("Today is not Monday")

print(time.date())
print(quote_of_the_day)

#send the quote
my_email = "breshshilaxy@yahoo.com"
message = "\n\n".join([
  f"Subject: Quote of the day",
  "",
  f"{quote_of_the_day}"
  ])

connection=smtplib.SMTP("smtp.mail.yahoo.com")
connection.ehlo()
connection.starttls()
connection.login(user=my_email, password="pass")
connection.sendmail(from_addr=my_email, to_addrs="breshshilaxy@gmail.com", msg=message)
connection.close()