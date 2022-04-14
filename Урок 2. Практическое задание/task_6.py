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


def guess_a_number():

    def guess_number(number: int = randint(0, 100), tries_left: int = 10):
        if tries_left == 0:
            print(f"К сожалению, вы не смогли угадать! Я загадал число {number}.")
            return
        try_num = input(f"Попытка № {10 - tries_left}:")
        if not try_num.isdigit():
            print("Я загадал число от 0 до 100. Вы пытаетесь угадать что-то другое. Попробуйте ещё раз.")
            guess_number(number, tries_left)

        try_num = int(try_num)
        if try_num < number:
            print("Больше!")
            tries_left -= 1
            guess_number(number, tries_left)
        elif try_num > number:
            print("Меньше!")
            tries_left -= 1
            guess_number(number, tries_left)
        else:
            print("УГАДАЛИ!")
            return

    print("Я загадал число от 0 до 100. Попробуйте угадать!")
    guess_number()
    if input("Хотите сыграть ещё раз (y/n)[n]?") == 'y':
        guess_a_number()


if __name__ == '__main__':
    guess_a_number()
