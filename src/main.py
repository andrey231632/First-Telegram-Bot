from telegram.ext import *
from src import config
from src.bot_control import BControl


def bot_start():

    bc = BControl()

    token = config.TOKEN
    updater = Updater(token, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", bc.start))
    dp.add_handler(CommandHandler("help", bc.help))
    dp.add_handler(MessageHandler(Filters.text, bc.handle_message))
    dp.add_handler(MessageHandler(Filters.photo, bc.handle_photo))

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    bot_start()
