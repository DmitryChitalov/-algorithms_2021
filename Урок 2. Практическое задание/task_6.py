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
true_number = random.randint(0, 100)

def guessing_game(true_number, num_attempts=10):
    if num_attempts == 0:  # базовый случай
        print(f'Вы проиграли:( Загаданное число: {true_number}.')
    else:  # шаг рекурсии
        print(f'У вас осталось {num_attempts} попыток.')
        try:
            user_number = int(input('Угадайте натуральное число от 1 до 100: '))
        except ValueError:
            print("Введите натуральное число.")
            guessing_game(true_number, num_attempts)
        else:
            if user_number == true_number:
                print(f'Поздравляем! Вы угадали! Загаданное число {true_number}')
            elif user_number < true_number:
                print(f'Загаданное число больше вашего.')
                guessing_game(true_number, num_attempts - 1)
            else:
                print(f'Загаданное число меньше вашего.')
                guessing_game(true_number, num_attempts - 1)


guessing_game(true_number)
