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
number = random.randint(0,100)
def guess(n, tries = 10):
    if tries == 0:
        return f"You lose((( Game is Over!!! Proper value is {n}"
    try:
        user_guess = int(input("Input your guess please>>> "))
    except ValueError:
        print("Input value is incorrect, please input number from 0 to 100 ")
        return  guess(n, tries)
    if user_guess > n:
        print("Your guess is greater then number")
    elif user_guess == n:
        return f"Congratulations you won!!! "
    elif user_guess < n:
        print("Your guess is less then number")
    return guess(n,tries - 1)

print(guess(number))
