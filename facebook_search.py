from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import requests
import re 
import time
import os 

#configure chomedriver

chrome_install = ChromeDriverManager().install()

folder = os.path.dirname(chrome_install)
chromedriver_path = os.path.join(folder, "chromedriver.exe")
chrome_options = Options()
chrome_options.add_argument("--force-device-scale-factor=0.25")

browser = webdriver.Chrome(
    service=Service(chromedriver_path),
    options=chrome_options
)
url = "https://www.facebook.com/marketplace/warsaw/search?daysSinceListed=1&sortBy=creation_time_descend&query=iphone%2013&exact=false&locale=pl_PL"

browser.get(url)

browser.maximize_window()

time.sleep(2)
try:
    decline_button = browser.find_element(By.XPATH, '//div[@aria-label="Odrzuć opcjonalne pliki cookie" and @role="button"]')
    decline_button.click()
    print("rejected cookies")

except:
    print("error while rejecting cookies")
    pass

try:
    close_button = browser.find_element(By.XPATH, '//div[@aria-label="Zamknij" and @role="button"]')
    close_button.click()
    print("Closed login popup")
except:
    print("error while closing login popup")
    pass

try:
    start_height = browser.execute_script("return document.body.scrollHeight")
    while True:
        browser.execute("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(5)

        new_height = browser.execute_script("return document.body.scrollHeight")

        if new_height ==start_height:
            break

        start_height = new_height
        print('scrolled')
except:
    print("error while scroling")
    time.sleep(10)

html = browser.page_source

soup = BeautifulSoup(html, "html.parser")

browser.close()

prices = soup.find_all(string=re.compile(r"zł$"))


for price in prices:

    item_price = price.strip()


    parent_a = price.find_parent("a")  
    if parent_a:
        item_link = parent_a["href"]


        img_tag = parent_a.find("img", alt=True)
        if img_tag:
            item_name = img_tag["alt"]


        print(f"Nazwa: {item_name}")
        print(f"Cena: {item_price}")
        print(f"Link: {item_link}")
        print("-" * 30)


print(len(prices))


