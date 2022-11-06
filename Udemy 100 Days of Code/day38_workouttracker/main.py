import configparser, requests
from datetime import datetime

config_obj = configparser.ConfigParser()
config_obj.read(r"..\config.ini")
NUTRI_ID = config_obj["ids"]["NUTRITIONIX_ID"]
NUTRI_API_KEYS = config_obj["api keys"]["NUTRITIONIX_API_KEY"]
SHEETY_KEY = config_obj["api keys"]["SHEETY"]

nlp_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
sheety_endpoint = "https://api.sheety.co/fd0106b1139fdf3c32ae29f66eab55e1/myWorkouts/workouts"

headers = {
    "x-app-id": NUTRI_ID,
    "x-app-key": NUTRI_API_KEYS,
}

user_input = input("What exercise did you do today?\n")

nlp_config = {
    "query": user_input,
    "gender": "male",
    "weight_kg": 72.5,
    "height_cm": 175,
    "age": 22,
}

nutri_response = requests.post(url=nlp_endpoint, json=nlp_config, headers=headers).json()

sheety_headers = {
    "Content-Type": "application/json",
    "Authorization": SHEETY_KEY,
}

for i in nutri_response["exercises"]:
    sheety_config = {
        "workout": {
            "date": datetime.today().strftime("%d/%m/%Y"),
            "time": datetime.today().strftime("%X"),
            "exercise": i["name"].title(),
            "duration": i["duration_min"],
            "calories": i["nf_calories"],
        }
    }

    sheety_response = requests.post(url=sheety_endpoint, json=sheety_config, headers=sheety_headers)
    print(sheety_response.text)