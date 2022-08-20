from telegram.ext import Updater, CommandHandler

def main():
    TOKEN = "5578582382:AAEwTFDUjaV2Rk1i9PVqJq-KE6WrSoAGAnM"
    updater = Updater(token=TOKEN, use_context=True)
    dispatcher = updater.dispatcher

    weather_handler = CommandHandler("weather", weather)
    currency_handler = CommandHandler("currency", currency)
    start_handler = CommandHandler("start", start)

    dispatcher.add_handler(weather_handler)
    dispatcher.add_handler(currency_handler)
    dispatcher.add_handler(start_handler)

    updater.start_polling()

if __name__ == '__main__':
    main()