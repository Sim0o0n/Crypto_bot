from telegram.ext import Application, CommandHandler, MessageHandler, filters
from loader import load_config, initialize
from handlers.handlers import start, low_prices, max_prices, best_crypto, currency_rate, history, unknown


def main():
    config = load_config()
    initialize()

    application = Application.builder().token(config["bot_token"]).build()

    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("low_prices", low_prices))
    application.add_handler(CommandHandler("max_prices", max_prices))
    application.add_handler(CommandHandler("best_crypto", best_crypto))
    application.add_handler(CommandHandler("currency_rate", currency_rate))
    application.add_handler(CommandHandler("history", history))

    application.add_handler(MessageHandler(filters.COMMAND, unknown))

    application.run_polling()


if __name__ == '__main__':
    main()

