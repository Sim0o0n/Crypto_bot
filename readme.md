# Telegram Crypto Bot (EN)

This bot provides information about cryptocurrencies and exchange rates. It uses the Bybit API to deliver real-time information.

## Installation

1. Clone the repository:
    ```
    git clone https://github.com/Sim0o0n/Crypto_bot
    ```
2. Install dependencies:
    ```
    pip install -r requirements.txt
    ```
3. Configure the Telegram bot token in the `main.py` file:
    ```python
    application = Application.builder().token("YOUR_TOKEN").build()
    ```
4. Run the bot:
    ```
    python main.py
    ```

## Commands and Sample Outputs

- `/start` - Start the bot.
    ```
    Hello! I'm a bot for getting cryptocurrency prices.
    Commands:
    /low_prices - Cryptocurrencies with the lowest prices
    /max_prices - Cryptocurrencies with the highest prices
    /best_crypto - Top cryptocurrencies of the last 24 hours
    /currency_rate - Exchange rates
    /history - User query history
    ```
- `/low_prices` - Prices of cryptocurrencies with the lowest price.
    ```
    Cryptocurrencies with the lowest prices:
    SPELLUSDT: 0.0005937 USD (0.105174%)
    1000BTTUSDT: 0.0007617 USD (0.061306%)
    DENTUSDT: 0.0008250 USD (0.057285%)
    ZBCNUSDT: 0.000980 USD (0.054897%)
    10000LADYSUSDT: 0.0010252 USD (0.090406%)
    REEFUSDT: 0.001204 USD (0.082733%)
    1000000BABYDOGEUSDT: 0.0012184 USD (0.132973%)
    10000SATSUSDT: 0.001229 USD (0.024166%)
    XCNUSDT: 0.0013532 USD (0.073116%)
    MOBILEUSDT: 0.001391 USD (0.04351%)
    HOTUSDT: 0.001496 USD (0.111441%)
    ZKFUSDT: 0.001669 USD (0.088005%)
    LEVERUSDT: 0.002045 USD (0.052496%)
    VTHOUSDT: 0.002141 USD (0.085149%)
    MBLUSDT: 0.002149 USD (0.04727%)
    1CATUSDT: 0.002163 USD (0.060814%)
    SLPUSDT: 0.002393 USD (0.136277%)
    10000000AIDOGEUSDT: 0.002555 USD (0.122583%)
    MYRIAUSDT: 0.003037 USD (0.098372%)
    FUNUSDT: 0.003176 USD (0.094417%)
    VRAUSDT: 0.003186 USD (0.112041%)
    MEWUSDT: 0.003506 USD (0.092892%)
    XVGUSDT: 0.0036420 USD (0.136526%)
    FITFIUSDT: 0.003836 USD (0.068523%)
    SCUSDT: 0.003965 USD (0.077445%)
    10000NFTUSDT: 0.004302 USD (0.029432%)
    RSRUSDT: 0.004304 USD (0.093495%)
    LINAUSDT: 0.004826 USD (0.064872%)
    STMXUSDT: 0.004920 USD (0.286274%)
    KEYUSDT: 0.0049795 USD (0.100685%)
    ```
- `/max_prices` - Prices of cryptocurrencies with the highest price.
    ```
    Cryptocurrencies with the highest prices:
    BTCUSDZ24: 59464.00 USD (0.04352%)
    BTCUSDU24: 57890.00 USD (0.04249%)
    BTCUSD: 56742.00 USD (0.041309%)
    BTCUSDT: 56739.10 USD (0.041309%)
    YFIUSDT: 6183 USD (0.135328%)
    ETHUSDZ24: 3152.55 USD (0.044011%)
    ETHUSDU24: 3067.45 USD (0.043137%)
    ETHUSD: 3005.20 USD (0.043544%)
    ETHUSDT: 3003.74 USD (0.042082%)
    PAXGUSDT: 2348 USD (0.004706%)
    MKRUSDT: 2273.9 USD (0.123857%)
    BNBUSDT: 509.80 USD (0.086414%)
    BCHUSDT: 328.50 USD (0.095%)
    GNOUSDT: 242.94 USD (0.075526%)
    TAOUSDT: 223.80 USD (0.079438%)
    XMRUSDT: 155.98 USD (0.105927%)
    SOLUSDT: 139.910 USD (0.10978%)
    SOLUSD: 139.87 USD (0.109727%)
    AAVEUSDT: 80.98 USD (0.069466%)
    TRBUSDT: 80.910 USD (0.104422%)
    QNTUSDT: 74.20 USD (0.077705%)
    LTCUSDT: 62.66 USD (0.061134%)
    LTCUSD: 62.56 USD (0.05962%)
    ILVUSDT: 56.525 USD (0.079339%)
    COMPUSDT: 46.17 USD (0.070236%)
    METISUSDT: 37.05 USD (0.068955%)
    BSVUSDT: 35.96 USD (0.079879%)
    EGLDUSDT: 33.05 USD (0.17157%)
    SSVUSDT: 28.630 USD (0.011839%)
    ORDIUSDT: 28.300 USD (0.044357%)
    ```
- `/best_crypto` - Top 5 cryptocurrencies with the highest growth in the last 24 hours.
    ```
    Top 5 cryptocurrencies with the highest growth in the last 24 hours:
    10000COQUSDT: 0.01615 USD (0.36172%)
    ZROUSDT: 4.1419 USD (0.358356%)
    POPCATUSDT: 0.5121 USD (0.303053%)
    STMXUSDT: 0.004910 USD (0.282654%)
    UNFIUSDT: 4.7620 USD (0.272751%)
    ```
- `/currency_rate` - Exchange rates.
    ```
    USD exchange rate:
    USD/RUB: 88.43
    USD/USDT: 1
    ```
- `/history` - Query history.
    ```
    User query history:
    User ID: 00000000000, Command: currency_rate, Time: 2024-07-06 10:00:18
    ```

## Description

The bot uses libraries to work with various APIs and requests. It supports multiple users and stores their query history in a database using the Peewee ORM.

## Errors

When entering non-existent commands or incorrect data, the bot displays a corresponding notification.

## Interacting with ByBit API
### Command /low_prices
    ```
    Request:
    url = "https://api.bybit.com/v2/public/tickers"
    response = requests.get(url)
    data = response.json()

    Response:
    {
        "ret_code": 0,
        "ret_msg": "OK",
        "ext_code": "",
        "ext_info": "",
        "result": [
            {
                "symbol": "BTCUSD",
                "last_price": "34000",
                "price_24h_pcnt": "-0.5"
            },
            {
                "symbol": "ETHUSD",
                "last_price": "2200",
                "price_24h_pcnt": "-1.0"
            }
        ]
    }
    ```

### Command /max_prices
    ```
    Request:
    url = "https://api.bybit.com/v2/public/tickers"
    response = requests.get(url)
    data = response.json()

    Response:
    {
        "ret_code": 0,
        "ret_msg": "OK",
        "ext_code": "",
        "ext_info": "",
        "result": [
            {
                "symbol": "BTCUSD",
                "last_price": "35000",
                "price_24h_pcnt": "1.5"
            },
            {
                "symbol": "ETHUSD",
                "last_price": "2500",
                "price_24h_pcnt": "2.0"
            }
        ]
    }
    ```

### Command /best_crypto
    ```
    Request:
    url = "https://api.bybit.com/v2/public/tickers"
    response = requests.get(url)
    data = response.json()

    Response:
    {
        "ret_code": 0,
        "ret_msg": "OK",
        "ext_code": "",
        "ext_info": "",
        "result": [
            {
                "symbol": "BTCUSD",
                "last_price": "34000",
                "price_24h_pcnt": "2.0"
            },
            {
                "symbol": "ETHUSD",
                "last_price": "2200",
                "price_24h_pcnt": "1.5"
            }
        ]
    }
    ```

### Command /currency_rate
    ```
    Request:
    url = "https://api.exchangerate-api.com/v4/latest/USD"
    response = requests.get(url)
    data = response.json()

    Response:
    {
        "base": "USD",
        "date": "2023-07-01",
        "time_last_updated": 1596460802,
        "rates": {
            "EUR": 0.85,
            "GBP": 0.75,
            "JPY": 110.0
        }
    }
    ```

## Working with the Database
    ```
    For the /history command, the user's query history is saved.
    Each query is recorded in the database with the user's ID, command, and query time.
    ```


# Telegram Crypto Bot (RU)

Этот бот предоставляет информацию о криптовалютах и курсах валют. Он использует Bybit API для предоставления актуальной информации в реальном времени.


## Установка

1. Клонируйте репозиторий:
    ```
    git clone https://github.com/Sim0o0n/Crypto_bot
    ```
2. Установите зависимости:
    ```
    pip install -r requirements.txt
    ```
3. Настройте токен Telegram бота в файле `main.py`:
    ```python
    application = Application.builder().token("YOU_TOKEN").build()
    ```
4. Запустите бота:
    ```
    python main.py
    ```

## Команды и пример вывода данных

- `/start` - Запуск бота.
    ```
    Привет! Я бот для получения цен на криптовалюты. 
   Команды:
   /low_prices - Криптовалюты с минимальными ценами
   /max_prices - Криптовалюты с максимальными ценами
   /best_crypto - Лучшие криптовалюты за последние сутки
   /currency_rate - Курсы валют
   /history - История запросов пользователей
    ```
- `/low_prices` - Цены криптовалют с минимальной ценой.
    ```
    Криптовалюты с минимальными ценами:
   SPELLUSDT: 0.0005937 USD (0.105174%)
   1000BTTUSDT: 0.0007617 USD (0.061306%)
   DENTUSDT: 0.0008250 USD (0.057285%)
   ZBCNUSDT: 0.000980 USD (0.054897%)
   10000LADYSUSDT: 0.0010252 USD (0.090406%)
   REEFUSDT: 0.001204 USD (0.082733%)
   1000000BABYDOGEUSDT: 0.0012184 USD (0.132973%)
   10000SATSUSDT: 0.001229 USD (0.024166%)
   XCNUSDT: 0.0013532 USD (0.073116%)
   MOBILEUSDT: 0.001391 USD (0.04351%)
   HOTUSDT: 0.001496 USD (0.111441%)
   ZKFUSDT: 0.001669 USD (0.088005%)
   LEVERUSDT: 0.002045 USD (0.052496%)
   VTHOUSDT: 0.002141 USD (0.085149%)
   MBLUSDT: 0.002149 USD (0.04727%)
   1CATUSDT: 0.002163 USD (0.060814%)
   SLPUSDT: 0.002393 USD (0.136277%)
   10000000AIDOGEUSDT: 0.002555 USD (0.122583%)
   MYRIAUSDT: 0.003037 USD (0.098372%)
   FUNUSDT: 0.003176 USD (0.094417%)
   VRAUSDT: 0.003186 USD (0.112041%)
   MEWUSDT: 0.003506 USD (0.092892%)
   XVGUSDT: 0.0036420 USD (0.136526%)
   FITFIUSDT: 0.003836 USD (0.068523%)
   SCUSDT: 0.003965 USD (0.077445%)
   10000NFTUSDT: 0.004302 USD (0.029432%)
   RSRUSDT: 0.004304 USD (0.093495%)
   LINAUSDT: 0.004826 USD (0.064872%)
   STMXUSDT: 0.004920 USD (0.286274%)
   KEYUSDT: 0.0049795 USD (0.100685%)
    ```
- `/max_prices` - Цены криптовалют с максимальной ценой.
    ```
    Криптовалюты с максимальными ценами:
   BTCUSDZ24: 59464.00 USD (0.04352%)
   BTCUSDU24: 57890.00 USD (0.04249%)
   BTCUSD: 56742.00 USD (0.041309%)
   BTCUSDT: 56739.10 USD (0.041309%)
   YFIUSDT: 6183 USD (0.135328%)
   ETHUSDZ24: 3152.55 USD (0.044011%)
   ETHUSDU24: 3067.45 USD (0.043137%)
   ETHUSD: 3005.20 USD (0.043544%)
   ETHUSDT: 3003.74 USD (0.042082%)
   PAXGUSDT: 2348 USD (0.004706%)
   MKRUSDT: 2273.9 USD (0.123857%)
   BNBUSDT: 509.80 USD (0.086414%)
   BCHUSDT: 328.50 USD (0.095%)
   GNOUSDT: 242.94 USD (0.075526%)
   TAOUSDT: 223.80 USD (0.079438%)
   XMRUSDT: 155.98 USD (0.105927%)
   SOLUSDT: 139.910 USD (0.10978%)
   SOLUSD: 139.87 USD (0.109727%)
   AAVEUSDT: 80.98 USD (0.069466%)
   TRBUSDT: 80.910 USD (0.104422%)
   QNTUSDT: 74.20 USD (0.077705%)
   LTCUSDT: 62.66 USD (0.061134%)
   LTCUSD: 62.56 USD (0.05962%)
   ILVUSDT: 56.525 USD (0.079339%)
   COMPUSDT: 46.17 USD (0.070236%)
   METISUSDT: 37.05 USD (0.068955%)
   BSVUSDT: 35.96 USD (0.079879%)
   EGLDUSDT: 33.05 USD (0.17157%)
   SSVUSDT: 28.630 USD (0.011839%)
   ORDIUSDT: 28.300 USD (0.044357%)
    ```
- `/best_crypto` - Топ 5 криптовалют с наибольшим ростом за последние сутки.
    ```
    Топ 5 криптовалют с наибольшим ростом за последние сутки:
   10000COQUSDT: 0.01615 USD (0.36172%)
   ZROUSDT: 4.1419 USD (0.358356%)
   POPCATUSDT: 0.5121 USD (0.303053%)
   STMXUSDT: 0.004910 USD (0.282654%)
   UNFIUSDT: 4.7620 USD (0.272751%)
    ```
- `/currency_rate` - Курс валют.
    ```
    Курс доллара:
   USD/RUB: 88.43
   USD/USDT: 1
    ```
  - `/history` - История запросов.
      ```
      История запросов пользователей:
      Пользователь ID: 00000000000, Команда: currency_rate, Время: 2024-07-06 10:00:18

      ```

## Описание

Бот использует библиотеки для работы с различными API и запросами. Он поддерживает работу со множеством пользователей и хранит их поисковую историю в базе данных с использованием ORM Peewee.

## Ошибки

При вводе несуществующих команд или неверных данных, бот выводит соответствующее уведомление.

## Взаимодействие с API ByBit
## Команда /low_prices

    ```
    Запрос:
    url = "https://api.bybit.com/v2/public/tickers"
    response = requests.get(url)
    data = response.json()

    Ответ:
        {
        "ret_code": 0,
        "ret_msg": "OK",
        "ext_code": "",
        "ext_info": "",
        "result": [
            {
                "symbol": "BTCUSD",
                "last_price": "34000",
                "price_24h_pcnt": "-0.5"
            },
            {
                "symbol": "ETHUSD",
                "last_price": "2200",
                "price_24h_pcnt": "-1.0"
            }
        ]
    }


   ## Команда /max_prices
    ```
    Запрос:
    url = "https://api.bybit.com/v2/public/tickers"
    response = requests.get(url)
    data = response.json()
    
    Ответ:
    {
        "ret_code": 0,
        "ret_msg": "OK",
        "ext_code": "",
        "ext_info": "",
        "result": [
            {
                "symbol": "BTCUSD",
                "last_price": "35000",
                "price_24h_pcnt": "1.5"
            },
            {
                "symbol": "ETHUSD",
                "last_price": "2500",
                "price_24h_pcnt": "2.0"
            }
        ]
    }
    ```
## Команда /best_crypto

    ```
        Запрос:
        url = "https://api.bybit.com/v2/public/tickers"
        response = requests.get(url)
        data = response.json()
    
        Ответ:
        {
        "ret_code": 0,
        "ret_msg": "OK",
        "ext_code": "",
        "ext_info": "",
        "result": [
            {
                "symbol": "BTCUSD",
                "last_price": "34000",
                "price_24h_pcnt": "2.0"
            },
            {
                "symbol": "ETHUSD",
                "last_price": "2200",
                "price_24h_pcnt": "1.5"
            }
        ]
    }

    ```
## Команда /currency_rate

    ```
        Запрос:
        url = "https://api.exchangerate-api.com/v4/latest/USD"
        response = requests.get(url)
        data = response.json()
    
        Ответ:
        {
        "base": "USD",
        "date": "2023-07-01",
        "time_last_updated": 1596460802,
        "rates": {
            "EUR": 0.85,
            "GBP": 0.75,
            "JPY": 110.0
        }
    }

    ```

## Работа с базой данных
    ```
    Для команды /history сохраняется история запросов пользователей. 
    Каждый запрос записывается в базу данных с указанием ID пользователя, команды и времени запроса.

    ```