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


def riddle_nub(rand_numb=None, count=9):
    if rand_numb is None:
        rand_numb = randint(0, 100)

    numb = int(input("Введите число: "))

    if numb == rand_numb:
        return "Вы отгадали загаднное число! Число = {}".format(rand_numb)
    elif count <= 0:
        return "Игра окончена вы проиграли! Загаданное число {}".format(rand_numb)
    elif numb > rand_numb:
        print("Число попыток {}".format(count))
        print("Число больше загаднного!")
        return riddle_nub(rand_numb, count - 1)
    elif numb < rand_numb:
        print("Число попыток {}".format(count))
        print("Число меньше загаднного!")
        return riddle_nub(rand_numb, count - 1)


print(riddle_nub())
