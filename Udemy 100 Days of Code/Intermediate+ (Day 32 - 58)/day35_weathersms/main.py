import requests
import os
from twilio.rest import Client

oem_endpoint = "http://api.openweathermap.org/data/2.5/forecast"
apikey = ""
account_sid = ""
auth_token = ""

DENVER_LAT = 39.739235
DENVER_LONG = -104.990250

GALWAY_LAT = 53.273800
GALWAY_LONG = -9.051780

parameters = {
    "lat": GALWAY_LAT,
    "lon": GALWAY_LONG,
    "appid": apikey,
}

wet_weather = False

response = requests.get(oem_endpoint, params=parameters)
response.raise_for_status()
data = response.json()
forecast = data["list"][:4]
for i in forecast:
    if i["weather"][0]["id"] < 700:
        wet_weather = True

if wet_weather:
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body="It's going to rain today.",
        from_='whatsapp:+14155238886',
        to='whatsapp:+000000000'
    )
    
    print(message.status)