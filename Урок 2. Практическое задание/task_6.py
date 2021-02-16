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


def num(number=randint(0, 101), count=1):
    if count > 10:
        return print("attempts ended")
    answer = int(input("Input your number: "))
    if answer > number:
        print("Your answer is greater")
    elif answer < number:
        print("Your answer is less")
    else:
        return print("Victory")
    num(count=count+1)


num()
