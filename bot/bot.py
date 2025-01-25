import telebot

from decouple import config

from utils import (
    is_user_allowed,
    is_imei_valid,
    get_imei_info_from_api,
)


TELEGRAM_BOT_TOKEN = config('TELEGRAM_BOT_TOKEN', cast=str)
bot = telebot.TeleBot(TELEGRAM_BOT_TOKEN)


@bot.message_handler(commands=['start'])
def send_welcome(message: telebot.types.Message) -> None:
    uid = message.from_user.id
    if not is_user_allowed(uid):
        bot.send_message(message.chat.id, 'У Вас нет доступа к фунционалу этого бота.')
        return 
    
    bot.send_message(message.chat.id, 'Привет! Меня зовут Чекер. \nОтправь мне IMEI для проверки.')


@bot.message_handler()
def check_imei(message: telebot.types.Message) -> None:
    uid = message.from_user.id
    if not is_user_allowed(uid):
        bot.send_message(message.chat.id, 'У Вас нет доступа к фунционалу этого бота.')
        return

    imei = message.text
    if not is_imei_valid(imei):
        bot.send_message(message.chat.id, 'Некорректный IMEI. Проверьте правильность ввода.')
        return

    info = get_imei_info_from_api(imei)
    if 'error' in info:
        bot.send_message(message.chat.id, f'Возникла ошибка: \n{info['error']}')
        return

    bot.send_message(message.chat.id, f'Вот информация по Вашему запросу: \n{info}')


def run() -> None:
    bot.infinity_polling()
