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


def game(number=random.randint(0, 100), try_less=9):
    clients_number = int(input('Please enter the number that you think: '))
    if clients_number == number or try_less == 0:
        return print(f'The number was {number}')
    elif clients_number > number:
        print('The number that you inserted is too big! ')
    else:
        print("The number that you inserted is too small! ")
    try_less = try_less - 1
    return game(number, try_less)


game()
