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


def guess(number, attempt=1):
    user_input = input(f" Попытка № {attempt}. Введите число от 0 до 100: ")
    try:
        guessed_number = int(user_input)
    except ValueError:
        guessed_number = None
    if attempt == 10 and guessed_number != number:
        print('You lost !!!')
        return None
    elif guessed_number == number:
        print ('You are the winner !!!')
        return None
    else:
        if guessed_number is None:
            print('Вы ввели не число.')
        elif guessed_number < number:
            print('Вы ввели число меньше.')
        elif guessed_number > number:
            print('Вы ввели число больше. ')
        return guess(number, attempt+1)


guess(random.randint(0, 100))
