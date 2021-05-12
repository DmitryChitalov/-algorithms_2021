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

def guessing(number, attemps):
    user_answer = input('Ввеедите число: ')
    try:
        user_answer = int(user_answer)
    except Exception:
        print('Вы ввели строку, а не число! Исправьтесь')
        return guessing(number, attemps)
    if user_answer == number and attemps > 1:
        return print(f'Верно! загаданное число - {number}')
    elif user_answer < number and attemps > 1:
        print('Введенное число меньше загаданного!')
    elif  user_answer > number and attemps > 1:
        print('Введенное число больше загаданного!')
    else:
        return print('Попытки кончились! Вы проиграли!')
    attemps -= 1
    guessing(number, attemps)

if __name__ == '__main__':
    attemps = 10
    number = random.randint(1, 100)
    guessing(number, attemps)


