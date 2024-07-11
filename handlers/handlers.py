from telegram import Update
from telegram.ext import CallbackContext
from keyboards.keyboards import get_keyboard
from utils.utils import get_low_price_cryptos, get_max_price_cryptos, get_best_crypto, get_currency_rate
from database.db import log_user_request, get_user_requests


async def start(update: Update, context: CallbackContext) -> None:
    keyboard = get_keyboard()
    await update.message.reply_text(
        'Привет! Я бот для получения цен на криптовалюты. '
        '\nКоманды:'
        '\n/low_prices - Криптовалюты с минимальными ценами'
        '\n/max_prices - Криптовалюты с максимальными ценами'
        '\n/best_crypto - Лучшие криптовалюты за последние сутки'
        '\n/currency_rate - Курсы валют',
        reply_markup=keyboard
    )


async def low_prices(update: Update, context: CallbackContext) -> None:
    prices = get_low_price_cryptos()
    await update.message.reply_text(prices)
    log_user_request(update.message.from_user.id, "low_prices")


async def max_prices(update: Update, context: CallbackContext) -> None:
    prices = get_max_price_cryptos()
    await update.message.reply_text(prices)
    log_user_request(update.message.from_user.id, "max_prices")


async def best_crypto(update: Update, context: CallbackContext) -> None:
    cryptos = get_best_crypto()
    await update.message.reply_text(cryptos)
    log_user_request(update.message.from_user.id, "best_crypto")


async def currency_rate(update: Update, context: CallbackContext) -> None:
    rates = get_currency_rate()
    await update.message.reply_text(rates)
    log_user_request(update.message.from_user.id, "currency_rate")


async def history(update: Update, context: CallbackContext) -> None:
    requests = get_user_requests()
    message = "История запросов пользователей:\n"
    for req in requests:
        message += f"Пользователь ID: {req.user_id}, Команда: {req.command}, Время: {req.timestamp}\n"
    await update.message.reply_text(message)


async def unknown(update: Update, context: CallbackContext) -> None:
    await update.message.reply_text("Извините, я не понимаю эту команду.")
