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


def guess_the_number(number, counter=1):
    user_number = int(input('Введите число от 1 до 100: '))
    if user_number == number:
        print('Вы угадали число')
    elif counter == 10:
        print(f'Вы проиграли. Загаданное число - {number}')
    else:
        if user_number > number:
            print('Введенное число больше загаданного')
        else:
            print('Введенное число меньше загаданного')
        return guess_the_number(number, counter + 1)


selected_number = randint(0, 100)
guess_the_number(selected_number)
