"""
6.	В программе генерируется случайное целое число от 0 до 100.
Пользователь должен его отгадать не более чем за 10 попыток. После каждой
неудачной попытки должно сообщаться больше или меньше введенное пользователем
число, чем то, что загадано. Если за 10 попыток число не отгадано,
то вывести загаданное число.

Подсказка:
Базовый случай здесь - угадали число или закончились попытки

Решите через рекурсию. Решение через цикл не принимается.
Для оценки Отлично в этом блоке необходимо выполнить 5 заданий из 7
"""

from random import randint

random_number = randint(0, 101)
x = 0
print(random_number)


# def guess_game(number, shot):
#     if shot < 10:
#         user_number = int(input('Введите Ваше число от 0 до 100: '))
#         if user_number == number:
#             print(f'Число отгадано верно: {user_number} за {shot} попыток.')
#         else:
#             if user_number < number:
#                 print(f'Загаданное число больше Вашего.')
#             else:
#                 print(f'Загаданное число меньше Вашего.')
#             shot += 1
#             print(f'Число не отгадано. Осталось {(10 - shot)} попыток.')
#             guess_game(number, shot)
#     else:
#         print(f'Вы не угадали. Было загадано число {number}.')
#
#
# guess_game(random_number, x)


def guess_game(shot=10):
    try:
        if shot == 0:
            print(f'Вы проиграли,попытки закончились, загаданное число: {random_number}')
            return

        user_number = int(input('Введите число от 0 до 100: '))

        if user_number == random_number:
            print('Поздравляю! Вы выиграли!')
            return

        if user_number < random_number:
            print(f'Ваше число меньше загаданного, осталось {shot - 1} попыток')

        elif user_number > random_number:
            print(f'Ваше число больше загаданного, осталось {shot - 1} попыток')

        shot -= 1

        return guess_game(shot)

    except ValueError:
        print('Вы ввели строку (((. Исправьтесь')
        return guess_game(shot)


guess_game()
