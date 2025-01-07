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


class FacebookSearcher:
    def __init__(self, product="iphone", city="warsaw", days_since_listed = 1):
        #TODO:
        #add so that user can input what they are trying to search
        self.city = city
        self.product = re.sub("[ ]","%20").strip()
        self.days_since_listed = days_since_listed
        self.URL =f"https://www.facebook.com/marketplace/{self.city}/search?daysSinceListed=1&sortBy=creation_time_descend&query={self.product}&exact=false&locale=pl_PL"

        #configure chomedriver

        chrome_install = ChromeDriverManager().install()

        folder = os.path.dirname(chrome_install)
        chromedriver_path = os.path.join(folder, "chromedriver.exe")
        chrome_options = Options()
        chrome_options.add_argument("--force-device-scale-factor=0.25")

        self.browser = webdriver.Chrome(
            service=Service(chromedriver_path),
            options=chrome_options
        )

    def getHTML(self):
        self.browser.get(self.URL)

        self.browser.maximize_window()

        time.sleep(2)
        try:
            decline_button = self.browser.find_element(By.XPATH, '//div[@aria-label="Odrzuć opcjonalne pliki cookie" and @role="button"]')
            decline_button.click()
            print("rejected cookies")

        except:
            print("error while rejecting cookies")
            pass

        try:
            close_button = self.browser.find_element(By.XPATH, '//div[@aria-label="Zamknij" and @role="button"]')
            close_button.click()
            print("Closed login popup")
        except:
            print("error while closing login popup")
            pass
        
        #TODO:
        #Fix scrolling if necesary

        try:
            start_height = self.browser.execute_script("return document.body.scrollHeight")
            while True:
                self.browser.execute("window.scrollTo(0, document.body.scrollHeight);")
                time.sleep(5)

                new_height = self.browser.execute_script("return document.body.scrollHeight")

                if new_height ==start_height:
                    break

                start_height = new_height
                print('scrolled')
        except:
            print("error while scroling")
            time.sleep(10)

        html = self.browser.page_source
        self.browser.close()

        return html
    def getProductsInfo(self):

        html = self.getHTML()
        product_info = []

        soup = BeautifulSoup(html, "html.parser")
        prices = soup.find_all(string=re.compile(r"zł$"))

        for price in prices:

            item_price = price.strip()

            parent_a = price.find_parent("a")  
            if parent_a:
                item_link = f"https://www.facebook.com{parent_a['href']}"


                img_tag = parent_a.find("img", alt=True)
                if img_tag:
                    item_name = img_tag["alt"]

                product ={
                    "title" : item_name,
                    "price" : item_price,
                    "link" : item_link
                }

                #print(product)

                # print(f"Nazwa: {item_name}")
                # print(f"Cena: {item_price}")
                # print(f"Link: {item_link}")
                # print("-" * 30)

                product_info.append(product)

        return product_info
    
    def printInfo(self, product_list):
        for product in product_list:

            print(f"Nazwa: {product['title']}")
            print(f"Cena: {product['price']}")
            print(f"Link: {product['link']}")
            print("-" * 30)
