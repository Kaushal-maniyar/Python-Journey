from twilio.rest import Client
from newsapi import NewsApiClient
from datetime import date, timedelta
import os
import requests

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
URL = "https://www.alphavantage.co/query"

parameters = {
    "apikey": os.environ.get("alpha_key"),
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,

}


response = requests.get(url=URL, params=parameters)
response.raise_for_status()
data = response.json()
change = []
count = 0
for (key, value) in data["Time Series (Daily)"].items():
    if count < 2:
        price_change = float(data["Time Series (Daily)"][key]["4. close"]) - float(
            data["Time Series (Daily)"][key]["1. open"])
        temp = price_change / float(data["Time Series (Daily)"][key]["1. open"]) * 100
        change.append(temp)
        count += 1
    else:
        break

newsapi = NewsApiClient(api_key='9cd631aecc3a49099bb314fed9e12603')
all_articles = newsapi.get_everything(q='Tesla',
                                      sources='bbc-news,the-verge',
                                      domains='bbc.co.uk,techcrunch.com',
                                      from_param=str(date.today() - timedelta(days=2)),
                                      to=str(date.today()),
                                      language='en',
                                      )

emoji = ""
for i in change:
    if i <= -4 or i >= 4:
        if i > 0:
            emoji = "🔺"
        else:
            emoji = "🔻"
        message = f"TSLA: {emoji}{round(i, 2)}%\nHeadline:\n{all_articles['articles'][0]['title']}\nBrief:" \
                  f"\n{all_articles['articles'][0]['description']}"
        client = Client(os.environ.get("sid"), os.environ.get("token"))
        message = client.messages \
            .create(
                body=message,
                from_=os.environ.get("sender"),
                to=os.environ.get("receiver")
            )
        break
