import time

import telebot
from telebot import types

from price_parse import *

bot = telebot.TeleBot()  # TOKEN HERE


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    hi = 'привет!'
    info = 'с помощью этого бота можно следить за актуальным курсом BTC, TON, USDT и других токенов.'
    dev = 'разработчик: @yaxzo'
    end = 'хорошего дня!'
    print(message.chat.username)
    bot.reply_to(message, f'{hi}\n{info}\n\n{dev}\n\n{end}')


@bot.message_handler(content_types=['text'])
def send_price(message):
    str = message.text.split()
    num = str[0]
    coin = str[1]
    link = "https://api.binance.com/api/v3/ticker/price?symbol=" + coin
    parse = parsing_price(link)
    cost = parse[0]
    name = parse[1]

    link = 'https://www.cbr-xml-daily.ru/daily_json.js'

    bot.reply_to(message, f'{num} {name} | {round(float(cost) * float(num), 3)} $\n'
                          f'{num} {name} | {round((float(cost) * get_usd(link) * float(num)) // (get_uah(link) / 10), 3)} ₴\n'
                          f'{num} {name} | {round((float(cost) * get_usd(link) * float(num)), 3)} ₽')


bot.infinity_polling()
