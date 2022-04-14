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


def guess_number(rand_num, _try=10):
    number = int(input("Enter the number: "))
    if _try == 0:
        return print(f'Game over. Number is: {rand_num}')
    else:
        if number == rand_num:
            return print(f'Correct')
        elif number < rand_num:
            print(f'Your number is smaller')
            return guess_number(rand_num, _try - 1)
        else:
            print(f'Your number is greater')
            return guess_number(rand_num, _try - 1)


if __name__ == '__main__':
    guess_number(randint(1, 100))
