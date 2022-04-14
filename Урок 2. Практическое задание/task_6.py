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

rand_start = 0
rand_end = 100


def guessing(number, attempt=10):
    guess = int(input(f"Угадайте число от {rand_start} до {rand_end}! "))
    attempt -= 1
    if guess == number:
        return print("Вы угадали!")
    elif attempt < 1:
        return print(f"Закончились попытки! Было загадано число: {number}")

    if guess < number:
        return print(f"Загаданное число больше! Осталось попыток {attempt}"), guessing(number, attempt)
    elif guess > number:
        return print(f"Загаданное число меньше! Осталось попыток {attempt}"), guessing(number, attempt)


guessing(randint(rand_start, rand_end))
