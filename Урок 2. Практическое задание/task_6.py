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

random_number = random.randint(0, 100)
print(random_number)


def guessing(number, limit=9):
    while True:
        user_number = input("Введите натуральное число - ")
        if user_number.isdigit():
            user_number = int(user_number)
            break
    if limit == 0:
        return print("Вы не угадали число. Попыток не осталось")
    if user_number == number:
        return print("Поздравляем. Вы угадали число")
    else:
        if user_number > number:
            print("Загаданное число меньше")
            print(f"Попыток осталось: {limit}")
            return guessing(number, limit - 1)
        else:
            print("Загаданное число больше")
            print(f"Попыток осталось: {limit}")
            return guessing(number, limit - 1)


guessing(random_number)
