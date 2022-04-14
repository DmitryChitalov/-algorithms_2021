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


def guess_num(attempt_counter, number):
    print(number)
    print('attempt num - %s' % attempt_counter)
    answer = int(input('enter num'))
    if answer == number or attempt_counter == 10:
        if answer == number:
            print('You guessed right - %s' % answer)
        else:
            print('There are no more attempts. The number was - %s' % number)
        return

    if number > answer:
        print('more')
    else:
        print('less')

    return guess_num(attempt_counter + 1, number)


guess_num(1, random.randint(1, 100))
