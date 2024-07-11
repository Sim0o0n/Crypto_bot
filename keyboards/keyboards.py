from telegram import KeyboardButton, ReplyKeyboardMarkup


def get_keyboard():
    keyboard = [
        [KeyboardButton("/low_prices")],
        [KeyboardButton("/max_prices")],
        [KeyboardButton("/best_crypto")],
        [KeyboardButton("/currency_rate")],
    ]
    return ReplyKeyboardMarkup(keyboard, resize_keyboard=True)



