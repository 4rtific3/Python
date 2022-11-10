class FlightData:
    
    def __init__(self, price, dep_city, dep_airport, arr_city, arr_airport, dep_date, return_date, link, stop_overs=0, via_city=""):
        self.price = price
        self.dep_city = dep_city
        self.dep_airport = dep_airport
        self.arr_city = arr_city
        self.arr_airport = arr_airport
        self.dep_date = dep_date
        self.return_date = return_date
        self.link = link
        self.stop_overs = stop_overs
        self.via_city_1 = via_city