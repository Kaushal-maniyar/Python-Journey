from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import os

EMAIL = os.environ.get('EMAIL')
PASSWORD = os.environ.get('PASSWORD')
# Loading the driver
chrome_driver_path = os.environ.get('CHROME_PATH')
driver_service = Service(chrome_driver_path)
browser = webdriver.Chrome(service=driver_service)
browser.get('https://www.instagram.com/?hl=en')
time.sleep(4)
email_box = browser.find_element(By.NAME, 'username')
email_box.send_keys(EMAIL)
time.sleep(4)
password_box = browser.find_element(By.NAME, 'password')
password_box.send_keys(PASSWORD)
password_box.send_keys(Keys.ENTER)
time.sleep(4)
browser.refresh()
time.sleep(3)
# Not Now Button
browser.find_element(By.XPATH, '/html/body/div[5]/div/div/div/div[3]/button[2]').click()
time.sleep(3)
search_box = browser.find_element(By.XPATH, '//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/input')
search_box.send_keys('online shopping')
time.sleep(3)
result = browser.find_element(By.XPATH, '//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/div[3]/div/div[2]/div/div[1]/a/div/div[2]')
result.click()
time.sleep(5)

followers = browser.find_element(By.XPATH, '//*[@id="react-root"]/section/main/div/header/section/ul/li[2]/a/div')
followers.click()
time.sleep(5)
follow_buttons = browser.find_elements(By.CSS_SELECTOR, 'li button')
print(follow_buttons)
print(len(follow_buttons))
time.sleep(5)
for button in follow_buttons:
    if button.text == "Follow":
        try:
            button.click()
        except:
            pass
    time.sleep(3)
