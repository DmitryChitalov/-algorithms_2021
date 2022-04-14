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

import random


def recur_method(count, numb):
    print('Попытка №', count)
    answer = int(input('Введите число от 0 до 100: '))
    if count == 10 or answer == numb:
        print('Загаданное число', numb)
        if answer == numb:
            print('Верно')
        print('Загаданное число', numb)
    else:
        if answer > numb:
            print('Загаданное число меньше чем', numb)
        else:
            print('Загаданное число больше чем', numb)
        recur_method(count+1, numb)


recur_method(1, random.randint(0, 100))

