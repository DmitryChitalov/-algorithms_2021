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


def guess_number(number, try_count=1):
    try:
        user_number = int(input('Введите число от 1 до 100: '))
        if user_number == number:
            print('Вы выйграли')
        elif try_count == 10:
            print(f'Вы проиграли. Было загадано число: {number}')
        elif user_number < 0 or user_number > 100:
            print('Загадано число от 1 до 100')
            guess_number(number, try_count)
        else:
            print('Загаданное число меньше') if user_number > number else print('Загаданное число больше')
            try_count += 1
            guess_number(number, try_count)
    except ValueError:
        print('Ошибка ввода. Вы ввели не целое число.')
        guess_number(number, try_count)


if __name__ == '__main__':
    guess_number(random.randint(1, 100))
