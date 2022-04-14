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


def guess_the_number(number, hidden, attempts):
    if number == hidden:
        print(f"Поздравляю! Вы угадали! Загаданное число: {hidden}")
    elif attempts == 10:
        print(f"К сожалению, Вы не угадали :( Загаданное число: {hidden}")
    else:
        if number > hidden:
            print(f"Загаданное число меньше. Осталось попыток: {10 - attempts}")
            number = int(input("Введите число: "))
            guess_the_number(number, hidden, attempts + 1)
        else:
            print(f"Загаданное число больше. Осталось попыток: {10 - attempts}")
            number = int(input("Введите число: "))
            guess_the_number(number, hidden, attempts + 1)


user_number = int(input("Введите число: "))
hidden_number = randint(0, 100)
guess_the_number(user_number, hidden_number, 1)
