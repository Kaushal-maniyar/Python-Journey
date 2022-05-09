import os

import requests
from datetime import datetime

USERNAME = "kaushal111"
TOKEN = os.environ.get("token")
pixela_endpoint = "https://pixe.la/v1/users"
GRAPH_ID = "graph1"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
graph_config = {
    "id": GRAPH_ID,
    "name": "Coding Graph",
    "unit": "No. of Lines",
    "type": "int",
    "color": "sora"
}
header = {
    "X-USER-TOKEN": TOKEN
}
# Post a pixel
today = datetime.now()
pixel_config = {
    "date": today.strftime("%Y%m%d"),
    "quantity": input("How many lines did you type today? :")
}
pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"

response = requests.post(url=pixel_endpoint, json=pixel_config, headers=header)
print(response.text)
'''
# Update a pixel
pixel_update_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime('%Y%m%d')}"

modify_data = {
    "quantity": "100"
}
response = requests.put(url=pixel_update_endpoint, json=modify_data, headers=header)
print(response.text)

# Delete a pixel
delete_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/20220305"
response = requests.delete(url=delete_endpoint, headers=header)
print(response.text)
'''