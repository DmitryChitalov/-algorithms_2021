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

n = randint(0, 100)


def try_to_guess(count=0):
    global n
    if count == 10:
        print(f'10 attempts ended.It was {n}. You lose')
        return
    else:
        user_guess = int(input('Input the guess: '))
        if user_guess == n:
            print(f'{n}! Congratulations! You win')
            return
        elif user_guess > n:
            print('Your number is more, try again')
            try_to_guess(count + 1)
        elif user_guess < n:
            print('Your number is less, try again')
            try_to_guess(count + 1)


try_to_guess()