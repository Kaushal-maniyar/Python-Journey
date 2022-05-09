from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import requests
import time
import os

USER_AGENT = os.environ.get('USER_AGENT')
response = requests.get("https://www.zillow.com/ny/rentals/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C"
                        "%22usersSearchTerm%22%3A%22NY%22%2C%22mapBounds%22%3A%7B%22west%22%3A-81.59279440625%2C"
                        "%22east%22%3A-69.94728659375%2C%22south%22%3A38.78926849997137%2C%22north%22%3A46"
                        ".544564185211435%7D%2C%22regionSelection%22%3A%5B%7B%22regionId%22%3A43%2C%22regionType%22"
                        "%3A2%7D%5D%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22fsba%22%3A%7B%22value%22"
                        "%3Afalse%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D"
                        "%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22auc"
                        "%22%3A%7B%22value%22%3Afalse%7D%2C%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22ah%22%3A%7B"
                        "%22value%22%3Atrue%7D%2C%22mp%22%3A%7B%22max%22%3A2000%7D%2C%22price%22%3A%7B%22max%22"
                        "%3A463801%7D%7D%2C%22isListVisible%22%3Atrue%2C%22mapZoom%22%3A6%7D",
                        headers={"Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8,ar;q=0.7", "User-Agent": USER_AGENT})
webpage = response.text
soup = BeautifulSoup(webpage, "html.parser")
prices = soup.find_all(class_="list-card-price")
links = soup.find_all(name='a', class_="list-card-link", href=True)
addresses = soup.find_all(name='address', class_='list-card-addr')
price_list = []
link_list = []
address_list = []
for i in range(len(prices)):
    price_list.append(prices[i].text)
    link_list.append(links[i]['href'])
    address_list.append(addresses[i].text)
print(price_list)
print(link_list)
print(address_list)

chrome_driver_path = "C:/Users/TWINKLE/Downloads/chromedriver_win32/chromedriver.exe"
driver_service = Service(chrome_driver_path)
browser = webdriver.Chrome(service=driver_service)
browser.get('https://docs.google.com/forms/d/e/1FAIpQLSeBeZcyRz1fEzqPsNWktSOCcQverGo5AHBHsTEvXYS3vs7GQA/viewform?usp'
            '=sf_link')
i = 0
while i <= len(price_list):
    time.sleep(3)
    address = browser.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div['
                                             '1]/div/div[1]/input')
    address.send_keys(address_list[i])
    price = browser.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div['
                                           '1]/div/div[1]/input')
    price.send_keys(price_list[i])
    link = browser.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div['
                                          '1]/div/div[1]/input')
    link.send_keys(link_list[i])
    browser.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span/span').click()
    i += 1
    time.sleep(3)
    browser.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[1]/div/div[4]/a').click()
