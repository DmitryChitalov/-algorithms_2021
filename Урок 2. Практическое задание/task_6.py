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


def check_user_answer(right_answer, try_counter, max_try):

    if try_counter > max_try:
        print(f'К сожалению, вы не смогли угадать число за {max_try} попыток')
        quit()

    try:
        user_answer = int(input("Введите Ваш вариант:\n"))
    except ValueError:
        # В случае, если пользователь ввел строку, а не число, попытку не считаем сгоревшей
        print('Необходимо отгадать ЧИСЛО, а не строку')
        check_user_answer(right_answer, try_counter, max_try)

    if user_answer == right_answer:
        print(f'Вы угадали за {try_counter} попыток!')
    else:
        err_desc = f'Загаданное число меньше, чем {user_answer}' if user_answer > right_answer else f'Загаданное число больше, чем {user_answer}'
        print(err_desc)
        check_user_answer(right_answer, try_counter + 1, max_try)


rand_number = randint(0, 100)

check_user_answer(rand_number, 1, 10)
