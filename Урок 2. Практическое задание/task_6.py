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


def numb_input():
    numb = input('Enter the number: ')
    return int(numb)


def numb_guess(rand_numb, cnt=10):
    numb = numb_input()
    if numb == rand_numb or cnt == 1:
        return f'Загаданное число: {rand_numb}'
    elif numb < rand_numb:
        print('Higher')
        return numb_guess(rand_numb, cnt - 1)




num = randint(0, 100)
print("I'm thinking of a number between 1 and 100 \nTry to guess it in ten tries or less")
print(numb_guess(num))