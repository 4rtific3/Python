# import smtplib

# my_email = "jg2test1@gmail.com"
# password = ""

# with smtplib.SMTP("smtp.gmail.com") as connection:
#     # Transport Layer Security: Securing connection
#     connection.starttls()
#     connection.login(user=my_email, password=password)
#     connection.sendmail(from_addr=my_email, to_addrs="jg2test2@yahoo.com", msg="Subject:Hello\n\nThis is the body of my email.")

# import datetime as dt

# now = dt.datetime.now()
# year = now.year
# day_of_week = now.weekday()

# dob = dt.datetime(year=2000, month=7, day=12)
# print(now)