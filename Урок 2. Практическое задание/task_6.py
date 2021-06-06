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

def game(rand, attempt=9):
    user_input = int(input('Введите число от 1 до 100: '))
    if user_input == rand:
        return f'Вы угадали с {10 - attempt} попытки!'
    elif attempt == 0:
        return f'Ваши попытки закончились.\nБыло загадано {rand}.'
    else:
        print('Ваше число больше загаданного') if user_input > rand \
            else print('Ваше число меньше загаданного')
    attempt -= 1
    return game(rand, attempt)

print(game(random.randint(1, 101)))
