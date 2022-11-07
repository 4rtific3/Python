from data_manager import DataManager
from flight_search import FlightSearch
from notification_manager import NotificationManager

data_manager = DataManager()
flight_search = FlightSearch()
notification_manager = NotificationManager()

raw_sheety_data = data_manager.get_data()["prices"]
sheet_data = [i for i in raw_sheety_data]

# # Function to fill in empty IATA Codes
# for i in sheet_data:
#     if not i["iataCode"]:
#         city = i["city"]
#         iata_code = flight_search.get_iata(city)
#         data_manager.update_iata(iata_code, i["id"])

for destination in sheet_data:
    flight_data = flight_search.search_flights(destination["iataCode"])
    if flight_data == None:
        print(f'No flights with only 1 stopover for {destination["city"]} were found.')
        continue
    if flight_data.price < destination["lowestPrice"]:
        notification_manager.send_email(flight_data)


