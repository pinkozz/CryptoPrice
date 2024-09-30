import time
from get_price import get_price

def main():
    link = "https://coinmarketcap.com/currencies/bitcoin/"

    headers = {        
        "User-Agent: Mozilla/5.0 (Linux; Android 10; Pixel 3 XL Build/QPP6.190730.005) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36"
    }

    last_price = 0

    while True:
        if last_price != get_price(link=link, headers=headers, element="span", class_name="clvjgF"):
            print(get_price(link=link, headers=headers, element="span", class_name="clvjgF")[1::])
            last_price = get_price(link=link, headers=headers, element="span", class_name="clvjgF")

if __name__ == "__main__":
    main()
