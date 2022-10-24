import requests
import datetime as dt

MY_LAT = 53.273800
MY_LONG = -9.051780

# response = requests.get("http://api.open-notify.org/iss-now.json")
# response.raise_for_status()

# data = response.json()["iss_position"]
# longitude = data["longitude"]
# latitude = data["latitude"]

# iss_position = (longitude, latitude)
# print(iss_position)

# parsed_data = json.dumps(data)
# print(parsed_data)

parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise_time = data["results"]["sunrise"].split("T")[1].split(":")[0]
sunset_time = data["results"]["sunset"].split("T")[1].split(":")[0]
print(sunrise_time, sunset_time)

time_now = dt.datetime.now()
print(time_now)