from smtplib import *
from twilio.rest import Client
import os

MY_EMAIL = os.environ.get("EMAIL")
PASSWORD = os.environ.get("EMAIL_PASSWORD")


class NotificationManager:
    def __init__(self, founds: list):
        if founds:
            for deal in founds:
                message = f"Low price alert!\n" \
                      f"Only $ {deal['price']} to fly from London-{deal['origin_airport']} " \
                      f"to {deal['destination_city']}" \
                      f"-{deal['destination_airport']} from {deal['out_date']} to {deal['return_date']}"
                client = Client(os.environ.get("SSID"), os.environ.get("TOKEN"))
                client.messages.create(
                    body=message,
                    from_=os.environ.get("SENDER"),
                    to=os.environ.get("RECEIVER")
                )

    def send_email(self, users: list, founds: list):
        if founds:
            for deal in founds:
                message = f"Subject:Low price alert!\n\n" \
                          f"Only $ {deal['price']} to fly from London-{deal['origin_airport']} " \
                          f"to {deal['destination_city']}" \
                          f"-{deal['destination_airport']} from {deal['out_date']} to {deal['return_date']}"
                for user in users:
                    with SMTP('smtp.gmail.com') as connection:
                        connection.starttls()
                        connection.login(user=MY_EMAIL, password=PASSWORD)
                        connection.sendmail(
                            from_addr=MY_EMAIL,
                            to_addrs=user['email'],
                            msg=message)
