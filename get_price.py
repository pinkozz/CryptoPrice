import requests
from bs4 import BeautifulSoup

def get_price(link, headers, element, class_name):
    res = requests.get(link, headers=headers)

    soup = BeautifulSoup(res.content, "html.parser")
    price = soup.find(element, {"class": class_name}).text

    return price
