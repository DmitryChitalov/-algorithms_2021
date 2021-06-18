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
from task_1 import is_int


def guess_number(number, count=10):
    user_number = is_int(input(f'Попытка №{count}. Введите число от 0 до 100: '))
    if user_number is None or user_number < 0 or user_number > 100:
        print('Надо вводить числа только от 0 до 100. Попробуйте еще.')
        guess_number(number, count)
        return
    elif user_number == number:
        print(f'Ура!!! Вы угадали! Это действительно число {number}')
        return
    elif count == 1:
        print(f'Вы не угадали, закончились попытки. Загаданное число: {number}')
        return
    elif user_number < number:
        print('Загаданное число больше, чем Вы ввели')
    else:
        print('Загаданное число меньше, чем Вы ввели')
    guess_number(number, count - 1)


hidden_number = randint(0, 100)
guess_number(hidden_number)
