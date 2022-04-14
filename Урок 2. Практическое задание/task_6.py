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


def guess_the_number(num: int, guesses=10):
    answer = int(input('Введите число: '))
    if answer < num:
        print('Загаданное число побольше')
    elif answer > num:
        print('Загаданное число поменьше')
    else:
        print('Вы победили!')
        return
    if guesses == 1:
        print('Вы проиграли, число', num)
        return
    guess_the_number(num, guesses - 1)


comp_num = randint(1, 100)
guess_the_number(comp_num)
