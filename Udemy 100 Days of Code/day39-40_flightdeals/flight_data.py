class FlightData:
    
    def __init__(self, price, dep_city, dep_airport, arr_city, arr_airport, dep_date, return_date, link):
        self.price = price
        self.dep_city = dep_city
        self.dep_airport = dep_airport
        self.arr_city = arr_city
        self.arr_airport = arr_airport
        self.dep_date = dep_date
        self.return_date = return_date
        self.link = link