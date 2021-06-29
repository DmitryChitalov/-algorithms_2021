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


def guess_number(number, attenpt_count=10):
    user_number = int(input('Отгадайте число: '))
    if attenpt_count == 1:
        return print(f'Вы проиграли.Загаданное чило: {number}')
    else:
        if user_number < number:
            print(f'Ваше число меньше загаданного. У вас осталось {attenpt_count - 1} попыток')
            return guess_number(number, attenpt_count - 1)
        elif user_number > number:
            print(f'Ваше число больше загаданного. У вас осталось {attenpt_count - 1} попыток')
            return guess_number(number, attenpt_count - 1)
        elif number == user_number:
            return print(f'Поздравляю! Вы угадали! Загаданное число: {number}')


number = randint(0, 100)
f = guess_number(number)
