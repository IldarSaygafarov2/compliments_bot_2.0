import time
from data.loader import bot
from data import config
import random
from helpers.utils import read_json, read_file
from telebot.apihelper import ApiTelegramException
import threading
import schedule


@bot.message_handler(commands=['start'])
def start(message):
    chat_id = message.chat.id

    bot.send_message(
        chat_id,
        """
Привет, я не вижу тебя, я просто бот, но я уверен что смотря на тебя люди улыбаются твоей энерегетике.
Жмякни на команду /compliment
Надеюсь что смог поднять тебе настроение☻☻
""",
        parse_mode="HTML",
    )


@bot.message_handler(commands=['compliment'])
def get_compliment(message):
    chat_id = message.chat.id
    compliments = read_json("compliments.json")
    compliment = random.choice(compliments)[0].replace("\n ", "\n")
    bot.send_message(chat_id, compliment)


@bot.message_handler(commands=['special'])
def get_special(message):
    chat_id = message.chat.id
    if chat_id != 1080936152 or chat_id != 5090318438:
        bot.send_message(chat_id, 'Прости, но эти сообщения может получить только один человек!')
        return

    compliments = read_file("my_compliments.txt")
    compliment = random.choice(compliments)
    bot.send_message(config.MAIN_USER_ID, 'это сообщение для тебя малыш!')
    bot.send_message(config.MAIN_USER_ID, compliment)


def send_compliment_by_me():
    my_compliments = read_file("my_compliments.txt")
    compliment = random.choice(my_compliments)
    chat_id = config.MAIN_USER_ID
    # config.MAIN_USER_ID
    # for chat_id in [config.MAIN_USER_ID, 5090318438]:
    try:
        bot.send_message(chat_id, "А это для моей девочки♥")
        bot.send_message(chat_id, compliment)
    except ApiTelegramException as e:
        if e.description == 'Forbidden: bot was blocked by the user':
            print('bot was blocked by', chat_id)
    print('отправлено')
