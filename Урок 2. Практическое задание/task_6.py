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


def guess_number(number_to_guessed, current_attempt=1):
    if current_attempt > 10:
        print("No more attempts left")
        return
    else:
        number_to_try = int(input("Guess number (0-100): "))
        if number_to_guessed == number_to_try:
            print("You won")
            return
        else:
            if number_to_try > number_to_guessed:
                print("Less!")
            else:
                print("Greater!")
            current_attempt += 1
            guess_number(number_to_guessed, current_attempt)


chosen_number = random.choice(range(0, 100))
guess_number(chosen_number)
