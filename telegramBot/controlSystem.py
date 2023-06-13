from tkinter.messagebox import showerror

import pygame
from tkinter import *
from tkinter import ttk

HEIGHT = 360
WIDTH = 350
FONT = 'Arial 15 bold'
TABLE = []
OBJECTS = []


def destroy_object():
    global TABLE
    global OBJECTS

    for ob in OBJECTS:
        ob.pack_forget()
    OBJECTS = []

    for t in TABLE:
        t.grid_remove()
    TABLE = []


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
    btn_back.grid(pady=10, padx=10)
    TABLE.append(btn_back)


def settings():
    radio_btn = Radiobutton(root)


def open_error():
    showerror(title="Ошибка", message="У вас нет прав доступа", detail="Авторизируйтесь от имени администратора",)


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

btn_state = Button(root, text='Лист состояния', font=FONT, command=state)

btn_settings = Button(root, text='Настройки', font=FONT, command=settings)

btn_back = Button(root, text='Назад', font=FONT, command=menu)

menu()

root.mainloop()

# from tkinter import *
# 
# ws = Tk()
# ws.title("Python Guides")
# 
# 
# def convert():
#     if a1['state'] == NORMAL:
#         a1["state"] = DISABLED
#         a2["text"] = "ON"
#     elif a1['state'] == DISABLED:
#         a1["state"] = NORMAL
#         a2["text"] = "OFF"
# 
# 
# a1 = Label(ws, text="Bulb")
# a1.config(height=8, width=9)
# a1.grid(row=0, column=0)
# a2 = Button(text="OFF", command=convert)
# a2.grid(row=0, column=1)
# ws.mainloop()
