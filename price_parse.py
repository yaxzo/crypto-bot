import json
from pprint import pprint

import requests

# defining key/request url
link = "https://api.binance.com/api/v3/ticker/price?symbol=DOGEUSDT"


def parsing_price(link):
    # requesting data from url
    data = requests.get(link)
    data = data.json()

    return [data['price'], data['symbol']]


def get_usd(link):
    data = requests.get(link).json()
    usd = data['Valute']['USD']

    return usd['Value']


def get_uah(link):
    data = requests.get(link).json()
    uah = data['Valute']['UAH']

    return uah['Value']


print(get_uah('https://www.cbr-xml-daily.ru/daily_json.js'))
print(get_usd('https://www.cbr-xml-daily.ru/daily_json.js'))
