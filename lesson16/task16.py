# Створіть клас, який реалізує підключення до API НБУ ( документація тут https://bank.gov.ua/ua/open-data/api-dev ).
# Обʼєкт класу повинен вміти отримувати курс валют станом на певну дату. Обʼєкт класу повинен вміти записати курси
# в текстовий файл. Назва файлу повинна містити дату на яку шукаємо курс, наприклад:
#  21_11_2019.txt
# Дані в файл запишіть у вигляді списку :
#
# 1. [назва валюти 1] to UAH: [значення курсу до валюти 1]
# 2. [назва валюти 2] to UAH: [значення курсу до валюти 2]
# 3. [назва валюти 3] to UAH: [значення курсу до валюти 3]
# ...
# n. [назва валюти n] to UAH: [значення курсу до валюти n]
# P.S. Архітектура класу - на розсуд розробника. Не забувайте про DRY, KISS, YAGNI, SRP та перевірки!)
import requests
import datetime

class ExchangeRate:

    currency = None
    rate = None

    def __init__(self, currency, rate):
        self.currency = currency
        self.rate = rate

    def __str__(self):
        return f'{self.currency} to UAH: {self.rate}'

    def __repr__(self):
        return f'{self.currency} to UAH: {self.rate}'


class ExchangeRateParser:

    exchange_rates = []
    rate_url = 'https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange?json'

    def get_exchange_rate(self):

        try:
            response = requests.get(self.rate_url)
        except Exception as e:
            print(e)
            response = None

        if response:
            if 300 > response.status_code >= 200:
                if 'application/json' in response.headers.get('Content-Type', ''):
                    try:
                        response_json = response.json()
                    except Exception as e:
                        print(e)
                    else:
                        print(response_json)

                        for exchange_rate in response_json:
                            currency = exchange_rate.get('cc', {})
                            rate = exchange_rate.get('rate', {})
                            self.exchange_rates.append(ExchangeRate(currency, rate))
                        print(self.exchange_rates)

    def write_down_rate(self):
        self.get_exchange_rate()

        with open(datetime.datetime.now().strftime("%d_%m_%Y.txt"), 'w') as file:
            for exchange_rate in self.exchange_rates:
                file.write(str(exchange_rate) + '\n')


parser = ExchangeRateParser()
parser.write_down_rate()
