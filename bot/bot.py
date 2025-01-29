import json
import telebot

from decouple import config

from utils import (
    is_user_allowed,
    is_imei_valid,
)

from reqs import (
    create_user,
    current_user,
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
    user = current_user(uid=message.from_user.id)

    if 'error' not in user:
        bot.send_message(
            message.chat.id,
            "👋 Привет! Рад тебя снова видеть.\n\n"
            "✅ Твой аккаунт уже создан, так что можешь сразу отправить мне IMEI, и я проверю его для тебя. 🔍"
        )
    else:
        user = create_user(uid=message.from_user.id)

        bot.send_message(
            message.chat.id,
            "🚀 Приветствую! Меня зовут <b>Чекер</b> — твой помощник по проверке IMEI.\n\n"
            "✅ Твой аккаунт успешно зарегистрирован в системе. Теперь можешь использовать все функции бота!",
            parse_mode="HTML"
        )

        bot.send_message(
            message.chat.id,
            "🔹 Просто отправь мне <b>IMEI</b>, и я проверю его для тебя. \n"
            "📌 Если у тебя есть вопросы — используй команду <code>/help</code>.",
            parse_mode="HTML"
        )


@bot.message_handler(commands=['services'])
@access_required
def send_service_list(message: telebot.types.Message) -> None:  
    response = get_service_list(
        uid=message.from_user.id
    )

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


@bot.message_handler(commands=['help'])
@access_required
def send_help(message: telebot.types.Message) -> None:
    help_text = (
        "🤖 <b>Чекер - бот для проверки IMEI</b>\n\n"
        "📌 <b>Как использовать:</b>\n"
        "— Просто отправь мне IMEI, и я предоставлю информацию о нем. 🔍\n"
        "— Если IMEI некорректный, я сообщу об этом. ❌\n\n"
        "🛠 <b>Доступные команды:</b>\n"
        "🔹 <code>/start</code> — Начать работу с ботом\n"
        "🔹 <code>/help</code> — Получить справку\n"
        "🔹 <code>/services</code> — Список доступных сервисов (если включено)\n\n"
        "📞 <b>Поддержка:</b>\n"
        "Если у вас возникли вопросы, обратитесь к администратору. 📩"
    )

    bot.send_message(message.chat.id, help_text, parse_mode="HTML")


@bot.message_handler()
@access_required
def send_info_by_imei(message: telebot.types.Message) -> None:
    imei = message.text.strip()
    
    if not is_imei_valid(imei):
        bot.send_message(message.chat.id, "❌ Некорректный IMEI. Проверьте правильность ввода.")
        return

    response = create_imei_check(imei=imei, uid=message.from_user.id)

    if 'error' in response:
        bot.send_message(
            message.chat.id,
            f"⚠️ Возникла ошибка:\n<b>{response.get('error', 'Неизвестная ошибка')}</b>\n"
            f"{response.get('details', '')}",
            parse_mode="HTML"
        )
        return

    service_title = response.get("service", {}).get("title", "Неизвестный сервис")
    status = response.get("status", "unknown")
    properties = response.get("properties", {})

    status_emoji = {
        "successful": "✅",
        "unsuccessful": "❌",
        "failed": "⚠️"
    }.get(status, "❔")

    text = (
        f"<b>📌 Информация по IMEI {imei}:</b>\n\n"
        f"🔹 <b>Сервис:</b> {service_title}\n"
        f"🔹 <b>Статус:</b> {status_emoji} {status.capitalize()}\n"
    )

    if properties:
        text += "\n<b>📍 Детали устройства:</b>\n"
        for key, value in properties.items():
            formatted_key = key.replace("_", " ").title()
            text += f"🔸 <b>{formatted_key}:</b> {value}\n"

    bot.send_message(
        message.chat.id,
        text,
        parse_mode="HTML"
    )


def run() -> None:
    bot.infinity_polling()

run()