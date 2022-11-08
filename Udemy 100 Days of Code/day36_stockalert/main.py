import configparser, requests, json
import datetime as dt
import smtplib
# email library structures emails to send UTF-8 encoded messages as SMTP sendmail only supports ASCII
from email.message import EmailMessage
# The BDay module "Business Days" only calculates work days
from pandas.tseries.offsets import BDay
from pprint import pprint

config_obj = configparser.ConfigParser()
config_obj.read(r"C:\Users\jg2jo\OneDrive\Documents\GitHub\Python\Udemy 100 Days of Code\config.ini")
AV_API_KEY = config_obj["api keys"]["AV_API_KEY"]
NEWS_API_KEY = config_obj["api keys"]["NEWS_API_KEY"]
GMAIL_PASSWORD = config_obj["passwords"]["GMAIL"]

MY_EMAIL = "jg2test1@gmail.com"
STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

article_list = []

yesterday = str(dt.date.today() - BDay(1)).split()[0]
day_before_yesterday = str(dt.date.today() - BDay(2)).split()[0]

av_parameters = {
    "function": "TIME_SERIES_DAILY_ADJUSTED",
    "symbol": STOCK,
    "apikey": AV_API_KEY,
}

news_parameters = {
    "q": COMPANY_NAME,
    "from": yesterday,
    "sortBy": "popularity",
    "apiKey": NEWS_API_KEY,
}

av_response = requests.get("https://www.alphavantage.co/query", params=av_parameters)
av_data = av_response.json()

news_response = requests.get("https://newsapi.org/v2/everything", params=news_parameters)
news_data = news_response.json()

new_price = float(json.dumps(av_data["Time Series (Daily)"][yesterday]["4. close"]).strip("\""))
old_price = float(json.dumps(av_data["Time Series (Daily)"][day_before_yesterday]["4. close"]).strip("\""))

percent_delta = round((new_price - old_price) / old_price * 100, 2)

if percent_delta > 0:
    delta_icon = "▲"
else:
    delta_icon = "▼"

if abs(percent_delta) >= 5:
    for i in range(3):
        article_list.append(news_data["articles"][i]["title"])
        article_list.append(news_data["articles"][i]["description"])
        article_list.append(news_data["articles"][i]["url"])
    
    msg = EmailMessage()
    msg["Subject"] = "TSLA Alert"
    msg["From"] = "jg2test1@gmail.com"
    msg["To"] = "jg2test1@gmail.com"
    msg.set_content(f"""\
TSLA: {delta_icon}{percent_delta}%

Headline: {article_list[0]}
Brief: {article_list[1]}
Link: {article_list[2]}

Headline: {article_list[3]}
Brief: {article_list[4]}
Link: {article_list[5]}

Headline: {article_list[6]}
Brief: {article_list[7]}
Link: {article_list[8]}
""")

    with smtplib.SMTP(host="smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=GMAIL_PASSWORD)
        connection.send_message(msg)




