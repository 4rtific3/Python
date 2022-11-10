import configparser, requests

config_obj = configparser.ConfigParser()
config_obj.read("../../config.ini")

KEY = config_obj["api keys"]["SHEETY"]
SHEETY_ENDPOINT = "https://api.sheety.co/fd0106b1139fdf3c32ae29f66eab55e1/flightDeals"

class DataManager:    

    def get_data(self):
        headers = {
            "Content-Type": "application/json",
            "Authorization": KEY,
        }
        self.data = requests.get(url=f"{SHEETY_ENDPOINT}/prices", headers=headers)
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
        requests.put(url=f"{SHEETY_ENDPOINT}/prices/{row}", json=params, headers=headers)
    
    def add_user(self):
        
        f_name = input("What is your first name?\n").title().strip()
        l_name = input("What is your last name?\n").title().strip()
        email = input("What is your email address?\n")
        email_check = input("Please key in your email address again")
        
        if email == email_check:
            headers = {
                "Content-Type": "application/json",
                "Authorization": KEY,
                }
            params = {
                "user": {
                    "firstName": f_name,
                    "lastName": l_name,
                    "email": email,
                    }
            }
            requests.post(url=f"{SHEETY_ENDPOINT}/prices", json=params, headers=headers)
            print("You have successfully joined the flight club!")