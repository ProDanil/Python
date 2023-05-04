import telebot
from telebot import types

bot = telebot.TeleBot('6189669484:AAHjBHycz0bq1s5tvBLC5ky17Iff2Wrk_8U')


@bot.message_handler(commands=['start', 'info', 'website'])
def get_command(message):
    # bot.send_message(message.chat.id, message)
    if message.text == '/start':
        mess = f'Привет, <b>{message.from_user.first_name} <u>{message.from_user.last_name}</u></b>'
        bot.send_message(message.chat.id, mess, parse_mode='html')
    elif message.text == '/info':
        bot.send_message(message.chat.id, message)
    elif message.text == '/website':
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton('Посетить веб сайт', url='https://vk.com/dantchik'))
        bot.send_message(message.chat.id, 'Посетите мою страницу ВК', reply_markup=markup)


@bot.message_handler(content_types=['text'])
def get_text_message(message):
    if message.text == 'Привет':
        bot.send_message(message.chat.id, 'И тебе привет!')
    elif message.text == 'id':
        bot.send_message(message.chat.id, f'Твой ID: {message.from_user.id}')
    elif message.text == 'location':
        bot.send_location(message.chat.id, 60.058286, 30.440842)
    elif message.text == 'мем':
        mem = open('mem.png', 'rb')
        bot.send_photo(message.chat.id, mem)
    elif message.text == 'выбор':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
        website = types.KeyboardButton('Веб сайт')
        start = types.KeyboardButton('Start')
        markup.add(website, start)
        bot.send_message(message.chat.id, 'Выбор за вами', reply_markup=markup)
    else:
        bot.send_message(message.chat.id, 'Я тебя не понимаю')


bot.polling(none_stop=True)
