import telebot
from telebot import types
from time import sleep

bot = telebot.TeleBot('6189669484:AAHjBHycz0bq1s5tvBLC5ky17Iff2Wrk_8U')


@bot.message_handler(commands=['start'])
def start(message):
    prolog(message)


def prolog(message):
    sleep(2)
    bot.send_message(message.chat.id, 'Прошу вас, помогите!')
    sleep(1)
    bot.send_message(message.chat.id, 'Кто нибудь! На помощь!')
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    buttons = (types.KeyboardButton('Кто вы?'),
               types.KeyboardButton('Что происходит?'),
               types.KeyboardButton('Где вы?'),
               types.KeyboardButton('Может вызвать полицию?'))
    markup.add(*buttons)
    sleep(1)
    bot.send_message(message.chat.id, 'ПОМОГИТЕ!', reply_markup=markup)


@bot.message_handler(content_types=['text'])
def get_text(message):
    if message.text in ['Кто вы?', 'Что происходит?', 'Где вы?']:
        answer_prolog_1(message)
        sleep(1)
        bot.send_message(message.chat.id, 'Расскажу всё на месте, прошу вас, нет времени объяснять')
    elif message.text == 'Может вызвать полицию?':
        answer_prolog_1(message)
        sleep(1)
        bot.reply_to(message.chat.id, 'Уже вызвал, нет времени ждать')


def answer_prolog_1(message):
    sleep(3)
    bot.send_message(message.chat.id, 'Слава богу!')
    sleep(2)
    bot.send_message(message.chat.id, 'Я выслал это сообщение всем в радиусе 500 м')
    sleep(1)
    bot.send_message(message.chat.id, 'не думал, что кто-то получит.')


def answer_prolog_2(message):
    sleep(3)
    bot.send_message(message.chat.id, 'Я застрял в своей квартире')
    sleep(2)
    bot.send_message(message.chat.id, 'Еле достал телефон, чтобы вызвать помощь')
    sleep(2)
    bot.send_message(message.chat.id, ' прошу скорее, не могу дышать')
    sleep(1)
    bot.send_location(message.chat.id, 60.058286, 30.440842)


bot.polling(none_stop=True)
