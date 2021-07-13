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


def check_input():
    try:
        x = int(input('Введите чило: '))
        return x
    except:
        ex = input(f'Вы ввели не число... Надоело? [Y/N] ')
        if ex != 'Y'.lower():
            check_input()


def quest(target_number=randint(0, 100), attempts=10):
    if attempts > 0:
        attempts -= 1
        t = check_input()
        if t is not None:
            if t == target_number:
                print('Ураааа!!! Вы угадали!')
            elif t < target_number:
                print('Ваше число меньше задуманного. ')
                quest(target_number, attempts)
            elif t > target_number:
                print('Ваше число больше задуманного. ')
                quest(target_number, attempts)
        else:
            print('Нууу, не у всех хватает терпения играть в такие игры... ')
    else:
        print(f'Попытки кончились. Не угадали, а число было: {target_number}')


# Let's HAVE FUUUUUNNNNN!!!!!
quest()
