import configparser, requests
import datetime as dt
from flight_data import FlightData
from pprint import pprint

config_obj = configparser.ConfigParser()
config_obj.read("../../config.ini")

KEY = config_obj["api keys"]["TEQUILA"]
TEQUILA_ENDPOINT = "https://api.tequila.kiwi.com"

class FlightSearch:
    
    def get_iata(self, city):
        headers = {
            "accept": "application/json",
            "apikey": KEY,
        }
        config = {
            "term": city,
            "location_types": "city",
            "limit": "1",
        }
        response = requests.get(url=f"{TEQUILA_ENDPOINT}/locations/query", params=config, headers=headers)
        data = response.json()
        return data["locations"][0]["code"]

    def search_flights(self, iata_code):
        headers = {
            "accept": "application/json",
            "apikey": KEY,
        }
        config = {
            "curr": "GBP",
            "fly_from": "LON",
            "fly_to": iata_code,
            "date_from": dt.date.today() + dt.timedelta(days=1),
            "date_to": dt.date.today() + dt.timedelta(days=180),
            "nights_in_dst_from": 7,
            "nights_in_dst_to": 28,
            "flight_type": "round",
            "max_stopovers": 0,
            "limit": 1,
        }
        
        response = requests.get(url=f"{TEQUILA_ENDPOINT}/v2/search", params=config, headers=headers)
        
        try:
            data = response.json()["data"][0]
        except IndexError:
            try:
                config["max_stopovers"] = 1
                response = requests.get(url=f"{TEQUILA_ENDPOINT}/v2/search", params=config, headers=headers)
                data = response.json()["data"][0]
                
                flight_data = FlightData(
                    price=data["price"],
                    dep_city=data["cityFrom"],
                    dep_airport=data["flyFrom"],
                    arr_city=data["cityTo"],
                    arr_airport=data["flyTo"],
                    dep_date=data["local_arrival"].split("T")[0],
                    return_date=data["route"][-1]["local_departure"].split("T")[0],
                    link=data["deep_link"],
                    stop_overs=1,
                    via_city=data["route"][0]["cityTo"],
                )
                
                return flight_data
            
            except IndexError:
                return None
                
        else:
            flight_data = FlightData(
                price=data["price"],
                dep_city=data["cityFrom"],
                dep_airport=data["flyFrom"],
                arr_city=data["cityTo"],
                arr_airport=data["flyTo"],
                dep_date=data["local_arrival"].split("T")[0],
                return_date=data["route"][1]["local_departure"].split("T")[0],
                link=data["deep_link"]
            )
        
            return flight_data
    
