import pandas
from smtplib import *
from datetime import *
from random import randint
import os

MY_EMAIL = os.environ.get("MY_EMAIL")
PASSWORD = os.environ.get("PASSWORD")

# Today Information
now = datetime.now()
day = now.day
month = now.month

# Read csv
dataframe = pandas.read_csv('birthdays.csv')
intermediate = dataframe[dataframe.month == month]
people = intermediate[intermediate.day == day]
people_list = people.to_dict(orient='records')

# Pick Formate
pick_one_letter = randint(1, 3)
with open(file=f'./letter_templates/letter_{randint(1, 3)}.txt') as file:
    content = file.read()

with SMTP('smtp.gmail.com') as connection:
    connection.starttls()
    connection.login(user=MY_EMAIL, password=PASSWORD)
    if people_list:
        for person in people_list:
            connection.sendmail(
                from_addr=MY_EMAIL,
                to_addrs=person['email'],
                msg=f'Subject:Happy Birthday\n\n{content.replace("NAME", person["name"])}')
