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


def func_riddle(n, y):
    try:
        x = int(input('Enter number 1-100: '))
        if n == x:
            print('You guessed.')
        elif y == 1:
            print('You have run out of attempts.')
        else:
            if n > x:
                print('The hidden number is greater.')
            else:
                print('The hidden number is less.')
            func_riddle(n, y=y-1)
    except ValueError:
        print('You entered not an integer.')
        func_riddle(n, y)


if __name__ == '__main__':
    num = random.randint(1, 100)
    func_riddle(num, 10)
