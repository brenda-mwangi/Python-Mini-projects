import smtplib
import datetime as dt
import random
from app_password import app, my_email, address

# create the datetime object
time = dt.datetime.now()
today = time.weekday()

if today == 2:
    with open("quotes.txt", mode="r") as file:
        quotes = [i.strip() for i in file.readlines()]
        quote_of_the_day = random.choice(quotes)
else:
    print("Today is not Monday")

print(time.date())
print(quote_of_the_day)

#send the quote
message = "\n\n".join([
  f"Subject: Quote of the day",
  "",
  f"{quote_of_the_day}"
  ])

connection=smtplib.SMTP("smtp.gmail.com", 587)
connection.starttls()
connection.ehlo()
connection.login(user=my_email, password=app)
connection.sendmail(from_addr=my_email, to_addrs=address, msg=message)
connection.close()