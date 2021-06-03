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


def guess_number(number: int = 0, attempt: int = 0, max_attempts: int = 10):
    if attempt == 0:
        return guess_number(random.randint(0, 100), 1, max_attempts)

    if attempt > max_attempts:
        print(f'Вы не угадали. Искомое число: {number}')
        return

    try:
        user_number = int(input(f'Угадайте число от 0 до 100 (осталось попыток {max_attempts - attempt + 1}): '))
    except ValueError:
        print(f'Вы ввели не число!')
        return guess_number(number, attempt+1, max_attempts)

    if user_number == number:
        print(f'Поздравляю вы угадали!')
        return
    elif user_number > number:
        print(f'Искомое число меньше')
        return guess_number(number, attempt+1, max_attempts)
    else:
        print(f'Искомое число больше')
        return guess_number(number, attempt + 1, max_attempts)


guess_number()
