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


def get_correct_user_answer(answer, attempts):
    try:
        answer = int(input(f'Введите число от 0 до 100. Количество попыток: {attempts} \n'))
    except ValueError:
        print('Попытайтесь снова.')
        return get_correct_user_answer(answer, attempts)
    return answer, attempts


def mini_game_guess_the_number(answer, user_answer=None, attempts=10):
    if attempts == 0:
        print(f'Вы не угадали. Правильный ответ: {answer}')

    user_answer, attempts = get_correct_user_answer(user_answer, attempts)
    attempts -= 1

    if user_answer == answer:
        print(f'Поздравляю, Вы угадали! Ответ: {answer}')
        return

    print('Число меньше загаданного') if user_answer < answer else print('Число больше загаданного')
    return mini_game_guess_the_number(answer, user_answer, attempts)


comp_number = int(100 * random() - 1)
mini_game_guess_the_number(comp_number)
