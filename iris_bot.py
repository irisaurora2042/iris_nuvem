from telegram.ext import Updater, CommandHandler

def start(update, context):
    update.message.reply_text('Olá! Eu sou o seu bot.')

def main():
    updater = Updater("7525887930:AAFT3FhRKBSf7VOL8szAyOY0-bMjiYtpq24", use_context=True)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", start))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()