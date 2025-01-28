import json
import telebot

from decouple import config

from utils import (
    is_user_allowed,
    is_imei_valid,
)

from reqs import (
    get_service_list,
    create_imei_check,
)


TELEGRAM_BOT_TOKEN = config('TELEGRAM_BOT_TOKEN', cast=str)
bot = telebot.TeleBot(TELEGRAM_BOT_TOKEN)


def access_required(handler):
    def wrapper(message: telebot.types.Message, *args, **kwargs):
        if not is_user_allowed(message.from_user.id):
            bot.send_message(
                chat_id=message.chat.id,
                text='У Вас нет доступа к функционалу этого бота.'
            )
            return
        return handler(message, *args, **kwargs)
    return wrapper


@bot.message_handler(commands=['start'])
@access_required
def send_welcome(message: telebot.types.Message) -> None:
    bot.send_message(
        message.chat.id,
        'Привет! Меня зовут Чекер. \nОтправь мне IMEI для проверки.'
    )


@bot.message_handler(commands=['services'])
@access_required
def send_service_list(message: telebot.types.Message) -> None:  
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
@access_required
def send_info_by_imei(message: telebot.types.Message) -> None:
    imei = message.text
    if not is_imei_valid(imei):
        bot.send_message(message.chat.id, 'Некорректный IMEI. Проверьте правильность ввода.')
        return

    response = create_imei_check(imei)
    if 'error' in response:
        bot.send_message(
            message.chat.id,
            f'Возникла ошибка: \n{response['error']}\n{response['details']}'
        )
        return

    bot.send_message(
        message.chat.id,
        f'Вот информация по Вашему запросу: \n{response}'
    )


def run() -> None:
    bot.infinity_polling()

run()