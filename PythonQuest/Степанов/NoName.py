from turtle import *

print('игра')
print('некоторые рисунки появятся либо в другом приложении/вкладке или тут')
print('Вводить только цифры или слова да/нет')
print('неправильный ответ если порграмма просит ввести еще раз')
print('Выбери dver(4)#1')
u = int(input())

while u != 4:
    print('Повтор')
    u = int(input())



print('Выбери dver(4)#2')
t = int(input())
while t != 4:
    print('Повтор')
    t = int(input())


print('Выбери dver(4)#3')
t = int(input())
while t != 1:
    print('Повтор')
    t = int(input())


print('Выбери dver(4)#4')
t = int(input())
while t != 2:
    print('Повтор')
    t = int(input())



print('2 раунд(6дверей)')
print('Выбери dver(6)#1')
t = int(input())
while t != 6:
    print('Повтор')
    t = int(input())




print('Выбери dver(6)#2')
t = int(input())
while t != 1:
    print('Повтор')
    t = int(input())


print('Выбери dver(6)#3')
t = int(input())
while t != 2:
    print('Повтор')
    t = int(input())
print('вы можете отправится на раунд 6 сразу отправиться? да/нет')
print('тысячи нужно вводить с точкой например: 7000 - 7.000')
er = input()
if er == 'да':
    print('готово')
    print('Выбери dver(50)#1(дверь которая ближе равна:120-50-27')
    t = float(input())
    while t != 43:
        print('Повтор')
        t = float(input())


    print('Выбери dver(50)#2(дверь которая ближе равна:120-50-20')
    t = float(input())
    while t != 50:
        print('Повтор')
        t = float(input())


    print('Выбери dverь(50)#3(дверь которая ближе равна:1200-500-20')
    t = float(input())
    while t != 680:
        print('Повтор')
        t = float(input())





    print('Выбери dver(50)#4(дверь которая ближе равна:5000-2000+40.000-36.000')
    t = float(input())
    while t != 7.000:
        print('Повтор')
        t = float(input())


    print('Выбери dver(50)#5(дверь которая ближе равна:100.000-42.900+5-789')
    t = float(input())
    while t != 56.316:
        print('Повтор')
        t = float(input())


    print('Выбери dverь(50)#6(дверь которая ближе равна:1.000.000-45.000+7-56')
    t = float(input())
    while t != 954.951:
        print('Повтор')
        t = float(input())
    print('ПОБЕДА')

    begin_fill()
    fillcolor('green')
    color('green')
    forward(150)
    left(90)
    forward(50)
    left(90)
    forward(150)
    left(90)
    forward(50)
    left(90)
    hideturtle()
    end_fill()

    color('black')
    write('победа', font=("Arial", 20, "normal"))

    exitonclick()
else:
    print('ок')

    print('Выбери dverь(10)#1(дверь которая ближе равна:55-5')
    t = int(input())
    while t != 50:
        print('Повтор')
        t = int(input())
    print('Выбери dverь(10)#2(дверь которая ближе равна:2222-2223')
    t = int(input())
    while t != -1:
        print('Повтор')
        t = int(input())
    print('Выбери dverь(10)#1(дверь которая ближе равна:510-390')
    t = int(input())
    while t != 120:
        print('Повтор')
        t = int(input())
    print('игра пройденна')
    begin_fill()
    fillcolor('green')
    color('green')
    forward(150)
    left(90)
    forward(50)
    left(90)
    forward(150)
    left(90)
    forward(50)
    left(90)
    hideturtle()
    end_fill()
    color('black')
    write('победа', font=("Arial", 20, "normal"))
    hideturtle()
    exitonclick()
print('конец')
