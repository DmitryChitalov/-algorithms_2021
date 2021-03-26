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
from random import randint

def guessing_game(num_attempt=10, user_number=-1, hidden_number=-1):
    print("Осталось попыток ", num_attempt)

    if hidden_number < 0:
        hidden_number = randint(0, 100)

    if num_attempt <= 0:
        print("Увы, вы не победили. Закончились попытки. Было загадано число ", hidden_number)
        exit()

    try:
        number = int(input("Введите число:"))
    except ValueError:
        print('Вы вместо числа ввели строку (((. Исправьтесь')
        return guessing_game(num_attempt, user_number, hidden_number)

    user_number = number
    if user_number == hidden_number:
        print("Поздравляем, вы угадали! Действительно, было загадано число ", hidden_number)
        exit()
    else:
        print("Загаданное число больше" if user_number < hidden_number else "Загаданное число меньше")
        num_attempt -= 1
        return guessing_game(num_attempt, user_number, hidden_number)


guessing_game()
