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
from random import randrange as rand

enigma = rand(0, 101)
print(enigma)  # для удобства проверки программы отображаю загаданное число


def guess_num(comp_num, i=0):
    try:
        human_num = int(input(f'Try to guess integer number from 0 to 100. You have {10-i} attempts for it: '))
        if human_num > 100 or human_num < 0:
            raise ValueError
    except ValueError:
        print('Please only integer numbers between 0 and 100!')
        guess_num(comp_num, i)
    else:
        if comp_num == human_num:
            print(f'Congratulations! You win!')
        elif i > 8:
            print(f'You have no attempts. The hidden number is {comp_num}.')
        else:
            print(f"Computer's number is smaller!") if comp_num < human_num else print(f"Computer's number is bigger!")
            return guess_num(comp_num, i + 1)


guess_num(enigma)
