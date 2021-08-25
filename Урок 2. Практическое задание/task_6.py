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


def enter_number():
    try:
        val = abs(int(input('Please enter some number\n')))
    except ValueError:
        print("Error you've entered incorrect value")
        return enter_number()
    return val


def guess_number(number, count=10):
    vol = enter_number()
    if vol != number:
        if count > 1:
            if vol > number:
                print(f'The hidden number is less than yours please try again\n'
                      f'number of attempts = {count-1}')
                return guess_number(number, count-1)
            if vol < number:
                print(f'The hidden number is bigger than yours please try again\n'
                      f'Number of attempts = {count-1}')
                return guess_number(number, count-1)
        print(f'Attempts ended you lost\nThe hidden number is {number}')
        exit()
    print("It's correct! You won!!!")


num = random.randint(0, 100)
# print(num)
guess_number(num)
