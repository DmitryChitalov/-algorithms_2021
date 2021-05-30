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


def number_guess(attempt, number):
    user_number = int(input(f'Your choice: '))
    if user_number == number:
        print(f'You win!')
        return
    elif attempt == 1:
        print('*' * 40)
        print(f'Wrong!')
        print(f'The hidden number = {number}')
        return
    else:
        print('*' * 40)
        print('Please enter a larger number:' if user_number < number else 'Please enter a number less:')
        print(f'Remaining number of attempts: {attempt - 1}')
    number_guess(attempt - 1, number)


secret_number = randint(1, 100)
print('Guess a number from 1 to 100')
number_guess(10, secret_number)
