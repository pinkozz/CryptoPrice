import requests
from bs4 import BeautifulSoup

def get_price(link, headers, element, class_name):
    res = requests.get(link, headers=headers)
    if res.status_code == 200:

        soup = BeautifulSoup(res.content, "html.parser")
        price = soup.find(element, {"class": class_name}).text
        
        price = price[1:3:] + price[4::]

        return float(price)
    else:
        return 0