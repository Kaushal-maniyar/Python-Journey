import requests
import os
from smtplib import *
from bs4 import BeautifulSoup

MY_EMAIL = os.environ.get("MY_EMAIL")
PASSWORD = os.environ.get("PASSWORD")
USER_AGENT = os.environ.get("USER_AGENT")
response = requests.get("https://www.amazon.in/WOW-Organic-Vinegar-Foaming-Built/dp/B07SQXPW35/ref=sr_1_1_sspa?crid=CXV3AD8QL228&keywords=wow%2Bface%2Bwash%2Bfor%2Boily%2Bskin&qid=1649736552&smid=A2WK4OB3ROODF0&sprefix=wow%2Bface%2Bwash%2Bfor%2Caps%2C241&sr=8-1-spons&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUEzTUpTS0w2RzY3OFVOJmVuY3J5cHRlZElkPUEwMjkwOTExM0NTVE1CSTFPMDYwRyZlbmNyeXB0ZWRBZElkPUEwNTkyMjkzMkVSOEdKNjBZWkRaNyZ3aWRnZXROYW1lPXNwX2F0ZiZhY3Rpb249Y2xpY2tSZWRpcmVjdCZkb05vdExvZ0NsaWNrPXRydWU&th=1",
                        headers={"Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8,ar;q=0.7", "User-Agent": USER_AGENT})

webpage = response.text
soup = BeautifulSoup(webpage, "lxml")
price = float(soup.find(name="span", class_="a-offscreen").text[1::])
print(price)
if price <= 270:
    with SMTP('smtp.gmail.com', port=587) as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=PASSWORD)
        connection.sendmail(
                    from_addr=MY_EMAIL,
                    to_addrs="maniyarkaushal111@gmail.com",
                    msg=f'Subject:Price Alert!!\n\nWow face wash\nBuy it Now\nhttps://www.amazon.in/WOW-Organic-Vinegar-Foaming-Built/dp/B07SQXPW35/ref=sr_1_1_sspa?crid=CXV3AD8QL228&keywords=wow%2Bface%2Bwash%2Bfor%2Boily%2Bskin&qid=1649736552&smid=A2WK4OB3ROODF0&sprefix=wow%2Bface%2Bwash%2Bfor%2Caps%2C241&sr=8-1-spons&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUEzTUpTS0w2RzY3OFVOJmVuY3J5cHRlZElkPUEwMjkwOTExM0NTVE1CSTFPMDYwRyZlbmNyeXB0ZWRBZElkPUEwNTkyMjkzMkVSOEdKNjBZWkRaNyZ3aWRnZXROYW1lPXNwX2F0ZiZhY3Rpb249Y2xpY2tSZWRpcmVjdCZkb05vdExvZ0NsaWNrPXRydWU&th=1')
