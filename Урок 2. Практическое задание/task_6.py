import random

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


def game(n, count=1):
    try:
        user_answer = int(input(f'{11 - count} attempts\nEnter an integer from 0 to 100: '))
    except ValueError:
        print('You entered str-class!')
        return game(n, count)
    if count == 10:
        print('You are failed!')
    elif user_answer == n:
        print('You are win!')
    elif user_answer > n:
        print('The number is less!')
        return game(n, count + 1)
    else:
        print('The number is bigger!')
        return game(n, count + 1)


a = random.randint(0, 100)
game(a)
