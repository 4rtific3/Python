import requests
from datetime import datetime
import smtplib
import time

MY_LAT = 53.273800
MY_LONG = -9.051780
MY_EMAIL = "jg2test1@gmail.com"
MY_PASSWORD = "ebwszvmfelunwtnh"

def iss_overhead():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()
    
    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])
    
    lat_diff = MY_LAT - iss_latitude
    long_diff = MY_LONG - iss_longitude
    
    if abs(lat_diff) <= 5 and abs(long_diff) <= 5:
        return True

def is_night():
    if hour_now >= sunset or hour_now <= sunrise:
        return True

parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

time_now = datetime.now()
hour_now = time_now.hour

while True:
    time.sleep(60)
    if iss_overhead() and is_night():
        with smtplib.SMTP(host="smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL, password=MY_PASSWORD)
            connection.sendmail(from_addr=MY_EMAIL, to_addrs=MY_EMAIL, msg="Subject:ISS Overhead\n\nThe ISS is visible in the night sky!")
