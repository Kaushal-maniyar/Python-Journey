import os
from twilio.rest import Client
import requests

parameter = {
    "lat": 20,
    "lon": 70,
    "appid": os.environ.get("weather_key"),
    "exclude": "current,minutely,daily",
}
account_sid = os.environ.get("sid")
auth_token = os.environ.get("token")
response = requests.get(url=f"https://api.openweathermap.org/data/2.5/onecall", params=parameter)
response.raise_for_status()
weather_data = response.json()
hourly_weather_id = []
for i in range(12):
    hourly_id = weather_data["hourly"][i]["weather"][0]["id"]
    hourly_weather_id.append(hourly_id)
for i in hourly_weather_id:
    if i < 700:
        client = Client(account_sid, auth_token)
        message = client.messages \
            .create(
                body="Bring your umbrella with you, it's raining today.",
                from_=os.environ.get("sender"),
                to=os.environ.get("receiver")
            )
        break
