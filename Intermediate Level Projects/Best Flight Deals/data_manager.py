import requests
import os

sheet_endpoint = os.environ.get('SHEET_END_POINT')


class DataManager:
    def __init__(self):
        response = requests.get(url=sheet_endpoint, auth=(os.environ.get("user"), os.environ.get("password")))
        flight_data = response.json()['prices']
        self.sheet_data = flight_data

    def update_city_code(self, new_sheet_data: list):
        for city in new_sheet_data:
            new_record = {'price': city}
            requests.put(url=f'{sheet_endpoint}/{city["id"]}',
                         auth=(os.environ.get("user"), os.environ.get("password")),
                         json=new_record)
        self.sheet_data = new_sheet_data
