from tkinter.messagebox import showerror, showinfo
from tkinter import *
from tkinter import ttk
from random import shuffle


HEIGHT = 360
WIDTH = 350
PASSWORD = '12345'
STATE = 'user'  # user admin success
TABLE = []
OBJECTS = []
ENABLED = []
TEST_OBJ = []
WINDOWS = []

# кортежи и словари, содержащие настройки шрифтов и отступов
FONT = ('Arial', 15, 'bold')              # шрифт параметров
FONT_HEADER = ('Arial', 15, 'bold')       # шрифт заголовков
FONT_ENTRY = ('Arial', 12)                # шрифт панели ввода
LABEL_FONT = ('Arial', 11)                # шрифт кнопок
BASE_PADDING = {'padx': 10, 'pady': 8}
HEADER_PADDING = {'padx': 10, 'pady': 12}
POS = {"padx": 6, "pady": 6, "anchor": NW}

questions = ['Главный талант Никиты',
             'Настоящее имя Частного Детектива',
             'Что стало с пропавшими детьми?',
             'Почему пропал Никита?',
             'Если Никиту похитили, то зачем?',
             'Кто был тот мальчик на Научной Конференции 2010?',
             'В какой период произошёл сбой системы дома?',
             'Где профессор?',
             'Профессор виновен? Напишите вердикт.']
answers = [['Рисование', 'Наука', 'Спорт', 'Он был бездарным', 'свой ответ'],
           ['Моисеев Никита', 'Моисеев Пётр', 'Леонов Николай', 'Герасенко Евгений', 'свой ответ'],
           ['Убиты профессором', 'Неизвестно', 'Вернулись к родным', 'Их не существовало', 'свой ответ'],
           ['Его похитили', 'Его убили', 'Отец его продал', 'Он не пропадал', 'свой ответ'],
           ['Ради денег', 'Из-за мести', 'Ради забавы', 'Его не похищали'],
           ['свой ответ', 'Один из похищенных мальчиков', 'Никита Моисеев', 'Брат Никиты'],
           ['2010 - 2015 гг', '2022 - 2023 гг', '2016 - 2021 гг', '2005 - 2009 гг', 'свой ответ'],
           ['Где-то в доме', 'Уехал', 'Неизвестно', 'Поместил разум в компьютер', 'свой ответ']]
correct_answer = []
for i in range(len(answers)):
    correct_answer.append(answers[i][0])
CORRECT = []


class Window(Toplevel):
    def __init__(self, W, H, pos=None):
        super().__init__()

        # конфигурация окна
        self.iconphoto(False, icon)
        if pos:
            self.geometry(f'{W}x{H}{pos}')
        else:
            self.geometry(f'{W}x{H}')
        self.resizable(0, 0)
        self.attributes("-toolwindow", True)  # отключение верхней панели окна
        self.protocol("WM_DELETE_WINDOW", lambda: dismiss(self))  # перехватываем нажатие на крестик
        self.grab_set()

    def set_title(self, title):
        self.title(title)


def is_admin():
    return STATE == 'admin'


def destroy_object(table=True, obj=True, enabled=True, test_obj=True):
    global TABLE
    global OBJECTS
    global ENABLED
    global TEST_OBJ

    if obj:
        for ob in OBJECTS:
            ob.pack_forget()
        OBJECTS = []
    if table:
        for t in TABLE:
            t.grid_remove()
        TABLE = []
    if enabled:
        ENABLED = []
    if test_obj:
        for ob in TEST_OBJ:
            ob.pack_forget()
        TEST_OBJ = []


def power_on():
    pass


def menu():
    destroy_object()
    # btn_state.grid()
    # btn_settings.grid()
    btn_state.pack(fill=X, pady=50)
    btn_settings.pack(fill=X, pady=10)
    OBJECTS.extend([btn_state, btn_settings])


def state():
    destroy_object()
    root.title('Статус системы')
    if STATE == 'user' or is_admin():
        status, color = state_list[2]
    else:
        status, color = state_list[0]
    for c in range(2): root.columnconfigure(index=c)
    for r in range(len(param_list)): root.rowconfigure(index=r)
    for r in range(len(param_list)):
        label_param = Label(root, text=param_list[r],
                            font=FONT,
                            justify=LEFT)

        if color == 'green' and r > 5:
            status = sensors_list[r - 6]

        label_status = Label(root, text=status,
                             font=FONT,
                             justify=LEFT, fg=color)
        label_param.grid(row=r, column=0)
        label_status.grid(row=r, column=1)
        TABLE.extend([label_param, label_status])
    btn_back.grid(column=1, pady=10, padx=10)
    TABLE.append(btn_back)


def settings():
    destroy_object()
    if is_admin():
        command = power_on
        btn_reboot['state'] = ACTIVE
        btn_state = ACTIVE
        val = enabled_off
    elif STATE == 'success':
        command = power_on
        btn_reboot['state'] = DISABLED
        btn_state = DISABLED
        val = enabled_on
    else:
        command = open_error
        btn_reboot['state'] = DISABLED
        btn_state = ACTIVE
        val = enabled_off
    for r in range(len(param_list)):
        enabled = StringVar(value=val)
        setting_label = Label(root, text=param_list[r],
                              font=FONT,
                              justify=LEFT)

        enabled_checkbutton = Checkbutton(textvariable=enabled,
                                          variable=enabled,
                                          offvalue=enabled_off,
                                          onvalue=enabled_on,
                                          font=LABEL_FONT,
                                          state=btn_state,
                                          command=command)
        setting_label.grid(row=r, column=0)
        enabled_checkbutton.grid(row=r, column=1)
        ENABLED.append(enabled)
        TABLE.extend([setting_label, enabled_checkbutton])
    btn_reboot.grid(row=len(param_list), column=0, pady=10, padx=10)
    btn_back.grid(row=len(param_list), column=1, pady=10, padx=10)
    TABLE.extend([btn_back, btn_reboot])


# Функция закрытия window
def dismiss(window):
    window.grab_release()                                         # освобождаем пользовательский ввод
    window.destroy()


def check_pass(password, window):
    global STATE
    # проверка
    if password == PASSWORD:
        showinfo(title="Успех", message="Авторизация прошла успешно!")
        STATE = 'admin'
        dismiss(window)
        settings()
    else:
        showerror(title="Ошибка", message="Неверный пароль!")


def enter_pass():
    window = Window(WIDTH, HEIGHT // 2, pos='+300+300')
    window.set_title('авторизация')

    # заголовок
    main_label = Label(window, text='Авторизация', font=FONT_HEADER, justify=CENTER, **HEADER_PADDING)
    main_label.pack()

    # метка для поля ввода пароля
    password_label = Label(window, text='Пароль', font=LABEL_FONT, **BASE_PADDING)
    password_label.pack()

    # поле ввода пароля
    password_entry = Entry(window, bg='#fff', fg='#444', font=FONT_ENTRY)
    password_entry.pack()

    # кнопка отправки формы
    send_btn = Button(window, text='Войти', command=lambda: check_pass(password_entry.get(), window))
    send_btn.pack(**BASE_PADDING)


def open_error():
    showerror(title="Ошибка", message="У вас нет прав доступа", detail="Авторизируйтесь от имени администратора")
    for enab in ENABLED:
        enab.set(enabled_off)
    enter_pass()


def check_quest(wind, num, answer, entry):
    global CORRECT
    print(num + 1, answer, entry)
    if num != len(answers) and answer == correct_answer[num]:
        CORRECT.append(1)
    elif answer == 'свой ответ':
        CORRECT.append(entry)
    else:
        CORRECT.append(0)

    if num < len(questions) - 1:
        destroy_object(table=False, obj=False, enabled=False)
        question(wind, num + 2)
    else:
        result = list(filter(lambda x: type(x) == int, CORRECT))
        print(f'Всего вопросов: {len(questions)}')
        print(f'Оценивалось: {len(result)}')
        print(f'ИТОГ: {sum(result)}/{len(result)}')
        print(f'{round(sum(result) / len(result) * 100, 2)}%')
        showinfo(title="Успех", message="Перезагрузка завершена!")
        correct_sys()


def question(wind, num):
    num = num - 1
    quest = questions[num]
    q_label = Label(wind, text=f'{num + 1}. {quest}', font=FONT, **BASE_PADDING)
    q_label.pack(POS)
    TEST_OBJ.append(q_label)

    lang = StringVar()
    if num < len(answers):
        shuffle(answers[num])
        ans = answers[num]
        for a in ans:
            btn = Radiobutton(wind, text=a, font=LABEL_FONT, value=a, variable=lang)
            btn.pack(POS)
            TEST_OBJ.append(btn)
    else:
        lang = StringVar(value='свой ответ')

    entry = Entry(wind, bg='#fff', fg='#444', font=FONT_ENTRY)
    entry.pack(POS)
    TEST_OBJ.append(entry)

    send_btn = Button(wind, text='Далее', command=lambda: check_quest(wind, num, lang.get(), entry.get()))
    send_btn.pack(POS)
    TEST_OBJ.append(send_btn)


def test():
    window = Window(WIDTH * 2, HEIGHT, pos='+300+300')
    WINDOWS.append(window)
    window.set_title('Опрос')
    text = 'Для перезагрузки системы пройдите тест\n'
    main_label = Label(window, text=text, font='Arial 12 italic')
    main_label.pack()
    question(window, 1)


def reboot():
    window = Window(WIDTH, HEIGHT // 2, pos='+100+100')
    window.set_title('Перезагрузка')

    WINDOWS.append(window)

    # заголовок
    main_label = Label(window, text='Идёт перезагрузка системы', font=FONT_HEADER, justify=CENTER, **HEADER_PADDING)
    main_label.pack()

    # настройка processbar
    #value_var = IntVar()

    progressbar = ttk.Progressbar(window, orient="horizontal", mode='indeterminate')
    progressbar.pack(fill=X, padx=6, pady=6)

    # label = ttk.Label(window, textvariable=value_var)
    # label.pack(anchor=N, padx=6, pady=6)

    progressbar.start() # запускаем progressbar
    test()


def correct_sys():
    global STATE
    for window in WINDOWS:
        dismiss(window)
    STATE = 'success'
    settings()


def finish():
    root.destroy()  # ручное закрытие окна и всего приложения
    print("Закрытие приложения")


# pygame.init()

root = Tk()
root.title('Меню')
icon = PhotoImage(file='nastrojka.png')
root.iconphoto(False, icon)
root.geometry(f'{WIDTH}x{HEIGHT}')
root.resizable(0, 0)
# root.attributes("-alpha", 0.5)            # установка прозрачности с помощью атрибута alpha
root.attributes("-toolwindow", True)  # отключение верхней панели окна
root.protocol("WM_DELETE_WINDOW", finish)

state_list = [('вкл', 'green'),
              ('выкл', 'red'),
              ('ошибка', 'red')]

sensors_list = ['23 C', '35 %', '118 кВт*ч', '25010 ХВС\n17859 ГВС']

param_list = ['свет:',
              'вентиляция:',
              'подача воды:',
              'двери:',
              'ящики:',
              'окна:',
              'температура:',
              'влажность:',
              'расход электричества:',
              'расход воды:']

# MENU
btn_state = Button(root, text='Лист состояния', font=FONT_HEADER, command=state)
btn_settings = Button(root, text='Настройки', font=FONT_HEADER, command=settings)

# STATUS
btn_back = Button(root, text='Назад', font=LABEL_FONT, command=menu)

# SETTINGS
enabled_on = 'Вкл'
enabled_off = 'Выкл'
btn_reboot = Button(root, text='Перезагрузка системы', font=LABEL_FONT, state=DISABLED, command=reboot)

menu()

root.mainloop()
