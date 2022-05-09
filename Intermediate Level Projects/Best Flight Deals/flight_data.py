import os
import requests
from datetime import datetime, timedelta

tomorrow = datetime.today() + timedelta(1)
six_month = tomorrow + timedelta(180)
TEQUILA_API_KEY = os.environ.get("kiwi_key")
headers = {"apikey": TEQUILA_API_KEY}


class FlightData:
    def __init__(self):
        self.price: int
        self.departure_airport_code = "LON"
        self.departure_city = "London"
        self.database = {}

    def search(self, city_code: str):
        response = requests.get(url=f"https://tequila-api.kiwi.com/v2/search?fly_from={self.departure_airport_code}"
                                    f"&fly_to={city_code}&dateFrom={tomorrow.strftime('%d/%m/%Y')}"
                                    f"&dateTo={six_month.strftime('%d/%m/%Y')}&"
                                    f"nights_in_dst_from=7&nights_in_dst_to=28&flight_type=round&one_for_city=1"
                                    f"&max_stopovers=0&curr=GBP",
                                headers=headers,)
        try:
            data = response.json()["data"][0]
            result_dict = {
                "price": data['price'],
                "origin_city": data['route'][0]['cityFrom'],
                "origin_airport": data['route'][0]['flyFrom'],
                "destination_city": data['route'][0]['cityTo'],
                "destination_airport": data['route'][0]['flyTo'],
                "out_date": data['route'][0]['local_departure'].split('T')[0],
                "return_date": data['route'][1]['local_departure'].split('T')[0]
                }
            self.database[city_code] = result_dict
        except IndexError:
            print(f"No flights found for {city_code}.")
