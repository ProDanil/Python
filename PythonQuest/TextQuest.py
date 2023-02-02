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
    ' ______',
    '|      |',
    '|      |'
    '|      |',
    '|      |',
    '|______|'
]

safe_num = [
    [
        ' ______',
        '|  --  |',
        '| |  | |',
        '| |  | |',
        '|  --  |',
        '|______|'
    ],
    [
        ' ______',
        '|   |  |',
        '|   |  |',
        '|   |  |',
        '|   |  |',
        '|______|'
    ],
    [
        ' ______',
        '| ___  |',
        '|    | |',
        '| |--| |',
        '| |___ |',
        '|______|'
    ],
    [
        ' ______',
        '| ___  |',
        '|    | |',
        '| ---| |',
        '| ___| |',
        '|______|'
    ],
    [
        ' ______',
        '| |  | |',
        '| |__| |',
        '|    | |',
        '|    | |',
        '|______|'
    ],
    [
        ' ______',
        '|  ___ |',
        '| |    |',
        '| |--| |',
        '| ___| |',
        '|______|'
    ],
    [
        ' ______',
        '|  __  |',
        '| |    |',
        '| |--| |',
        '| |__| |',
        '|______|'
    ],
    [
        ' ______',
        '| ___  |',
        '|    | |',
        '|    | |',
        '|    | |',
        '|______|'
    ],
    [
        ' ______',
        '|  __  |',
        '| |  | |',
        '| |--| |',
        '| |__| |',
        '|______|'
    ],
    [
        ' ______',
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
    print_delay('"Ух ты, настоящий охотничий домик!", - воскликнули вы')
    print_delay('Интересно, что там внутри?...')
    print()
    print('###########################################')
    print('1. войти')
    print('###########################################')
    while (answer := input()) not in 'войти 1':
        print('введите цифру или слово')
        print()


def scene_room():
    print_delay('Войдя во внутрь, вы оказались в небольшой комнате')
    print_delay('Слева вы увидели небольшой столик')
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
    scene = 1
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
            pass
        elif ans in '2 дверь':
            pass
        elif ans in '3 картина':
            pass
        elif ans in '4 выход':
            cls()
            print_delay('Стены слишком давили на вас')
            print_delay('Вас начало мутить и вы выбежали прочь из этого дома')
            print()
            sleep(3)
            print_delay('Больше вас никто не видел...')
            sleep(5)
            game = False
else:
    cls()
    print('КОНЕЦ')
    print()
    print('-----------------------------------')
    print('Спасибо за игру!')
    print('-----------------------------------')