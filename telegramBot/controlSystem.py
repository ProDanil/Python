import pygame
from tkinter import *
from tkinter import ttk

HEIGHT = 300
WIDTH = 300
FONT = 'Arial 15 bold'


def state():
    btn_state.pack_forget()
    btn_settings.pack_forget()
    root.title('Статус системы')
    state_label.pack()


def settings():
    pass


def finish():
    root.destroy()  # ручное закрытие окна и всего приложения
    print("Закрытие приложения")


pygame.init()

root = Tk()
root.title('Меню')
icon = PhotoImage(file='nastrojka.png')
root.iconphoto(False, icon)
root.geometry(f'{WIDTH}x{HEIGHT}')
root.resizable(0, 0)
#root.attributes("-alpha", 0.5)            # установка прозрачности с помощью атрибута alpha
root.attributes("-toolwindow", True)       # отключение верхней панели окна
root.protocol("WM_DELETE_WINDOW", finish)

btn_state = Button(root, text='Лист состояния', font=FONT, command=state)
btn_state.pack(fill=X, pady=50)

btn_settings = Button(root, text='Настройки', font=FONT, command=settings)
btn_settings.pack(fill=X, pady=10)

state_list = 'свет: ошибка\n' \
             'состояние дверей: ошибка'
state_label = Label(root, text=state_list, font=FONT)

root.mainloop()
