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

expect_number = random.randint(0, 100)


def guess_number(expect_number, attempts=10):
    if attempts == 0:  # базовый случай
        print(f'Было загадано число: {expect_number}')
    else:  # шаг рекурсии
        print(f'Осталось попыток: {attempts}')
        try:
            user_number = int(input('Угадайте число в диапазоне от 1 до 100: '))
        except ValueError:
            print("Вы ошиблись. Это не натуральное число")
            guess_number(expect_number, attempts)
        else:
            if user_number == expect_number:
                print(f'Вы угадали. Загаданное число {expect_number}')
            elif user_number < expect_number:
                print(f'Загаданное число больше.')
                guess_number(expect_number, attempts - 1)
            else:
                print(f'Загаданное число меньше.')
                guess_number(expect_number, attempts - 1)


guess_number(expect_number)
