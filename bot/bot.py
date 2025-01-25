import telebot
from decouple import config


TELEGRAM_BOT_TOKEN = config('TELEGRAM_BOT_TOKEN', cast=str)
bot = telebot.TeleBot(TELEGRAM_BOT_TOKEN)


@bot.message_handler(commands=['start'])
def send_welcome(message: telebot.types.Message) -> None:
    bot.send_message(message.chat.id, 'Привет! Меня зовут Чекер. \nОтправь мне IMEI для проверки.')


def run() -> None:
    bot.infinity_polling()
