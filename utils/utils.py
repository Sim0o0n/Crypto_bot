import requests
from peewee import Model, IntegerField, CharField, DateTimeField, SQL, SqliteDatabase

db = SqliteDatabase('crypto_bot.db')


class UserRequest(Model):
    user_id = IntegerField()
    command = CharField()
    timestamp = DateTimeField(constraints=[SQL('DEFAULT CURRENT_TIMESTAMP')])

    class Meta:
        database = db


def initialize_db():
    db.connect()
    db.create_tables([UserRequest], safe=True)


def log_user_request(user_id: int, command: str):
    UserRequest.create(user_id=user_id, command=command)


def get_all_crypto_prices():
    url = "https://api.bybit.com/v2/public/tickers"
    response = requests.get(url)
    data = response.json()
    prices = {}

    if data['ret_code'] == 0:
        for ticker in data['result']:
            symbol = ticker['symbol']
            prices[symbol] = {
                "price": ticker['last_price'],
                "change": ticker['price_24h_pcnt']
            }
    return prices


def get_low_price_cryptos():
    prices = get_all_crypto_prices()
    sorted_prices = sorted(prices.items(), key=lambda x: float(x[1]['price']))
    message = "Криптовалюты с минимальными ценами:\n"
    for symbol, info in sorted_prices[:30]:
        message += f"{symbol}: {info['price']} USD ({info['change']}%)\n"
    return message


def get_max_price_cryptos():
    prices = get_all_crypto_prices()
    sorted_prices = sorted(prices.items(), key=lambda x: float(x[1]['price']), reverse=True)
    message = "Криптовалюты с максимальными ценами:\n"
    for symbol, info in sorted_prices[:30]:
        message += f"{symbol}: {info['price']} USD ({info['change']}%)\n"
    return message


def get_best_crypto():
    prices = get_all_crypto_prices()
    sorted_prices = sorted(prices.items(), key=lambda x: float(x[1]['change']), reverse=True)
    message = "Топ 5 криптовалют с наибольшим ростом за последние сутки:\n"
    for symbol, info in sorted_prices[:5]:
        message += f"{symbol}: {info['price']} USD ({info['change']}%)\n"
    return message


def get_currency_rate():
    url = "https://api.exchangerate-api.com/v4/latest/USD"
    response = requests.get(url)
    data = response.json()
    rates = {}

    if 'rates' in data:
        rates['RUB'] = data['rates'].get('RUB')
        rates['USDT'] = data['rates'].get('USDT', 1)
    message = f"Курс доллара:\nUSD/RUB: {rates['RUB']}\nUSD/USDT: {rates['USDT']}"
    return message
