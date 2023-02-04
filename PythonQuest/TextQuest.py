from time import *

forest = [
    '   /\\',
    '  /  \\',
    ' /____\\',
    '  /   \\   /\\',
    ' /__ __\\ /__\\',
    '  /   \\   / \\',
    ' /_____\\ /___\\',
    '   | |    | |'
]

house = [
    '   ___________ ',
    '  /           \\',
    ' /_____________\\',
    '|   __   |  |  |',
    '|  |__|  | ||  |',
    '|_______ |__|__|'
]

room = [
    '_______________________________',
    '|                |      |     |',
    '|                    2        |',
    '|-----|                       |',
    '|  1  |                    3 ||',
    '|     |                      ||',
    '|-----|                       |',
    '|                     4       |',
    '|__________________|__X__|____|'
]

safe_bit = [
    ' ______ ',
    '|      |',
    '|      |',
    '|      |',
    '|      |',
    '|______|'
]

safe_num = [
    [
        ' ______ ',
        '|  --  |',
        '| |  | |',
        '| |  | |',
        '|  --  |',
        '|______|'
    ],
    [
        ' ______ ',
        '|      |',
        '|   |  |',
        '|   |  |',
        '|   |  |',
        '|______|'
    ],
    [
        ' ______ ',
        '| ___  |',
        '|    | |',
        '| |--| |',
        '| |___ |',
        '|______|'
    ],
    [
        ' ______ ',
        '| ___  |',
        '|    | |',
        '| ---| |',
        '| ___| |',
        '|______|'
    ],
    [
        ' ______ ',
        '|      |',
        '| |  | |',
        '| |--| |',
        '|    | |',
        '|______|'
    ],
    [
        ' ______ ',
        '|  ___ |',
        '| |    |',
        '| |--| |',
        '| ___| |',
        '|______|'
    ],
    [
        ' ______ ',
        '|  __  |',
        '| |    |',
        '| |--| |',
        '| |__| |',
        '|______|'
    ],
    [
        ' ______ ',
        '| ___  |',
        '|    | |',
        '|    | |',
        '|    | |',
        '|______|'
    ],
    [
        ' ______ ',
        '|  __  |',
        '| |  | |',
        '| |--| |',
        '| |__| |',
        '|______|'
    ],
    [
        ' ______ ',
        '|  __  |',
        '| |  | |',
        '|  --| |',
        '|  __| |',
        '|______|'
    ]
]

key = [
    ' ____',
    '|    |',
    '|    |---------------',
    '|____|           |   |'
]

Map = [
    '_________________________ ',
    '| X-----<--<--     /|\\   |',
    '|            |     /|\\   |',
    '|     /|\\    |      |    |',
    '|      |     --<--<--    |',
    '|               O   | /|\\|',
    '|  Д ---->------->--- /|\\|',
    '|______________________|_|'
]


def cls():
    print("\n" * 100)


def print_delay(line, sec=0.05):
    for s in line:
        print(s, end='')
        sleep(sec)
    print()


def print_picture(picture):
    for line in picture:
        print(*line, sep='')


def print_safe(bit_1, bit_2, bit_3, bit_4):
    for i in range(len(bit_1)):
        print(f'{bit_1[i]}    {bit_2[i]}    {bit_3[i]}    {bit_4[i]}')


def scene_forest():
    sleep(2)
    print_delay('Представте, что вы очутились в глубоком лесу...')
    sleep(3)
    print()
    print_delay('Вокруг ни души, вы идёте и наслаждаетесь пением птиц, шелестом ветра')
    print()
    sleep(3)
    print_delay('Слышите?...')
    print()
    print_picture(forest)
    print()
    sleep(5)


def scene_house():
    print_delay('Вы так увлеклись окружением, что не заметили как перед вами появился дом')
    sleep(2)
    print_delay('Примерно такой:')
    print()
    sleep(1)
    print_picture(house)
    print()
    sleep(3)
    print_delay('"Куда это я забрёл. Похоже, я заблудился...", - подумали вы')
    sleep(3)
    print_delay('"Ух ты, настоящий охотничий домик!"')
    print_delay('Может там мне удастся что-нибудь найти...')
    print()
    print('###########################################')
    print('1. войти')
    print('###########################################')
    while (answer := input()) not in 'войти 1':
        print('введите цифру или слово')
        print()


def scene_room():
    print_delay('Войдя во внутрь, вы оказались в небольшой комнате')
    print_delay('Слева стоял деревянный столик')
    print_delay('Справа висела картина')
    print_delay('А прямо перед вами была ещё одна дверь')
    sleep(3)
    print()
    print_delay('"Так, и куда теперь?"')
    print()
    print_picture(room)
    print()
    print('(X) - ВЫ НАХОДИТЕСЬ ЗДЕСЬ')
    print()
    print('###########################################')
    print('1. стол   2. дверь   3. картина   4. выход')
    print('###########################################')

    while (answer := input()) not in '1 стол 2 дверь 3 картина 4 выход':
        print('введите цифру или слово')
        print()

    return answer


def scene_new_room():
    room[4] = '|     |X                   3 ||'
    print_delay('"Так, и куда теперь?"')
    print()
    print_picture(room)
    print()
    print('(X) - ВЫ НАХОДИТЕСЬ ЗДЕСЬ')
    print()
    print('###########################################')
    print('2. дверь   3. картина   4. выход')
    print('###########################################')

    while (answer := input()) not in '2 дверь 3 картина 4 выход':
        print('введите цифру или слово')
        print()

    return answer


def scene_table():
    room[4] = '|  1  |X                   3 ||'
    room[-1] = '|__________________|_____|____|'
    print_picture(room)
    print()
    print_delay('На столе лежало множество охотничьих вещей: компас, бинокли, котелки...')
    sleep(2)
    print_delay('Но ваше внимание привлекла маленькая коробочка с кодовым замком')
    print()
    sleep(3)
    print_safe(safe_bit, safe_bit, safe_bit, safe_bit)
    print()
    print('###########################################')
    print('введите 4 цифры (без пробела) или введите "выход"')
    print('###########################################')

    while (answer := input()) != 'выход' and not (len(answer) == 4 and answer.isdigit()):
        print('введите цифру или слово')
        print()

    return answer


def escape():
    cls()
    sleep(1)
    print_delay('Вы вставили ключ в замок')
    print()
    sleep(2)
    print_delay('Дверь щёлкнула и со скрипом отворилась...')
    print()
    sleep(2)
    print_delay('Вы зашли и попали в маленькую комнатку')
    print()
    sleep(1)
    print_delay('"Похоже, кладовка. Хм, что это?", - ваш взгляд упал на клочок бумаги...')
    print()
    sleep(2)
    print_picture(Map)
    print()
    sleep(5)
    print_delay('"Это карта!", - воскликнули вы')
    print_delay('"Теперь я смогу выбраться отсюда"')
    sleep(2)
    cls()
    print_delay('Вы прошли через долгий и тернистый путь, но, наконец, добрались до дома...')
    sleep(3)


scene = 0
print('-----------------------------------')
print('Добро пожаловать в Text Quest Game!')
print('-----------------------------------')
print()
print('###########################################')
print('Хотите начать? (введите цифру или слово)')
print('1. да    2. нет')
print('###########################################')

while (answer := input()) not in 'да нет 1 2':
    print('введите цифру или слово')
    print()

if answer in 'да 1':
    game = True
    scene = 0
else:
    game = False

while game:
    if scene == 0:
        cls()
        scene_forest()
        scene += 1
    elif scene == 1:
        cls()
        scene_house()
        scene += 1
    elif scene == 2:
        cls()
        ans = scene_room()
        if ans in '1 стол':
            scene = 3
        elif ans in '2 дверь':
            cls()
            sleep(1)
            print_delay('Вы дёрнули ручку двери')
            print()
            sleep(2)
            print_delay('"Хм, дверь закрыта. Нужно поискать ключ"')
            print()
            sleep(2)
            scene = 2
        elif ans in '3 картина':
            cls()
            sleep(1)
            print_delay('Вы вы подошли к картине')
            sleep(2)
            print_delay('На ней была фотография дома очень похожего на этот')
            sleep(1)
            print_delay('В углу красовалась надпись')
            print()
            sleep(1)
            print_delay('"Дом охотника. Дата основания 1998..."')
            sleep(1)
            print_delay('"Возможно, это пригодится"')
            sleep(3)
            scene = 2
        elif ans in '4 выход':
            cls()
            print_delay('Стены слишком давили на вас')
            print_delay('Вас начало мутить и вы выбежали прочь из этого дома')
            print()
            sleep(3)
            print_delay('Больше вас никто не видел...')
            sleep(5)
            game = False
    elif scene == 3:
        cls()
        ans = scene_table()
        if ans == 'выход':
            scene = 2
        else:
            a = [int(i) for i in ans]
            print_safe(safe_num[a[0]], safe_num[a[1]], safe_num[a[2]], safe_num[a[3]])
            if ans == '1998':
                print()
                sleep(3)
                print_delay('* Шелчок *')
                print()
                sleep(2)
                print_delay('"Ура, получилось!"')
                print()
                sleep(2)
                print_delay('Из коробочки вы достали ключ')
                print()
                sleep(2)
                print_picture(key)
                print()
                sleep(5)
                cls()
                scene = 4
            else:
                print()
                sleep(3)
                print_delay('Ничего не произошло')
                print_delay('Похоже пароль неверный')
                print()
                sleep(3)
                scene = 3
    elif scene == 4:
        ans = scene_new_room()
        if ans in '2 дверь':
            scene = 5
        elif ans in '3 картина':
            cls()
            sleep(1)
            print_delay('Вы вы подошли к картине')
            sleep(2)
            print_delay('На ней была фотография дома очень похожего на этот')
            sleep(1)
            print_delay('В углу красовалась надпись')
            print()
            sleep(1)
            print_delay('"Дом охотника. Дата основания 1998..."')
            sleep(1)
            print_delay('"Этим я уже воспользовался"')
            sleep(3)
            scene = 4
        elif ans in '4 выход':
            cls()
            print_delay('Стены слишком давили на вас')
            print_delay('Вас начало мутить и вы выбежали прочь из этого дома')
            print()
            sleep(3)
            print_delay('Больше вас никто не видел...')
            sleep(5)
            game = False
    elif scene == 5:
        escape()
        game = False

else:
    cls()
    print('КОНЕЦ')
    print()
    print('-----------------------------------')
    print('Спасибо за игру!')
    print('-----------------------------------')
