from bs4 import BeautifulSoup
import requests
import re

#maybe add phone name as variable
      

class olxSearcher:
    def __init__(self, OLX_URL_PAGE1, OLX_URL_PAGE2, MAXPRICE, MINPRICE, PHONE_NAME):
        self.OLX_URL_PAGE1 = OLX_URL_PAGE1
        self.OLX_URL_PAGE2 = OLX_URL_PAGE2
        self.MAXPRICE = MAXPRICE
        self.MINPRICE = MINPRICE
        self.PHONE_NAME = PHONE_NAME
    

    def getPhonesinfo(self):

        BannedKeywords = [
            "opakowanie",
            "wymiana",
            "plecki",
            "korpus",
            "naprawa",
            "pokrowiec"
        ]




        response = requests.get(self.OLX_URL_PAGE1) 
        soup = BeautifulSoup(response.text, 'html.parser')
        prices = soup.find_all(string=re.compile(r"zł$"))
        self.phonelist = []
        for item in prices:
            if item.parent.parent.find('a') is None:
                continue
            link = f"https://www.olx.pl/{item.parent.parent.find('a').get('href')}/"
            title = item.parent.parent.find("h4").string
            price_element =item.parent.parent.parent.find_all("p")[0]
            id = item.find_parent('div', {'data-cy': 'l-card'}).get('id')

            
            for span in price_element.find_all("span"):
                span.decompose()

            price = price_element.string


            if price is not None:
                price = re.sub("[zł ]","",price).strip()
                price_float = float(re.sub("[,]",".",price).strip())
            else:
                price_float = None
            time_location = item.parent.parent.parent.find_all("p")[1].string
            
            

            if price_float is not None and price_float>=self.MINPRICE and price_float<=self.MAXPRICE:

                if self.PHONE_NAME in title.lower() or re.sub("[ ]","",self.PHONE_NAME) in title.lower() and title.lower() not in BannedKeywords:
                    

                    phone = {
                        "link": link,
                        "title" : title,
                        "price" : price,
                        "time_location" : time_location,
                        "id" : id # for database purpouses
                    }
                    self.phonelist.append(phone)
        response = requests.get(self.OLX_URL_PAGE2) 
        soup = BeautifulSoup(response.text, 'html.parser')
        prices = soup.find_all(string=re.compile(r"zł$"))

        for item in prices:

            link = f"https://www.olx.pl/{item.parent.parent.find('a').get('href')}/"
            title = item.parent.parent.find("h4").string
            price_element =item.parent.parent.parent.find_all("p")[0]
            id = item.find_parent('div', {'data-cy': 'l-card'}).get('id')

            
            for span in price_element.find_all("span"):
                span.decompose()

            price = price_element.string


            if price is not None:
                price = re.sub("[zł ]","",price).strip()
                price_float = float(re.sub("[,]",".",price).strip())

            time_location = item.parent.parent.parent.find_all("p")[1].string
            
            if price_float>=self.MINPRICE and price_float<=self.MAXPRICE:

                if self.PHONE_NAME in title.lower() or re.sub("[ ]","",self.PHONE_NAME) in title.lower():
                    

                    phone = {
                        "link": link,
                        "title" : title,
                        "price" : price,
                        "time_location" : time_location,
                        "id" : id # for database purpouses
                    }
                    self.phonelist.append(phone)
                    print(phone)
     

        return self.phonelist
    
    def printList(self):
        for item in self.phonelist:
        
            print(f"title: {item['title']}")
            print(f"price: {item['price']} zł")
            print(f"time and location: {item['time_location']}")
            print(f"link: {item['link']}")
            print(f"id: {item['id']}")
            print("+------------------------+")



        
                