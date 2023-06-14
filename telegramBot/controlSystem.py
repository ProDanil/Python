from tkinter.messagebox import showerror, showinfo

import pygame
from tkinter import *
from tkinter import ttk

HEIGHT = 360
WIDTH = 350
PASSWORD = '12345'
STATE = 'user'
TABLE = []
OBJECTS = []
ENABLED = []

# кортежи и словари, содержащие настройки шрифтов и отступов
FONT = ('Arial', 15, 'bold')              # шрифт параметров
FONT_HEADER = ('Arial', 15, 'bold')       # шрифт заголовков
FONT_ENTRY = ('Arial', 12)                # шрифт панели ввода
LABEL_FONT = ('Arial', 11)                # шрифт кнопок
BASE_PADDING = {'padx': 10, 'pady': 8}
HEADER_PADDING = {'padx': 10, 'pady': 12}


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


def destroy_object():
    global TABLE
    global OBJECTS
    global ENABLED

    for ob in OBJECTS:
        ob.pack_forget()
    OBJECTS = []

    for t in TABLE:
        t.grid_remove()
    TABLE = []
    ENABLED = []


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
    status, color = state_list[2]
    for c in range(2): root.columnconfigure(index=c)
    for r in range(len(param_list)): root.rowconfigure(index=r)
    for r in range(len(param_list)):
        label_param = Label(root, text=param_list[r],
                            font=FONT,
                            justify=LEFT)
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
    else:
        command = open_error
        btn_reboot['state'] = DISABLED
    for r in range(len(param_list)):
        enabled = StringVar(value=enabled_off)
        setting_label = Label(root, text=param_list[r],
                              font=FONT,
                              justify=LEFT)

        enabled_checkbutton = Checkbutton(textvariable=enabled,
                                          variable=enabled,
                                          offvalue=enabled_off,
                                          onvalue=enabled_on,
                                          font=LABEL_FONT,
                                          # state=DISABLED,
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
    window = Window(WIDTH, HEIGHT // 2)
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


def test():
    window = Window(WIDTH, HEIGHT)
    window.set_title('Опрос')
    text = 'Для перезагрузки системы пройдите тест'
    main_label = Label(window, text=text, font='Arial 12 italic')
    main_label.pack()


def reboot():
    window = Window(WIDTH, HEIGHT // 2, pos='+100+100')
    window.set_title('Перезагрузка')

    # заголовок
    main_label = Label(window, text='Идёт перезагрузка системы', font=FONT_HEADER, justify=CENTER, **HEADER_PADDING)
    main_label.pack()

    # настройка processbar
    value_var = IntVar()

    progressbar = ttk.Progressbar(window, orient="horizontal", variable=value_var)
    progressbar.pack(fill=X, padx=6, pady=6)

    label = ttk.Label(window, textvariable=value_var)
    label.pack(anchor=N, padx=6, pady=6)

    progressbar.start(100)  # запускаем progressbar
    test()


# def convert(lab, sw):
#     if lab['state'] == NORMAL:
#         lab["state"] = DISABLED
#         sw["text"] = "ON"
#     elif lab['state'] == DISABLED:
#         lab["state"] = NORMAL
#         sw["text"] = "OFF"


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

sensors_list = ['23 C', '35 %', '118 кВт*ч', '25010 ХВС 17859 ГВС']

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
