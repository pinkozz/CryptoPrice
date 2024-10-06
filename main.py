import time
import threading
import telebot
from get_price import get_price

bot = telebot.TeleBot(token="7784526991:AAEzGkfb2vMpPhEh-ullq6Cu6J--k11LOTo")

link = "https://coinmarketcap.com/currencies/bitcoin/"

headers = {        
    "User-Agent": "Mozilla/5.0 (Linux; Android 10; Pixel 3 XL Build/QPP6.190730.005) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36"
}

@bot.message_handler(commands=['start'])
def main(message):
    if message.chat.type == "private":
        bot.send_message(message.chat.id, "Hello! \n\nType /track to start tracking BTC price! \n\nType /alert to set signal once BTC hit certain price mark.")

@bot.message_handler(commands=['track'])
def track(message):
    last_price = 0

    if get_price(link=link, headers=headers, element="span", class_name="clvjgF") == 0:
        bot.send_message(message.chat.id, "The price tracking is currently unavailable")

    try:
        while True:
            if last_price != get_price(link=link, headers=headers, element="span", class_name="clvjgF"):
                price = get_price(link=link, headers=headers, element="span", class_name="clvjgF")
                bot.send_message(message.chat.id, price)
                last_price = get_price(link=link, headers=headers, element="span", class_name="clvjgF")
    except Exception as e:
        bot.send_message(message.chat.id, "An error occurred. Please restart the bot")
        print(e)

def monitor_price(chat_id, target_price, bot, link, headers, element, class_name):
    last_price = 0
    while True:
        current_price = get_price(link, headers, element, class_name)
        if last_price != current_price:
            bot.send_message(chat_id, f"Current BTC price: {current_price}")
            if current_price >= target_price:
                bot.send_message(chat_id, f"BTC has hit your target price of {target_price}!")
                break
            last_price = current_price
        time.sleep(60)

@bot.message_handler(commands=['alert'])
def alert(message):
    if message.chat.type == "private":
        bot.send_message(message.chat.id, "Enter the price mark that you want to be notified about (e.g. 62000.00)")

        @bot.message_handler(func=lambda msg: True)
        def capture_price(msg):
            try:
                target_price = float(msg.text)
                bot.send_message(msg.chat.id, f"Got it! I'll alert you when BTC hits {target_price}")    

                threading.Thread(target=monitor_price, args=(msg.chat.id, target_price, bot, link, headers, "span", "clvjgF")).start()
            except ValueError:
                bot.send_message(msg.chat.id, "Please enter a valid number.")

if __name__ == "__main__":
    bot.polling(non_stop=True)
