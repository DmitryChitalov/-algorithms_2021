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
from random import random


def mini_game_guess_the_number(answer, user_answer=None, attempts=10):
    if attempts == 0:
        print(f'Вы не угадали. Правильный ответ: {answer}')

    try:
        user_answer = int(input(f'Введите число от 0 до 100. Количество попыток: {attempts} \n'))
    except ValueError:
        print('Попытайтесь снова.')
        return mini_game_guess_the_number(answer, user_answer, attempts)
    attempts -= 1

    if user_answer == answer:
        print(f'Поздравляю, Вы угадали! Ответ: {answer}')
        return
    if user_answer < answer:
        print('Число меньше загаданного')
        return mini_game_guess_the_number(answer, user_answer, attempts)
    if user_answer > answer:
        print('Число больше загаданного')
        return mini_game_guess_the_number(answer, user_answer, attempts)


comp_number = int(100 * random() - 1)
mini_game_guess_the_number(comp_number)
