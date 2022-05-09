import requests
import os
import re

regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'


def check(email):
    if re.fullmatch(regex, email):
        return 1
    else:
        return 0


def double_cross(email1,  email2):
    if email1 == email2:
        return 1
    else:
        return 0


user_endpoint = os.environ.get('USER_END_POINT')


class User:
    def __init__(self):
        self.email = ""
        self.last_name = ""
        self.first_name = ""
        self.re_email = ""

    def new_user(self):
        self.first_name = input("Enter your First Name :\n")
        self.last_name = input("Enter your Last Name :\n")
        self.email = input("Enter your Email :\n")
        self.re_email = input("Re-Enter your Email:\n")
        while (not check(self.email)) or (not double_cross(self.email,self.re_email)):
            print("Something went wrong while entering email!")
            self.email = input("Enter your Email :\n")
            self.re_email = input("Re-Enter your Email:\n")
        self.insert_into_sheet()

    def insert_into_sheet(self):
        user_dict = {
            'user': {
                'firstName': self.first_name,
                'lastName': self.last_name,
                'email': self.email,
            }
        }
        response = requests.post(url=user_endpoint,
                                 json=user_dict,
                                 auth=(os.environ.get("SHEET_USER"), os.environ.get("SHEET_PASSWORD")))
        print(response.text)

    def get_users(self):
        response = requests.get(url=user_endpoint,
                                auth=(os.environ.get("SHEET_USER"), os.environ.get("SHEET_PASSWORD")))
        data = response.json()['user']
        return data
