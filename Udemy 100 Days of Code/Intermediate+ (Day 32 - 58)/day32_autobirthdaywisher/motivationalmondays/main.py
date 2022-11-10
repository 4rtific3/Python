from email import message
import smtplib
import datetime as dt
import random

MY_EMAIL = "jg2test1@gmail.com"
MY_PASSWORD = ""

now = dt.datetime.now()
weekday = now.weekday()

with open("quotes.txt") as df:
    data = df.readlines()

random_quote = random.choice(data)

with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()
    connection.login(MY_EMAIL, MY_PASSWORD)
    if weekday == 0:
        connection.sendmail(from_addr=MY_EMAIL, to_addrs=MY_EMAIL, msg=f"Subject: Inspirational Mondays\n\n{random_quote}")