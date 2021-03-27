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

def guess_number (tries = 10, number=str(randint(1,100))):
    user_try = input('Введите число от 0 до 100:')
    if tries < 1:
        return f'Попытки закончились, вы проиграли:'
    elif number == user_try:
        return f'Поздравляем! Вы угадали число&'
    elif number < user_try:
        print(f'Ваше число больше загаданого! Попробуйте снова.')
        return guess_number(tries-1, number)
    elif number > user_try:
        print(f'Ваше число меньше загаданого! Попробуйте снова. ')
        return guess_number(tries - 1, number)

print(guess_number())