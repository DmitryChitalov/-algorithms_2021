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


def guess_num(comp_num, i=10):
    user_num = int(input('Угадайте число от 0 до 100. Введите число: '))
    if comp_num == user_num:
        return print('Поздравляем! Вы угадали!')
    elif comp_num < user_num and i > 1:
        print(f'Вы ввели слишком большое число! У вас ещё {i-1} попыток.')
    elif comp_num > user_num and i > 1:
        print(f'Вы ввели слишком маленькое число! У вас ещё {i-1} попыток.')
    else:
        return print(f'Увы! Попытки исчерпаны! Загаданное число: {comp_num}.')
    return guess_num(comp_num, i-1)


num = randint(0, 100)
guess_num(num)
