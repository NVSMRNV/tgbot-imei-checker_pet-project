import json
import telebot
from prettytable import PrettyTable
from decouple import config

from utils import (
    beautify,
    is_user_allowed,
    is_imei_valid,
    get_imei_info_from_api,
    get_service_list,
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


@bot.message_handler(commands=['services'])
def send_service_list(message: telebot.types.Message) -> None:
    uid = message.from_user.id
    if not is_user_allowed(uid):
        bot.send_message(
            chat_id=message.chat.id,
            text='У Вас нет доступа к фунционалу этого бота.'
        )
        return 
    
    response = get_service_list()
    if 'error' in response:
        bot.send_message(
            message.chat.id,
            f'Возникла ошибка: \n{response['error']}\n{response['details']}'
        )
        return

    answer = ''
    for service in response:
        answer += f'*🛠️ ID:* `{service['id']}`\n'
        answer += f'*📌 Title:* `{service['title']}`\n'
        answer += f'*💰 Price:* `{service['price']}`\n'
        answer += '-------------------------\n'

    bot.send_message(
        message.chat.id,
        f'*Вот список доступных сервисов:*\n\n{answer}', parse_mode='Markdown'
    )


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

    response = get_imei_info_from_api(imei)
    if 'error' in response:
        details = json.loads(response['details'])
        bot.send_message(message.chat.id, f'Возникла ошибка: \n{response['error']}\n{details['message']}')
        return

    bot.send_message(message.chat.id, f'Вот информация по Вашему запросу: \n{response}')


def run() -> None:
    bot.infinity_polling()

run()