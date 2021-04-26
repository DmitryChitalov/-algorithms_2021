"""
6.	В программе генерируется случайное целое число от 0 до 100.
Пользователь должен его отгадать не более чем за 10 попыток. После каждой
неудачной попытки должно сообщаться больше или меньше введенное пользователем
число, чем то, что загадано. Если за 10 попыток число не отгадано,
то вывести загаданное число.

Решите через рекурсию. Решение через цикл не принимается.
Для оценки Отлично в этом блоке необходимо выполнить 5 заданий из 7

Подсказка:
Базовый случай здесь - угадали число или закончились попытки
"""


import random

goal_num = random.randint(1, 100)
count = 10


def nums_game(num, count_num):

    try:
        user_num = int(input('Введите целое число от 1 до 100: '))
    except ValueError:
        print('Ошибка ввода.')
        return nums_game(goal_num, count)

    if count_num == 0:
        print(f'Попыток осталось - {count_num}.\n'
              f'Загаданное число - {goal_num}\n')
        repeat = input('Введите "y", чтобы начать заново: ')
        if repeat == 'y' or repeat == 'Y':
            return nums_game(goal_num, count)
        else:
            return 'Игра окончена.'

    if user_num == goal_num:
        return f'Вы отгадали.\n' \
               f'Вам потербовалось {10 - count_num} попыток.'

    if user_num > goal_num:

        print(f'Ваше число больше загаданного.\n'
              f'Попыток осталось - {count_num}')
        return nums_game(goal_num, count_num - 1)

    if user_num < goal_num:

        print(f'Ваше число меньше загаданного.\n'
              f'Попыток осталось - {count_num}')
        return nums_game(goal_num, count_num - 1)


print(nums_game(goal_num, count))
