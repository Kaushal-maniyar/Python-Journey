from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
import os

EMAIL = os.environ.get("EMAIL")
# Loading the driver
options = webdriver.ChromeOptions()
options.add_argument(f"user-data-dir={os.environ.get('DIR')}")
chrome_driver_path = os.environ.get('CHROME_PATH')
driver_service = Service(chrome_driver_path)
browser = webdriver.Chrome(service=driver_service, options=options)

browser.get("https://tinder.com/app/recs")

time.sleep(20)
like_button = browser.find_element(By.XPATH, '//*[@id="q939012387"]/div/div[1]/div/main/div[1]/div/div/div[1]/div[1]/'
                                             'div/div[4]/div/div[4]/button/span/span')
for i in range(10):
    like_button.click()
    time.sleep(10)
