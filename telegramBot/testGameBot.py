import telebot
from telebot import types
from time import sleep

bot = telebot.TeleBot('6189669484:AAHjBHycz0bq1s5tvBLC5ky17Iff2Wrk_8U')
STAGE = ''


@bot.message_handler(commands=['start'])
def start(message):
    global STAGE
    STAGE = 'prolog'
    prolog(message)


@bot.message_handler(commands=['info'])
def info(message):
    bot.send_message(message.chat.id, message)


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
    global STAGE
    if STAGE == 'prolog':
        if message.text in ['Кто вы?', 'Что происходит?', 'Где вы?']:
            answer_prolog_1(message)
            sleep(1)
            bot.send_message(message.chat.id, 'Расскажу всё на месте, прошу вас, нет времени объяснять')
            answer_prolog_2(message)
        elif message.text == 'Может вызвать полицию?':
            answer_prolog_1(message)
            sleep(1)
            bot.reply_to(message, 'Уже вызвал, нет времени ждать')
            answer_prolog_2(message)
        elif message.text == 'Я на месте':
            answer_prolog_3(message)



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
    sleep(2)
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    markup.add(types.KeyboardButton('Я на месте'))
    bot.send_location(message.chat.id, 60.058286, 30.440842, reply_markup=markup)


def answer_prolog_3(message):
    sleep(3)
    user_id = message.from_user.id
    user_first_name = message.from_user.first_name
    user_last_name = message.from_user.last_name
    mess = f'<em>Пользователь <code>Professor</code> добавил пользователя ' \
           f'<code>{user_id}</code> в квартиру 457 как <u>guest</u></em>'
    bot.send_message(message.chat.id, mess, parse_mode='html')
    sleep(2)
    bot.send_message(message.chat.id, 'Я добавил ваш id в список гостей моего дома.')
    sleep(3)
    bot.send_message(message.chat.id, 'Вы сможете открывать им некоторые двери в моей квартире, '
                                      'но, к сожалению, вы не сможете более отправлять мне сообщения.')
    sleep(2)
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    markup.add(types.KeyboardButton('Открыть входную дверь'))
    bot.send_message(message.chat.id, 'Попробуйте открыть входную дверь.', reply_markup=markup)


bot.polling(none_stop=True)
