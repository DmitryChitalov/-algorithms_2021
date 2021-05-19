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


def guess_game(attempts, num=int(randint(1, 100))):
    if attempts == 0:
        return f'Загаданное число было: {num}'
    guess = int(input('Введите число '))
    if guess == num:
        return f'Поздравляю, Вы угадали!'
    elif guess > num:
        print('Вы ввели слишком большое число')
        return guess_game(attempts - 1)
    elif guess < num:
        print('Вы ввели слишком маленькое число')
        return guess_game(attempts - 1)


print(guess_game(7))
