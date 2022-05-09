from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
import re


def get_cookie_count():
    cookies = browser.find_element(By.ID, 'cookies')
    number = re.split(" ", cookies.text)[0]
    if ',' in number:
        count = int(number.replace(',', ''))
    else:
        count = int(number)
    return count


# Loading the driver
chrome_driver_path = "C:/Users/TWINKLE/Downloads/chromedriver_win32/chromedriver.exe"
driver_service = Service(chrome_driver_path)
browser = webdriver.Chrome(service=driver_service)

browser.get("https://orteil.dashnet.org/cookieclicker/")
cookie = browser.find_element(By.XPATH, '//*[@id="bigCookie"]')

start = time.time()
break_time = start + 60
while True:
    cookie.click()
    if time.time() > start + 5:
        price_list = []
        items_list = []
        items_dict = {}
        cookie_count = get_cookie_count()
        items = browser.find_elements(By.CSS_SELECTOR, '.content .title')
        price = browser.find_elements(By.CLASS_NAME, 'price')
        for item in items:
            if item.text != '':
                if item.text not in items_list and not re.findall("[0-9]", item.text):
                    items_list.append(item.text)

        for p in price:
            if p.text != '':
                if int(p.text.replace(',', '')) not in price_list:
                    price_list.append(int(p.text.replace(',', '')))
        i = 0
        for item in items_list:
            items_dict[f'product{i}'] = price_list[i]
            i += 1
        # Clicking
        i = i - 1
        while i >= 0:
            while cookie_count > items_dict[f'product{i}']:
                try:
                    browser.find_element(By.ID, f'product{i}').click()
                except:
                    pass
                finally:
                    cookie_count = get_cookie_count()
            i -= 1
        start = time.time()
    if time.time() > break_time:
        break

print(browser.find_element(By.ID, 'cookies').text)
