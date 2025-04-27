import os
from telegram.ext import Updater, CommandHandler

def start(update, context):
    update.message.reply_text('Olá! Eu sou o seu bot.')

def main():
    updater = Updater(os.environ[\"BOT_TOKEN\"], use_context=True)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", start))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()