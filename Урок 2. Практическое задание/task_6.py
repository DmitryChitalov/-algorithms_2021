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

import random


def guess_number_up_to_100_in_10_tries(
        number=random.randint(0, 100),
        current_try=1,
        is_show_result=False
):
    # Базовый случай
    if current_try >= 10:
        print('К сожалению, попытки кончили, но вы так и не угадали')
        print(f'Загаданное число: {number}')
        return 1
    elif current_try == 1:
        print('Загадано число от 0 до 100. Вам требуется его отгадать')
        print('Мы же будем вам говорить это число больше или меньше')
        if is_show_result:
            print(f'Загаданное число: {number}')

    input_number_raw = input(f'Попытка {current_try}. Введите предполагаемое число: ')
    input_number = int(input_number_raw)

    if input_number > number:
        print(f'{input_number} больше, чем загаданное число')
    elif input_number < number:
        print(f'{input_number} меньше, чем загаданное число')
    # Базовый случай
    else:
        print(f'Поздавляю! вы угадали число: {number}')
        return 0

    current_try += 1
    # Шаг рекурсии
    guess_number_up_to_100_in_10_tries(number, current_try)


guess_number_up_to_100_in_10_tries()