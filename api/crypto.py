import requests


def get_all_crypto_prices():
    url = "https://api.bybit.com/v2/public/tickers"
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()

        prices = {}
        if data['ret_code'] == 0:
            for ticker in data['result']:
                symbol = ticker['symbol']
                prices[symbol] = {
                    "price": float(ticker['last_price']),
                    "change": float(ticker['price_24h_pcnt'])
                }
        return prices
    except requests.RequestException as e:
        print(f"Ошибка запроса к API ByBit: {e}")
        return {}
    except ValueError as e:
        print(f"Ошибка декодирования JSON: {e}")
        return {}


def get_currency_rate():
    url = "https://api.exchangerate-api.com/v4/latest/USD"
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()

        rates = {}
        if 'rates' in data:
            rates['RUB'] = data['rates'].get('RUB')
            rates['USDT'] = data['rates'].get('USDT', 1)
        return rates
    except requests.RequestException as e:
        print(f"Ошибка запроса к API Exchange Rate: {e}")
        return {}
    except ValueError as e:
        print(f"Ошибка декодирования JSON: {e}")
        return {}
