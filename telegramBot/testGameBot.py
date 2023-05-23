import telebot
from telebot import types
from time import sleep

bot = telebot.TeleBot('6189669484:AAHjBHycz0bq1s5tvBLC5ky17Iff2Wrk_8U')
STAGE = ''
SIDEBOARD_PIN = '534281'                                                    # Пароль от серванта в гостинной
NIGHTSTAND_PIN = '21343'                                                    # Пароль от тумбочки в спальне
BATHROOM_PIN = '12345'                                                      # Пароль от шкафа под ванной

'''
HTML
<i>, <em> - курсив
<b> - полужирный
<u> - подчеркнутый
<s> - зачеркнутый
<code> - вставка кода
'''


def bot_print(message, text, html=False):
    if html:
        bot.send_message(message.chat.id, text, parse_mode='html')
    else:
        bot.send_message(message.chat.id, text)


def status_print(message, color, text):
    mess = ''
    if color == 'red':
        mess = '🔴 <b>Доступ запрещён</b> 🔴\n\n'
    elif color == 'yellow':
        mess = '🟠 <b>Ошибка открытия</b> 🟠\n\n'
    elif color == 'green':
        mess = '🟢 <b>Доступ разрешён</b> 🟢\n\n'
    mess += text
    bot_print(message, mess, html=True)


@bot.message_handler(commands=['start'])
def start(message):
    global STAGE
    STAGE = 'prolog'
    prolog(message)


@bot.message_handler(commands=['info'])
def info(message):
    bot_print(message, message)


@bot.message_handler(commands=['help'])
def help_user(message):
    mess = f'<code>Для активации панели управления дверьми комнаты введите команду начиная с символа /.\n' \
           f'Пример: /hallway</code>'
    bot_print(message, mess, html=True)
    mess = f'<code>Для открытия двери нажмите на плитку с названием или напишите название самостоятельно.\n' \
           f'Пример: Гостинная</code>'
    bot_print(message, mess, html=True)
    mess = f'<code>Все двери открываются автоматически по команде, либо в ручном режиме.\n' \
           f'Дополнительную информацию ищите в инструкции к дверям.</code>'
    bot_print(message, mess, html=True)
    mess = f'<code>Двери имеют 3 уровня доступа:\n' \
           f'</code>🔴<code> - доступ запрещён, дверь невозможно открыть автоматически с Вашими правами.\n' \
           f'</code>🟠<code> - ошибка открытия, дверь открывается с помощью пин-кода, либо дверь неисправна.\n' \
           f'</code>🟢<code> - доступ разрешён, дверь будет разблокирована автоматически</code>'
    bot_print(message, mess, html=True)


@bot.message_handler(commands=['hallway'])
def hallway(message):
    global STAGE
    STAGE = 'hallway'
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = (types.KeyboardButton('Туалет'),
               types.KeyboardButton('Ванная'),
               types.KeyboardButton('Спальня'),
               types.KeyboardButton('Гостинная'),
               types.KeyboardButton('Гардероб'))
    markup.add(*buttons)
    sleep(1)
    bot.send_message(message.chat.id, '<code>HALLWAY статус: </code><u>Активен</u>\n\n'
                                      '<code>Выберите дверь</code>',
                     reply_markup=markup, parse_mode='html')


@bot.message_handler(commands=['living_closets'])
def living_closets(message):
    global STAGE
    STAGE = 'living_closets'
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = (types.KeyboardButton('Холодильник'),
               types.KeyboardButton('Сервант'),
               types.KeyboardButton('Балкон'))
    markup.add(*buttons)
    sleep(1)
    bot.send_message(message.chat.id, '<code>LIVING_CLOSETS статус: </code><u>Активен</u>\n\n'
                                      '<code>Выберите, что следует открыть</code>',
                     reply_markup=markup, parse_mode='html')


# Изменить название команды
@bot.message_handler(commands=['bedroom'])
def bedroom(message):
    global STAGE
    STAGE = 'bedroom'
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = (types.KeyboardButton('Шкаф'),
               types.KeyboardButton('Тумбочка'))
    markup.add(*buttons)
    sleep(1)
    bot.send_message(message.chat.id, '<code>BEDROOM статус: </code><u>Активен</u>\n\n'
                                      '<code>Выберите, что следует открыть</code>',
                     reply_markup=markup, parse_mode='html')


# Изменить название команды
@bot.message_handler(commands=['bathroom'])
def bathroom(message):
    global STAGE
    STAGE = 'bathroom'
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = (types.KeyboardButton('Полка'),
               types.KeyboardButton('Шкаф под ванной'))
    markup.add(*buttons)
    sleep(1)
    bot.send_message(message.chat.id, '<code>BATHROOM статус: </code><u>Активен</u>\n\n'
                                      '<code>Выберите, что следует открыть</code>',
                     reply_markup=markup, parse_mode='html')


@bot.message_handler(content_types=['text'])
def get_text(message):
    global STAGE
    if   STAGE == 'prolog':
        if message.text in ['Кто вы?', 'Что происходит?', 'Где вы?']:
            answer_prolog_1(message)
            sleep(1)
            bot_print(message, 'Расскажу всё на месте, прошу вас, нет времени объяснять')
            answer_prolog_2(message)
        elif message.text == 'Может вызвать полицию?':
            answer_prolog_1(message)
            sleep(1)
            bot.reply_to(message, 'Уже вызвал, нет времени ждать')
            answer_prolog_2(message)
        elif message.text == 'Я на месте':
            answer_prolog_3(message)
        elif message.text == 'Открыть входную дверь':
            answer_prolog_4(message)
    elif STAGE == 'hallway':
        if message.text in ['Туалет', 'Гостинная']:
            mess = '<code>Дверь открыта</code>'
            status_print(message, 'green', mess)
        elif message.text in ['Ванная', 'Гардероб']:
            mess = '<code>У вас нет прав доступа к этой двери</code>'
            status_print(message, 'red', mess)
        elif message.text == 'Спальня':
            mess = '<code>Возможно, что-то блокирует дверь, воспользуйтесь ручным управлением</code>'
            status_print(message, 'yellow', mess)
    elif STAGE == 'living_closets':
        if message.text == 'Холодильник':
            mess = '<code>Дверь открыта</code>'
            status_print(message, 'green', mess)
        elif message.text == 'Балкон':
            mess = '<code>У вас нет прав доступа к этой двери</code>'
            status_print(message, 'red', mess)
        elif message.text == 'Сервант':
            mess = '<code>Введите пин-код:</code>'
            STAGE = 'sideboard_pin_enter'
            status_print(message, 'yellow', mess)
    elif STAGE == 'bedroom':
        if message.text == 'Шкаф':
            mess = '<code>Дверь открыта</code>'
            status_print(message, 'green', mess)
        elif message.text == 'Тумбочка':
            mess = '<code>Введите пин-код:</code>'
            STAGE = 'nightstand_pin_enter'
            status_print(message, 'yellow', mess)
    elif STAGE == 'bathroom':
        if message.text == 'Полка':
            mess = '<code>Дверь открыта</code>'
            status_print(message, 'green', mess)
        elif message.text == 'Шкаф под ванной':
            mess = '<code>Введите пин-код:</code>'
            STAGE = 'bathroom_pin_enter'
            status_print(message, 'yellow', mess)
    elif STAGE == 'sideboard_pin_enter':
        if message.text == SIDEBOARD_PIN:
            mess = '<code>Дверь открыта</code>'
            status_print(message, 'green', mess)
        else:
            mess = '<code>Неверный пароль</code>'
            status_print(message, 'red', mess)
        living_closets(message)
    elif STAGE == 'nightstand_pin_enter':
        if message.text == NIGHTSTAND_PIN:
            mess = '<code>Дверь открыта</code>'
            status_print(message, 'green', mess)
        else:
            mess = '<code>Неверный пароль</code>'
            status_print(message, 'red', mess)
        bedroom(message)
    elif STAGE == 'bathroom_pin_enter':
        if message.text == BATHROOM_PIN:
            mess = '<code>Дверь открыта</code>'
            status_print(message, 'green', mess)
        else:
            mess = '<code>Неверный пароль</code>'
            status_print(message, 'red', mess)
        bathroom(message)


def prolog(message):
    sleep(2)
    bot_print(message, 'Прошу вас, помогите!')
    sleep(1)
    bot_print(message, 'Кто нибудь! На помощь!')
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    buttons = (types.KeyboardButton('Кто вы?'),
               types.KeyboardButton('Что происходит?'),
               types.KeyboardButton('Где вы?'),
               types.KeyboardButton('Может вызвать полицию?'))
    markup.add(*buttons)
    sleep(1)
    bot.send_message(message.chat.id, 'ПОМОГИТЕ!', reply_markup=markup)


def answer_prolog_1(message):
    sleep(3)
    bot_print(message, 'Слава богу!')
    sleep(2)
    bot_print(message, 'Я выслал это сообщение всем в радиусе 500 м')
    sleep(1)
    bot_print(message, 'не думал, что кто-то получит.')


def answer_prolog_2(message):
    sleep(3)
    bot_print(message, 'Я застрял в своей квартире')
    sleep(2)
    bot_print(message, 'Еле достал телефон, чтобы вызвать помощь')
    sleep(2)
    bot_print(message, ' прошу скорее, не могу дышать')
    sleep(2)
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    markup.add(types.KeyboardButton('Я на месте'))
    bot.send_location(message.chat.id, 60.058286, 30.440842, reply_markup=markup)


def answer_prolog_3(message):
    sleep(3)
    user_id = message.from_user.id
    mess = f'<u><i><code>Пользователь </code>Professor<code> добавил пользователя </code>' \
           f'{user_id}<code> в квартиру </code>457<code> как </code>guest</i></u>'
    bot_print(message, mess, html=True)
    sleep(2)
    bot_print(message, 'Я добавил ваш id в список гостей моего дома.')
    sleep(3)
    bot_print(message, 'Теперь вы сможете открывать некоторые двери в моей квартире с помощью телефона, '
                       'но, к сожалению, не сможете более отправлять мне сообщения.')
    sleep(2)
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    markup.add(types.KeyboardButton('Открыть входную дверь'))
    bot.send_message(message.chat.id, 'Попробуйте открыть входную дверь.', reply_markup=markup)


def answer_prolog_4(message):
    sleep(3)
    user_id = message.from_user.id
    user_first_name = message.from_user.first_name
    user_last_name = message.from_user.last_name
    mess = f'<code>Здравствуйте, {user_first_name} {user_last_name}.\n' \
           f'Добро пожаловать в умный дом\n' \
           f'Ваш ID: {user_id}</code>'
    status_print(message, 'green', mess)
    sleep(3)
    bot_print(message, 'Из-за сбоя в системе дома не работает свет,'
                       ' собственно, по этой же причине я и застрял')
    sleep(2)
    bot_print(message, 'Связь периодически падает, поэтому не всегда мои сообщения будут приходить.')
    sleep(2)
    bot_print(message, 'Прошу вас, восстановите систему дома, чтобы я мог выйти.')
    sleep(3)
    mess = f'<code>Используйте комманду /hallway для активации панели управления дверьми прихожей.\n' \
           f'Используйте комманду /help для открытия справки</code>'
    bot_print(message, mess, html=True)


bot.polling(none_stop=True)
