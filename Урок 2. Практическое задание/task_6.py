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
from random import randint


def guess(try_count=0, secret_num=randint(0, 100)):
    try:
        if try_count >= 10:
            print('Вы проиграли!')
            return
        user_answer = int(input('Введите число от 0 до 100: '))
        if user_answer > secret_num:
            print('Ваше число больше загаданного')
            try_count += 1
            guess(try_count, secret_num)
        elif user_answer < secret_num:
            print('Ваше число меньше загаданного')
            try_count += 1
            guess(try_count, secret_num)
        elif user_answer == secret_num:
            print('Вы отгадали!')
            return
    except ValueError as ex:
        print('Ошибка ввода, повторите!')
        guess(try_count, secret_num)


guess()
