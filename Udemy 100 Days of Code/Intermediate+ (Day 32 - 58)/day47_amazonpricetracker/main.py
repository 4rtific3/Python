import requests, configparser, smtplib
from email.message import EmailMessage
from bs4 import BeautifulSoup
from pprint import pprint

AMAZON_ENDPOINT = "https://www.amazon.com/dp/B09RKGQB99/ref=vp_d_pb_TIER3_d3_lp_B07PPD1H64_pd?_encoding=UTF8&pf_rd_p=7ff5771e-3d64-43df-8374-83d5fdf6e104&pf_rd_r=Q1CY0BJ5P79JBN0DQC6Q&pd_rd_wg=1FrC0&pd_rd_i=B095Y6ZF5Q&pd_rd_w=nbE17&content-id=amzn1.sym.7ff5771e-3d64-43df-8374-83d5fdf6e104&pd_rd_r=d7784e61-989f-4fc5-ae07-3fbdbbad8dc3&th=1"

config_obj = configparser.ConfigParser()
config_obj.read("../../config.ini")
ACCEPT_LANGUAGE = config_obj["http headers"]["ACCEPT_LANGUAGE"]
USER_AGENT = config_obj["http headers"]["USER_AGENT"]
EMAIL = "jg2test1@gmail.com"
PASSWORD = config_obj["passwords"]["gmail"]

headers = {
    "Accept-Language": ACCEPT_LANGUAGE,
    "User-Agent": USER_AGENT,
}

response = requests.get(AMAZON_ENDPOINT, headers=headers)
soup = BeautifulSoup(response.text, "lxml")

# currency = soup.find("span", class_="a-price-symbol")
# cost_dollar = soup.find("span", class_="a-price-whole")
# cost_cents = soup.find("span", class_="a-price-fraction")

# product_cost = f"{currency}{cost_dollar.text}{cost_cents.text}"

cost = soup.find("span", class_="a-offscreen")
cost = cost.text
cost_float = float(cost.strip("$"))

product_title = soup.find("span", id="productTitle")
product_title = product_title.text.strip()

if cost_float < 60:
    msg = EmailMessage()
    msg["Subject"] = "Amazon Price Alert!"
    msg["From"] = "jg2test1@gmail.com"
    msg["To"] = "jg2test1@gmail.com"
    msg.set_content(f"{product_title} is now {cost}\n{AMAZON_ENDPOINT}")
    with smtplib.SMTP(host="smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=EMAIL, password=PASSWORD)
        connection.send_message(msg)