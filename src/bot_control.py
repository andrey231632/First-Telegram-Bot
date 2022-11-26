from telegram.ext import *
from src.ml_data import MLData


class BControl:

    def __init__(self):
        self.ml = MLData()

    def start(self, update, context: CallbackContext):
        update.message.reply_text("Welcome and send picture !)")

    def help(self, update, context: CallbackContext):
        update.message.reply_text("""/start - Starts conversation  
/help - Shows this message""")

    def handle_message(self, update, context: CallbackContext):
        update.message.reply_text('Please train model and send picture.')

    def handle_photo(self, update, context: CallbackContext):
        update.message.reply_text(f"In this image i see a {self.ml.h_photo(update=update, context=context)}")
