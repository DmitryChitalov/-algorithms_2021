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
from random import randint


def my_func(attempt=10, number=str(randint(1, 100))):
    print(number)
    answer = input('Отгадайте число ')
    if attempt <= 1:
        return 'Попытки закончены '
    elif answer == number:
        return 'Вы победили! '
    elif answer < number:
        print('Ваше число меньше загаданного ')
        return my_func(attempt - 1, number)
    elif number < answer:
        print('Ваше число больше загаданного ')
        return my_func(attempt - 1, number)


print(my_func())
