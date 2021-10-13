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

from random import random


def name_number(secret_number, number_attempts):
    if number_attempts == 0:
        print('Вы не угадали. Ответ -', secret_number)
    else:
        if number_attempts == 10:
            print('Угадайте число, загаданное компьютером')
        number_user = int(input("Введите число от 0 до 100 "))
        if number_user < secret_number:
            print('Не угадали. Ваше число меньше')
            return name_number(secret_number, number_attempts - 1)
        elif number_user > secret_number:
            print('Не угадали. Ваше число больше')
            return name_number(secret_number, number_attempts - 1)
        elif number_user == secret_number:
            print('Ура! Число угадано!')


if __name__ == '__main__':
    name_number(round(random() * 100), 10)
