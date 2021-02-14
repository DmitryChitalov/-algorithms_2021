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


def game_guess(number_of_attempts=10, random_number=random.randint(0, 100)):
    print(random_number)
    try:
        user_answer = int(input('Угадайте число от 0 до 100: '))
    except ValueError:
        print('Данные необходимо вводить числами!')
        game_guess(number_of_attempts, random_number)
    else:
        if user_answer == random_number:
            print('Вы выиграли!')
        elif number_of_attempts == 1:
            print('Вы проиграли!')
        else:
            if user_answer > random_number:
                print('Слишком большое число. Нужно меньше')
            else:
                print('Слишком маленькое число! Нужно больше')
            print(f'Осталось попыток: {number_of_attempts - 1}')
            return game_guess(number_of_attempts - 1, random_number)


game_guess(10)


