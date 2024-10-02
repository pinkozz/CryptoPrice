import time
import telebot
from get_price import get_price

bot = telebot.TeleBot(token="YOUR_API")

@bot.message_handler(commands=['start'])
def main(message):
    if message.chat.type == "private":
        bot.send_message(message.chat.id, "Hello! Type /track to start tracking BTC price!")

@bot.message_handler(commands=['track'])
def track(message):
    link = "https://coinmarketcap.com/currencies/bitcoin/"

    headers = {        
        "User-Agent": "Mozilla/5.0 (Linux; Android 10; Pixel 3 XL Build/QPP6.190730.005) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36"
    }

    last_price = 0

    while True:
        if last_price != get_price(link=link, headers=headers, element="span", class_name="clvjgF"):
            price = get_price(link=link, headers=headers, element="span", class_name="clvjgF")
            bot.send_message(message.chat.id, price)
            last_price = get_price(link=link, headers=headers, element="span", class_name="clvjgF")

if __name__ == "__main__":
    bot.polling(non_stop=True)
