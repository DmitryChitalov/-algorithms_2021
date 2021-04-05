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


def guess_the_number(number, attempt=10, message=''):
    if message:
        print(message)
    try:
        answer = int(input('Угадайте число от 0 до 100: '))
        if attempt == 1:
            print('Вы проиграли.')
            return
        elif answer == number:
            print(f'Победа!!! Правильный ответ {number}')
            return
        elif answer < number:
            guess_the_number(number, attempt - 1, f'Ваш ответ слишком маленький.'
                                                  f'\nКоличество попыток: {attempt - 1}')
        elif answer > number:
            guess_the_number(number, attempt - 1, f'Ваш ответ слишком большой.'
                                                  f'\nКоличество попыток: {attempt - 1}')
    except ValueError:
        guess_the_number(number, attempt - 1, f'Только натуральные числа.'
                                              f'\nКоличество попыток: {attempt - 1}')


guess_the_number(random.randrange(0, 100))
