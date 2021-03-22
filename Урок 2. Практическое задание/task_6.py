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


def Riddle(val, i=1):
    if i > 10:
        return f"Попытки закончились. Загаданное число: {val}"
    else:
        j = int(input("Угадайте число: "))
        if j < val:
            print(f"Загаданное число больше. Осталось {10 - i} попыток(-ки)")
        elif j > val:
            print(f"Загаданное число меньше. Осталось {10 - i} попыток(-ки)")
        else:
            return "Вы угадали число! Поздравляю!"
        return Riddle(val, i + 1)


print(Riddle(randint(0, 100)))
