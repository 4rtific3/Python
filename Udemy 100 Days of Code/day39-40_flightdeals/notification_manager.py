import configparser, smtplib

config_obj = configparser.ConfigParser()
config_obj.read("../config.ini")
EMAIL_USER = "jg2test1@gmail.com"
EMAIL_PASS = config_obj["passwords"]["GMAIL"]



class NotificationManager:

    def send_email(self, flight_data):
        EMAIL_CONTENT = f"Low price alert! Only GBP {flight_data.price} to fly from \
{flight_data.dep_city}-{flight_data.dep_airport} to {flight_data.arr_city}-{flight_data.arr_airport}, \
from {flight_data.dep_date} to {flight_data.return_date}\nLink: {flight_data.link}"

        with smtplib.SMTP(host="smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=EMAIL_USER, password=EMAIL_PASS)
            connection.sendmail(from_addr=EMAIL_USER, to_addrs=EMAIL_USER, msg=f"Subject:Flight Deal Found!\n\n{EMAIL_CONTENT}")