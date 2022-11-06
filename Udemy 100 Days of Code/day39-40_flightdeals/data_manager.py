import configparser, requests

config_obj = configparser.ConfigParser()
config_obj.read("../config.ini")

KEY = config_obj["api keys"]["SHEETY"]
SHEETY_ENDPOINT = "https://api.sheety.co/fd0106b1139fdf3c32ae29f66eab55e1/flightDeals/prices"

class DataManager:    

    def get_data(self):
        headers = {
            "Content-Type": "application/json",
            "Authorization": KEY,
        }
        self.data = requests.get(url=SHEETY_ENDPOINT, headers=headers)
        return self.data.json()
    
    def update_iata(self, iata_code, row):
        headers = {
            "Content-Type": "application/json",
            "Authorization": KEY,
        }
        params = {
            "price": {
                "iataCode": iata_code,
            }
        }
        requests.put(url=f"{SHEETY_ENDPOINT}/{row}", json=params, headers=headers)