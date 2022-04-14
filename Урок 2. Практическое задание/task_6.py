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
import random
number = random.randint(1, 100)

def guess_numb1(guesses_made = 0):
    guess = int(input('Введи число: '))
    guesses_made += 1
    if guess == number:
        return print(f"Ты угадал число!")
    if guesses_made == 10:
        return print(f"Ты исчерпал свои попытки! Загаданное число {number}")
    else:
        if guess < number:
            print('Твое число меньше загаданного.')
            return guess_numb1()
        if guess > number:
            print('Твое число больше загаданного.')
            return guess_numb1()
guess_numb1()


import random

def guess_numb2(count, numb):
    """Рекурсия"""
    print(f"Попытка №{count}")
    answer = int(input("Введите число от 0 до 100: "))
    if count == 10 or answer == numb:
        if answer == numb:
            print("Верно!")
        print(f"Загаданное число: {numb}")
    else:
        if answer > numb:
            print(f"Загаданное число меньше чем {numb}")
        else:
            print(f"Загаданное число больше чем {numb}")
        guess_numb2(count + 1, numb)


guess_numb2(1, random.randint(0, 100))

