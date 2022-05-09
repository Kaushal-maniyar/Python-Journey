import os
from datetime import datetime
import time
import requests
from smtplib import *

MY_EMAIL = os.environ.get('MY_EMAIL')
PASSWORD = os.environ.get('PASSWORD')

current_hour = datetime.now().hour
response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()

data = response.json()

longitude = float(data["iss_position"]["longitude"])
latitude = float(data["iss_position"]["latitude"])

iss_position = (longitude, latitude)

parameter = {
    "lat": 22.303894,
    "lng": 70.802162,
    "formatted": 0
}

sun_info = requests.get(url="https://api.sunrise-sunset.org/json", params=parameter)
sun_info.raise_for_status()
sun_data = sun_info.json()
sunrise = float(sun_data["results"]["sunrise"].split("T")[1].split(":")[0])
sunset = float(sun_data["results"]["sunset"].split("T")[1].split(":")[0])
while True:
    time.sleep(60)
    with SMTP('smtp.gmail.com') as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=PASSWORD)
        if parameter["lat"] - 5 <= latitude <= parameter["lat"] + 5 and parameter["lng"] - 5 <= longitude <= parameter[
                "lng"] + 5 and (sunset < current_hour or current_hour < sunrise):
            connection.sendmail(
                from_addr=MY_EMAIL,
                to_addrs="maniyarkaushal111@gmail.com",
                msg=f'Subject:ISS is coming\n\nLook up right now.')
