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


def func6(count: int = 10, rand_num=random.randint(0, 101)):
    answer = int(input('Отгадайте число от 0 до 100: '))
    if answer == rand_num:
        print(rand_num, 'Вы выиграли')
    elif count == 0:
        print(rand_num, 'Вы проиграли')
    else:
        if answer > rand_num:
            print('Число меньше')
            return func6(count - 1)
        if answer < rand_num:
            print('Число больше')
            return func6(count - 1)


func6()
