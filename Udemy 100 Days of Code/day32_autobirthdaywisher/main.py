##################### Extra Hard Starting Project ######################
import smtplib
import datetime as dt
import pandas as pd
import random

LETTERS = ["letter_templates/letter_1.txt", "letter_templates/letter_2.txt", "letter_templates/letter_3.txt"]
MY_EMAIL = "jg2test1@gmail.com"
MY_PASSWORD = ""

data = pd.read_csv("birthdays.csv")
data_dict = {(data_row["month"], data_row["day"]): data_row for (index, data_row) in data.iterrows()}

today = (dt.datetime.now().month, dt.datetime.now().day)


# 1. Update the birthdays.csv
def add_birthday():
    name = input("What is your name? ")
    email = input("What is your email? ")
    dob = input("What is your date of birth? [YYYY/MM/DD] ")
    
    birth_date = "/".split(dob)[2]
    birth_month = "/".split(dob)[1]
    birth_year = "/".split(dob)[0]
    
    add_line = ",".join(name,email,birth_date,birth_month,birth_year)
    
    with open("birthdays.csv", "a") as df:
        df.write(f"{add_line}")


if today in data_dict:
    file_path = f"letter_templates/letter_{random.randint(1, 3)}.txt"
    birthday_person = data_dict[today]["name"]
    with open(file_path) as letter:
        contents = letter.read()
        birthday_letter = contents.replace("[NAME]", birthday_person)
    with smtplib.SMTP(host="smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=MY_PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL, to_addrs=data_dict[today]["email"], msg=f"Subject:Happy Birthday!\n\n{birthday_letter}")




