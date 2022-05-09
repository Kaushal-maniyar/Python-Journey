from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import os

EMAIL = os.environ.get('EMAIL')
NUMBER = os.environ.get('NUMBER')
PASSWORD = os.environ.get('PASSWORD')
print(PASSWORD)
# Loading the driver
chrome_driver_path = os.environ.get('CHROME_PATH')
driver_service = Service(chrome_driver_path)
browser = webdriver.Chrome(service=driver_service)
browser.get("https://www.speedtest.net/")
go = browser.find_element(By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[1]/a/span[4]')

go.click()
time.sleep(65)

down = browser.find_element(By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span')
down_speed = down.text
print(down_speed)

up = browser.find_element(By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[3]/div/div[2]/span')
up_speed = up.text
print(up_speed)

# New Tab
browser.execute_script("window.open('');")
twitter_window = browser.window_handles[1]
browser.switch_to.window(twitter_window)
browser.get("https://twitter.com/login")
time.sleep(5)

input_box = browser.find_element(By.TAG_NAME, 'input')
input_box.send_keys(EMAIL)
input_box.send_keys(Keys.ENTER)
time.sleep(4)

mobile_no_box = browser.find_element(By.TAG_NAME, 'input')
mobile_no_box.send_keys(NUMBER)
mobile_no_box.send_keys(Keys.ENTER)
time.sleep(4)

password_box = browser.find_element(By.XPATH, '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input')
password_box.send_keys(PASSWORD)
password_box.send_keys(Keys.ENTER)
time.sleep(4)

text_box = browser.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/label/div[1]/div/div/div/div/div[2]/div/div/div/div')
text_box.send_keys(f"@Vi_news My down speed is {down_speed} and my up speed is {up_speed}.")
time.sleep(3)

tweet = browser.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[3]/div/div/div[2]/div[3]/div/span/span')
tweet.click()
